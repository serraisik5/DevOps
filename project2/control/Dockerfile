FROM python:3.8-slim

RUN apt-get update && apt-get install -y ssh-client
RUN pip install ansible

# Setup SSH keys and permissions
COPY ../ssh_keys/ansible /root/.ssh/id_rsa
COPY ../ssh_keys/ansible.pub /root/.ssh/id_rsa.pub
RUN chmod 600 /root/.ssh/id_rsa && chmod 644 /root/.ssh/id_rsa.pub


CMD ["/bin/bash"]

