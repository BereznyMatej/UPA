#!/bin/bash

[[ -d "schemas" ]] || mkdir "schemas"
[[ -d "data" ]] || mkdir "data"

distro=$(gcc --version | grep 'Ubuntu')


if [ -z "$distro" ]; then
    rm -rf /etc/yum.repos.d/mongodb.repo    
    echo -e "[Mongodb]\nname=MongoDB Repository\nbaseurl=https://repo.mongodb.org/yum/redhat/8/mongodb-org/4.4/x86_64/\ngpgcheck=1\nenabled=1\ngpgkey=https://www.mongodb.org/static/pgp/server-4.4.asc" > tmp.txt
    cp tmp.txt /etc/yum.repos.d/mongodb.repo
    rm -f tmp.txt
    dnf -y install python3-devel openssl-devel zlib-devel bzip2-devel sqlite-devel libffi-devel python3-pip
    dnf install mongodb-org mongodb-org-server
    systemctl enable mongod.service
    systemctl start mongod.service
else
    add-apt-repository ppa:deadsnakes/ppa
    apt update
    apt install python3 python3-pip
    apt-get install gnupg
    wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
    echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
    apt-get install -y mongodb-org
    apt-get install -y mongodb-org=5.0.2 mongodb-org-database=5.0.2 mongodb-org-server=5.0.2 mongodb-org-shell=5.0.2 mongodb-org-mongos=5.0.2 mongodb-org-tools=5.0.2
    systemctl start mongod
fi



[[ -f "requirements.txt" ]] || python3 -m pip install -r requirements.txt
