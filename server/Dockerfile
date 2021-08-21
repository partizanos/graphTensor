

# FROM alpine:3.14
# # https://wiki.alpinelinux.org/wiki/Mysql
# # RUN apk add mysql mysql-clientRUN npm -v
# ENV PYTHONUNBUFFERED=1
# RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
# RUN python3 -m ensurepip
# # WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour 
# # with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
# RUN pip3 install --no-cache --upgrade pip setuptools
# RUN pip3 install pipenv
# RUN pipenv install flask
# # COPY --from=0 /go/src/github.com/alexellis/href-counter/app ./
# # CMD ["./app"]  





# syntax=docker/dockerfile:1
FROM node:13.12.0-alpine
COPY app ./app
COPY backend ./backend
WORKDIR /app
EXPOSE 3000
RUN npm -v
RUN npm install
# RUN npm start
# RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

