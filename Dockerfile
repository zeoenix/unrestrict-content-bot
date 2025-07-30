FROM python:3.11-slim

WORKDIR /app

# Copy the diagnostic script
COPY diagnostic.py .

# Run diagnostics (will stay alive for 5 minutes)
CMD ["python", "diagnostic.py"]
