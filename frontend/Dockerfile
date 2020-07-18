FROM node:latest

WORKDIR /code
COPY package.json /code

RUN npm ci
# COPY . /code
# RUN npm run build

# EXPOSE 3000

CMD ["npm", "start"]
