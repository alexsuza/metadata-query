# Use CentOS 7 as the base image
FROM centos:7

# Install Python 3 and pip
RUN yum -y update && \
    yum -y install epel-release && \
    yum -y install python36 python36-pip

# Change the working directory
WORKDIR /app

# Copy current directory contents into the container at /app
COPY . .

# Print directory contents for debugging
RUN ls -la

# Install the Python dependencies from requirements.txt
RUN pip3 install -r requirements.txt && \
    pip3 install -U python-dotenv

# The command to run the application
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]


# To build this file
# RUN$ docker build -t dbinfo .
# docker run -d -p 5000:5000 dbinfo
# (to store build log) RUN$ docker build -t dbinfo . > build.log 2>&1
