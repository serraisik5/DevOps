FROM python:3.8-slim

RUN apt-get update && apt-get install -y openssh-server sudo
RUN mkdir /var/run/sshd

COPY ../ssh_keys/ansible.pub /root/.ssh/authorized_keys
RUN chmod 600 /root/.ssh/authorized_keys

EXPOSE 80

CMD /usr/sbin/sshd -D & /bin/bash
