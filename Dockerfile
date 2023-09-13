# Use RHEL 8 as the base image
FROM registry.access.redhat.com/ubi8/ubi:latest

# Install Python 3 and pip
RUN yum -y update && \
    yum -y install python38 python38-pip && \
    yum clean all

# Change the working directory
WORKDIR /app

# Install the Python dependencies from requirements.txt
# This is moved up here to leverage Docker cache
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt && \
    pip3 install --no-cache-dir -U python-dotenv==0.15.0

# Copy current directory contents into the container at /app
COPY . .

# Print directory contents for debugging
RUN ls -la

# The command to run the application
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]
