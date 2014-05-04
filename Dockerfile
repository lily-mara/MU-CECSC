FROM ubuntu:14.04

RUN ["apt-get", "install", "-y", "curl", "python3", "build-essential", "python3-dev", "nginx", "supervisor"]
RUN curl https://bootstrap.pypa.io/get-pip.py | python3 -
RUN ["pip", "install", "tornado", "requests"]

RUN ["mkdir", "/var/www"]

ADD . /var/www/mu-cec/
ADD supervisord.conf /etc/supervisor/supervisord.conf