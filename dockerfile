# Use the official Python image as the base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Collect static files (this will gather all static files into the STATIC_ROOT directory)
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Run migrations and start Gunicorn
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && gunicorn blog_App.wsgi:application --bind 0.0.0.0:8000"]
