import pandas as pd
from neuralprophet import NeuralProphet
from src.utils.helpers import convert_epoch_to_datetime


def generate_forecast(data):
    # Prepare data for NeuralProphet
    df = pd.DataFrame(data)
    df['ds'] = pd.to_datetime(df['timestamp'], unit='s')
    df['y'] = df['pricePerUnit']

    # Calculate a weighted average price per timestamp
    df['weighted_price'] = df['pricePerUnit'] * df['quantity']
    df = df.groupby('ds').apply(
        lambda x: pd.Series({
            'y': x['weighted_price'].sum() / x['quantity'].sum(),  # Weighted average
            'quantity': x['quantity'].sum()  # Total quantity
        })
    ).reset_index()

    # Initialize and fit NeuralProphet model
    model = NeuralProphet()
    model.fit(df[['ds', 'y']], freq="D")

    # Create future dataframe and predict
    future = model.make_future_dataframe(df[['ds', 'y']], periods=7)
    forecast = model.predict(future)

    # Convert `ds` column to string format using the helper function
    forecast['ds'] = forecast['ds'].apply(lambda x: convert_epoch_to_datetime(x.timestamp()))

    return forecast[['ds', 'yhat1']].tail(7).to_dict(orient='records')
