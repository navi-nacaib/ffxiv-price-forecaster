import json
import os
from forecast.neuralprophet_forecast import generate_forecast
from forecast.data_processing import fetch_data


def lambda_handler(event, context):
    try:
        # Set the working directory to `/tmp` to redirect any writes there
        # Uncomment when deploying
        os.chdir("/tmp")

        # Fetch data from Universalis API
        data = fetch_data()

        # Generate forecast
        forecast = generate_forecast(data)

        # Return the forecast as JSON
        return {
            'statusCode': 200,
            'body': json.dumps(forecast)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
