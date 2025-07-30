FROM python:3.11-slim

WORKDIR /app

# Copy the container test script
COPY container_test.py .

# Test run (will exit after printing diagnostics)
CMD ["python", "container_test.py"]
