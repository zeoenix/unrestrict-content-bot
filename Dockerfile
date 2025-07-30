FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY . .

# Create a simple server that runs both health check and bot
COPY minimal_server.py health_server.py

# Run both the health server and bot using a simple shell script
RUN echo '#!/bin/bash\npython health_server.py &\npython bot.py' > start.sh && chmod +x start.sh

CMD ["bash", "start.sh"]
