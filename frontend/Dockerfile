FROM node:latest

ADD . /code
WORKDIR /code

RUN npm install
# COPY . /code
# RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
