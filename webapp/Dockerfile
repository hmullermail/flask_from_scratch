FROM centos:latest

ENV container docker

RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \
systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;

RUN mkdir /data/
#         /data/rtc        \
#         /data/hwclock    \
#         /data/migrations \
#         /data/images


RUN yum install -y less \
                kmod \
                nano \
                net-tools \
#               ifupdown \
#               iputils-ping \
                i2c-tools \
                usbutils \
#               build-essential \
          && yum clean all

######################################################
#   Enable systemd init system in the container
######################################################

ENV INITSYSTEM on
#ENV TIMEZONE America/Recife

ENV TZ=America/Recife
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#RUN yum install -y https://repo.ius.io/ius-release-el8.rpm
#RUN yum update

RUN dnf install -y  python3

RUN yum install -y openssl-devel \
                dnsmasq \
#               wireless-tools \
#               libdbus-glib-1-devel \
#               libcairo2-devel \
        && yum clean all

######################################################
#   Adding user and changing current directory
######################################################

RUN adduser hmv
WORKDIR /home/hmv

######################################################
#   pip install python deps from requirements.txt
#   For caching until requirements.txt changes
######################################################

COPY requirements.txt requirements.txt

RUN python3 -m venv venv
RUN venv/bin/pip install -r requirements.txt

######################################################
#   Copy source code into a container directory
######################################################

COPY app app
COPY migrations migrations
COPY app.db project.py config.py start.sh .env ./
RUN chmod +x start.sh

######################################################
#   Environment Variables
######################################################

ENV FLASK_APP project.py
ENV FLASK_DEBUG 0

RUN chown -R hmv:hmv ./
USER hmv

######################################################
#   run python script when container lands on device
######################################################

ENTRYPOINT ["bash", "./start.sh"]

