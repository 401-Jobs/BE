FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
COPY requirments.txt /code/
COPY . /code/
WORKDIR /code

# Install dependencies
COPY requirments.txt /code/
RUN pip install -r requirments.txt

# Copy project
COPY . /code/