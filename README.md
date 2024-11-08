# Price forecaster for Final Fantasy XIV

At a high level, this project is a serverless forecasting application for predicting item prices in Final Fantasy 
XIV (FFXIV).

1) Data Collection: The application regularly pulls the latest item sale data from Universalis, a third-party API that aggregates FFXIV marketplace data. This data includes item prices, quantities sold, and timestamps of transactions.


2) Data Processing & Forecasting: Using Python and the NeuralProphet forecasting library, the application processes 
   this historical market data to create predictive models. The current focus is on forecasting prices over the next 
   week


3) Serverless Architecture: To ensure scalability and cost-efficiency, the project is built as a serverless 
   application using AWS Lambda. This setup includes a Dockerized Python environment deployed as a Lambda container 
   image, with the flexibility to run complex computations without the limitations of a standard Lambda function 


4) User Access: The Lambda function is triggered through HTTP requests, allowing users to get real-time forecasts by 
   querying the Lambda function endpoint.

This project leverages AWS services and automated CI/CD with GitHub actions to streamline deployment. Upon each push to the main branch, the workflow:
- Checks out the code.
- Builds and pushes the Docker image to ECR.
- Deploys the updated Lambda function using the Serverless Framework.

## Prerequisites for local testing
1) __Install the Serverless Framework:__

        npm install -g serverless

2) __Install Docker:__ Docker Desktop is needed for simulating AWS Lambda functions locally with the Serverless Framework.

## Step 1: Set Up the Project for Local Testing

1) __Navigate to the project directory:__

        cd ffxiv-price-forecaster

2) __Install Python Dependencies Locally:__ The Serverless Framework with serverless-python-requirements plugin uses Docker to handle dependencies, but installing them locally allows you to run and debug easily outside Docker.

        pip install -r requirements.txt

## Step 2: Configure the Serverless Framework for Local Development

1) __Add the Serverless Offline Plugin:__ Install the plugin to simulate API Gateway locally.

         npm install serverless-offline --save-dev 
         serverless plugin install -n serverless-python-requirements

## Step 3: Run the Project Locally with Serverless Offline

1) __Start the Local Serverless Environment:__ Run the following command to start the Serverless Offline plugin, which will create a local endpoint that simulates API Gateway.

        serverless offline --config serverless-local.yml

2) __Access the Local Endpoint:__ 

    - After starting the offline server, you should see a local endpoint, typically running at ```http://localhost:3000```
    - Access the endpoint in your browser or via a tool like ```curl``` or ```Postman``` to test the /forecast route.
           ```curl http://localhost:3000/forecast```