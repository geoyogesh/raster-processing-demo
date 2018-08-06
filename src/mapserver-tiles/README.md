docker build -t mapserver-docker .

docker run --rm -it -p 8000:80 -v C:/Work/Github/temp/raster-processing-demo/src/mapserver-tiles/mapfiles:/usr/src/mapfiles mapserver-docker