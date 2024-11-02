:: Authenticate Docker to your ECR
aws ecr get-login-password --region us-west-1 | docker login --username AWS --password-stdin 218821328974.dkr.ecr.us-west-1.amazonaws.com

:: Build the Docker image
docker build -t serverless-ffxiv-price-forecaster .

:: Tag the Docker image
docker tag serverless-ffxiv-price-forecaster:latest 218821328974.dkr.ecr.us-west-1.amazonaws.com/serverless-ffxiv-price-forecaster:latest

:: Push the Docker image to ECR
docker push 218821328974.dkr.ecr.us-west-1.amazonaws.com/serverless-ffxiv-price-forecaster:latest
