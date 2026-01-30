# -------------------------
# Base image
# -------------------------
FROM python:3.11-slim

# -------------------------
# Environment variables
# -------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# -------------------------
# Set working directory
# -------------------------
WORKDIR /app

# -------------------------
# System dependencies
# (needed for psycopg2, Pillow, Tailwind, etc.)
# -------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# -------------------------
# Install Python dependencies
# -------------------------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# -------------------------
# Install Node dependencies (Tailwind)
# -------------------------
COPY package.json package-lock.json ./
RUN npm install

# -------------------------
# Copy project files
# -------------------------
COPY . .

# -------------------------
# Build Tailwind CSS
# -------------------------
# CHANGE THIS if your Tailwind command is different
RUN npm run build:tailwind

# -------------------------
# Collect static files
# -------------------------
# CHANGE SETTINGS MODULE if needed
RUN python manage.py collectstatic --noinput

# -------------------------
# Expose port
# -------------------------
EXPOSE 8000

# -------------------------
# Run Django with Gunicorn
# -------------------------
# CHANGE "myproject" to your actual project name
CMD ["gunicorn", "envision.wsgi:application", "--bind", "0.0.0.0:8000"]
