## Prerequisites
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

        npm install -g serverless-
        serverless plugin install -n serverless-python-requirements

## Step 3: Run the Project Locally with Serverless Offline

1) __Start the Local Serverless Environment:__ Run the following command to start the Serverless Offline plugin, which will create a local endpoint that simulates API Gateway.

        serverless offline

2) __Access the Local Endpoint:__ 

    - After starting the offline server, you should see a local endpoint, typically running at ```http://localhost:3000```
    - Access the endpoint in your browser or via a tool like ```curl``` or ```Postman``` to test the /forecast route.
           ```curl http://localhost:3000/forecast```