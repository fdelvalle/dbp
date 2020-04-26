# dbp

#DEV Install:

Python 3.8

sudo yum install gcc openssl-devel bzip2-devel libffi-devel

cd /opt
sudo wget https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz

sudo tar xzf Python-3.8.2.tgz

cd Python-3.8.2

sudo ./configure --enable-optimizations
sudo make altinstall

sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev

# Docker

docker-compose up
####### Open server 0.0.0.0:8000

#### In Terminal
docker exec -t -i dbp_web_1  bash

#### In bash mode
./manage makemigrations
./manage migrate
./manager createsuperuser


####### Admin Url 0.0.0.0:8000/admin
####### API root 0.0.0.0:8000/api/v1/



