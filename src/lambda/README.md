docker build --rm -t centos .
 docker build --rm -t centos . --no-cache


docker stop centos
docker rm centos
docker run -d -p 2222:22 centos -e AWS_ACCESS_KEY_ID=xyz -e AWS_SECRET_ACCESS_KEY=aaa

ssh -p 2222 user@localhost

newpass

docker cp centos:/lambda/src/bundle.zip "C:/temp/bundle.zip"



aws s3 cp bundle.zip s3://yogi-lambda-deployment/bundle.zip

aws lambda update-function-code --function-name test-yogi  --s3-bucket yogi-lambda-deployment --s3-key bundle.zip
--------------------------
aws lambda update-function-code --function-name test-yogi --zip-file fileb://bundle.zip
-------------------------
docker exec --rm geoyogesh/rasterio-lambda 'WORKDIR "/lambda/src"'

