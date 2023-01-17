FROM node

COPY package.json /app/

WORKDIR /app/data

RUN npm install

COPY . .

EXPOSE ${FRONT_PORT}