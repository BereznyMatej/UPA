#/bin/bash

[[ -d "schemas" ]] || mkdir "schemas"
[[ -d "data" ]] || mkdir "data"

distro=$(gcc --version | grep 'Ubuntu')


if [ -z "$distro"]; then
    yum -y install python3-devel openssl-devel zlib-devel bzip2-devel sqlite-devel libffi-devel python3-pip
else
    add-apt-repository ppa:deadsnakes/ppa
    apt update
    apt install python3 python3-pip
fi

[[ -f "requirements.txt" ]] || python3 -m pip install -r requirements.txt
