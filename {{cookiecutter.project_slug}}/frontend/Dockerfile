# Use an official node runtime as a parent image
FROM node:13.6.0

WORKDIR /app/

# Install dependencies
RUN npm install -g npm-check-updates
COPY package.json yarn.lock /app/

RUN npm install

# Add rest of the client code
COPY . /app/

EXPOSE 3000

CMD npm start