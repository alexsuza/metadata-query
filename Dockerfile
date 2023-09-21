FROM ubuntu

RUN apt update
RUN apt install python3-pip -y

WORKDIR /app

COPY . .

# Print directory contents for debugging
RUN ls -la

RUN pip install -r requirements.txt
RUN pip3 install -U python-dotenv

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]

# To build this file
# RUN$ docker build -t dbinfo .
# docker run -d -p 5000:5000 dbinfo
# (to store build log) RUN$ docker build -t dbinfo . > build.log 2>&1

# Tag and Push image to hub ()
# docker tag dbinfo:latest brainchild87/metademo:latest
# docker push brainchild87/metademo:latest
# docker pull brainchild87/metademo:latest