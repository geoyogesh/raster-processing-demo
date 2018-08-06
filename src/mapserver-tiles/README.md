docker build -t mapserver-docker .

docker run --rm -it -p 8000:80 -v "C:/Work/Github/temp/raster-processing-demo/src/mapserver-tiles/mapfiles:/usr/src/mapfiles" mapserver-docker

docker run -v "C:/Work/Github/temp/raster-processing-demo/src/mapserver-tiles/mapfiles:/map" -p "5000:5000" thingswise/mapserver:latest


http://localhost:5000/fcgi-bin/mapserv?map=/map/mapfile.map
http://localhost:5000/fcgi-bin/mapserv?map=/map/mapfile.map&mode=map

msLoadMap(): Premature End-of-File. msyylex(): Unable to access file. Error opening included file "aws_credentials.inc.map".

