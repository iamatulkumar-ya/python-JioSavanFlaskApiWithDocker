# Let's get the base image for our application 
FROM python:alpine3.18 as base

# Let's define the work directory for our appllication 
WORKDIR /var/app

# Setting env variable which will be used by flask 
ENV FLASK_APP=./src/startup.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV JIO_SAVAN_SEARCH_SONG_URL=https://saavn.me/search/songs?query=

# Copy requirements.txt file to install the dependencies
COPY requirements.txt requirements.txt

# Now let's install the dependencies
RUN pip install -r requirements.txt

# Exposing the port such that we can run our code
EXPOSE 5000
EXPOSE 80
# Let's copy everything into the WORKDIR
COPY . .

# Run the command to execue our file
CMD ["flask", "run"]