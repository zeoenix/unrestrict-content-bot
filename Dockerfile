FROM python:3.11-slim

WORKDIR /app

# Copy simple emergency diagnostic as bot.py
COPY emergency_simple.py bot.py

CMD ["python", "bot.py"]
