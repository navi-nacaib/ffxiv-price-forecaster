import json
from forecast.neuralprophet_forecast import generate_forecast
from forecast.data_processing import fetch_data


def lambda_handler(event, context):
    try:
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
