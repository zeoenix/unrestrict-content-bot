FROM python:3.11-slim

WORKDIR /app

# Copy the minimal server
COPY minimal_server.py .

# No healthcheck - let's see if container runs at all
CMD ["python", "minimal_server.py"]
