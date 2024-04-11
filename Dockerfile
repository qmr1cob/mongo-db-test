# Use the official Python image from Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the certificate file into a commonly used directory
COPY BOSCH-CA-DE_pem_1.cer /usr/local/share/ca-certificates/

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Set environment variables from .env file
ENV PATH="/app:${PATH}"
ENV MONGO_URI="mongodb://ttf1cob:T6krof-KrLrlDiBT@si0vm03536.de.bosch.com:30000,si0vm03537.de.bosch.com:30000,si0vm03538.de.bosch.com:30000/dataxpress?replicaSet=PS_Dev&tls=true&tlsCAFile=/usr/local/share/ca-certificates/BOSCH-CA-DE_pem_1.cer"
ENV MONGO_DB="dataxpress"
ENV MONGO_COLLECTION="dataxpress-xorder-status"
ENV HTTP_PROXY=http://10.143.16.65:8080
ENV HTTPS_PROXY=http://10.143.16.65:8080
# ENV NO_PROXY="si0vm03536.de.bosch.com"

# Define the command to run your FastAPI script using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
