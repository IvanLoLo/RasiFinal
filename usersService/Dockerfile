FROM python:3.12-alpine

WORKDIR /app

# Copy the django app to the working directory
COPY . /app

# Set the environment variables
ENV DB_USERNAME unaldinos
ENV DB_PASSWORD unaldinos
ENV DB_HOST 10.128.0.5
ENV DB_PORT 27017
ENV DB_NAME users_db
ENV JWT_SECRET t0pS3cr3t

# Install Python dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["sh", "init.sh"]