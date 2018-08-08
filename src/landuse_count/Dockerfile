FROM geoyogesh/rasterio-lambda
MAINTAINER Yogesh Dhanapal "geoyogesh@gmail.com"

WORKDIR "/lambda/src"
COPY lambda_count.py lambda_count.py
RUN zip -r9 bundle.zip lambda_count.py
ENV PATH=~/.local/bin:$PATH
WORKDIR /lambda/src
#CMD ["bash","aws s3 cp lambda/src/bundle.zip s3://yogi-lambda-deployment/bundle.zip", "aws lambda update-function-code --function-name test-yogi  --s3-bucket yogi-lambda-deployment --s3-key bundle.zip"]



