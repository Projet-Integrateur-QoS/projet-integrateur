FROM node

WORKDIR /data

COPY package.json .

RUN npm install

COPY . .

EXPOSE ${FRONT_PORT}

ENTRYPOINT [ "npm", "start" ]