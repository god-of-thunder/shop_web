# Use an official Python runtime as the base image
FROM python:3.9

# Install system dependencies for MySQL client
RUN apt-get update && apt-get install -y default-libmysqlclient-dev netcat
# 安装wait-for脚本

ADD https://github.com/eficode/wait-for/raw/master/wait-for /usr/local/bin/wait-for
RUN chmod +x /usr/local/bin/wait-for

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .


# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the Django project to the container
COPY . .

# Run the Django development server
CMD ["wait-for", "mysql:3306","--","python", "manage.py", "runserver", "0.0.0.0:8000"]