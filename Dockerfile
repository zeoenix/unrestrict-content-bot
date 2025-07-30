FROM python:3.11-slim

WORKDIR /app

# Copy the simple HTTP server (no dependencies needed)
COPY simple_http.py .

# Expose port
EXPOSE 8080

CMD ["python", "simple_http.py"]
