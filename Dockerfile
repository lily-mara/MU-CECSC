FROM ubuntu:14.04

RUN ["apt-get", "install", "-y", "curl", "python3", "build-essential", "python3-dev", "git", "nginx", "supervisor"]
RUN curl https://bootstrap.pypa.io/get-pip.py | python3 -
RUN ["pip", "install", "tornado", "requests"]

RUN ["mkdir", "/var/www"]
RUN ["git", "clone", "https://github.com/natemara/mu-cecsc", "/var/www/mu-cec"]

ENTRYPOINT ["/var/www/mu-cec/server.py"]