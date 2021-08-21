FROM node:13.12.0-alpine

# Run examples:
# docker build . -t test_image_server
# docker images --all
# REPOSITORY          TAG       IMAGE ID       CREATED              SIZE
# test_image_server   latest    15c45de05ebd   About a minute ago   177MB    <------------------
# docker101tutorial   latest    936ea8b30f6d   2 days ago           28.2MB
# alpine/git          latest    b8f176fa3f0d   2 months ago         25.1MB
# docker run   --hostname test --ip 10.1.2.3 15c45de05ebd 
# https://hub.docker.com/_/alpine
# Install python/pip
FROM alpine:3.14
# https://wiki.alpinelinux.org/wiki/Mysql
RUN apk add mysql mysql-client
# RUN apk add --no-cache mysql-client
# ENTRYPOINT ["mysql"]

# FROM ubuntu:20.04
# RUN apt-get update \
#     && apt-get install -y --no-install-recommends mysql-client \
#     && rm -rf /var/lib/apt/lists/*
# ENTRYPOINT ["mysql"]
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
# WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour 
# with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install pipenv
RUN pipenv install flask

# RUN npm install -g create-react-app

# MOVED TO BEGINNING beginning 
# FROM node:13.12.0-alpine

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install

# add app
COPY . ./

# start app
CMD ["npm", "start"]    



# START SERVER 







# https://stackoverflow.com/questions/11657829/error-2002-hy000-cant-connect-to-local-mysql-server-through-socket-var-run
# RUN  mysql start
# RUN mysql -h 127.0.0.1 -P 3306
# -u root -p root 

#  => ERROR [8/8] RUN mysql -h 127.0.0.1 -P 3306                                                                   0.4s 
# ------
#  > [8/8] RUN mysql -h 127.0.0.1 -P 3306:
# #11 0.349 ERROR 2002 (HY000): Can't connect to MySQL server on '127.0.0.1' (115)


# RUN pipenv shell
