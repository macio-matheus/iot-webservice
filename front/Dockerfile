FROM node:8.11

RUN mkdir /app
RUN mkdir /app_temp
WORKDIR /app_temp

# INSTALL DEPENDENCIES
COPY package.json /app_temp

# Update & Install theses apps.
RUN apt-get update && apt-get upgrade -y && apt-get install -y rsync
RUN npm config set strict-ssl false
RUN npm install --no-bin-links
RUN npm install -g nodemon@1.14.12

WORKDIR /app

EXPOSE 5000