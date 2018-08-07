docker build --rm -t centos .
 docker build --rm -t centos . --no-cache


docker stop centos
docker rm centos
docker run -d -p 2222:22 centos

ssh -p 2222 user@localhost

newpass

