FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install (needed for proper Railway deployment)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the final combined server
COPY final_combined.py .
COPY bot.py .
COPY config.py .
COPY database/ database/
COPY TechVJ/ TechVJ/

# Expose port
EXPOSE 8080

CMD ["python", "final_combined.py"]
