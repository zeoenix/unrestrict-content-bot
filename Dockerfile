FROM python:3.11-slim

WORKDIR /app

# Copy bot.py but rename our diagnostic as bot.py so Railway runs it
COPY diagnostic.py bot.py

# Also copy the real diagnostic for reference
COPY diagnostic.py .

CMD ["python", "bot.py"]
