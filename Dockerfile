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
ENV NO_PROXY="si0vm03536.de.bosch.com,si0vm03537.de.bosch.com,si0vm03538.de.bosch.com,.de.bosch.com,.bosch.com,.cluster.local,.svc,10.140.180.0/23,10.140.214.0/24,10.140.249.0/24,10.140.250.30,10.140.254.0/24,10.40.0.0/24,127.0.0.1,169.254.169.254,192.168.0.0/17,192.168.128.0/17,api-int.de3pro.osh.ipz001.internal.bosch.cloud,etcd-0.de3pro.osh.ipz001.internal.bosch.cloud,etcd-1.de3pro.osh.ipz001.internal.bosch.cloud,etcd-2.de3pro.osh.ipz001.internal.bosch.cloud,internal.bosch.cloud,localhost,osh.ipz001.internal.bosch.cloud"

# Define the command to run your FastAPI script using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
