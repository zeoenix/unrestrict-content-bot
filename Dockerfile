# Use official Python runtime as base image
FROM python:3.10.8-slim-buster

# Set working directory
WORKDIR /app

# Create non-root user for security
RUN groupadd -r botuser && useradd -r -g botuser botuser

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p logs downloads temp \
    && chown -R botuser:botuser /app

# Switch to non-root user
USER botuser

# Expose port for Flask app
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

# Validate configuration and run
CMD ["sh", "-c", "python validate_config.py && python app.py & python bot.py"]
