# "ported" by Adam Miller <maxamillion@fedoraproject.org> from
#   https://github.com/fedora-cloud/Fedora-Dockerfiles
#
# Originally written for Fedora-Dockerfiles by
#   scollier <scollier@redhat.com>

FROM centos:centos7
MAINTAINER The CentOS Project <cloud-ops@centos.org>

RUN yum -y update; yum clean all
RUN yum -y install openssh-server passwd; yum clean all
ADD ./start.sh /start.sh
RUN mkdir /var/run/sshd

RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N '' 

RUN chmod 755 /start.sh
# EXPOSE 22
RUN ./start.sh
ENTRYPOINT ["/usr/sbin/sshd", "-D"]

RUN yum -y install python27-devel python27-pip gcc libjpeg-devel zlib-devel gcc-c++
RUN yum -y install wget
RUN yum -y install make

RUN echo "$PWD"
RUN mkdir /lambda
RUN mkdir /lambda/local
RUN mkdir /lambda/src
WORKDIR "/lambda"
RUN echo "$PWD"


RUN wget https://github.com/OSGeo/proj.4/archive/4.9.2.tar.gz
RUN tar -zvxf 4.9.2.tar.gz
WORKDIR "/lambda/proj.4-4.9.2"
RUN ./configure --prefix=/lambda/local
RUN make
RUN make install
RUN echo "$PWD"

WORKDIR "/lambda"
RUN wget http://download.osgeo.org/gdal/1.11.3/gdal-1.11.3.tar.gz
RUN tar -xzvf gdal-1.11.3.tar.gz
WORKDIR "/lambda/gdal-1.11.3"
RUN ./configure --prefix=/lambda/local \
            --with-geos=/lambda/local/bin/geos-config \
            --with-static-proj4=/lambda/local
RUN make
RUN make install
RUN echo "$PWD"

WORKDIR "/lambda/src"
RUN yum install -y python-setuptools
RUN easy_install pip
RUN pip install -U virtualenv
RUN python -m virtualenv venv
RUN virtualenv env
RUN source env/bin/activate
RUN export GDAL_CONFIG=/lambda/local/bin/gdal-config
RUN pip install rasterio
