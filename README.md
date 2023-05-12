This directory defines an API endpoint using FastAPI that accepts POST requests to the route "/api/volume_prediction". The endpoint expects two input parameters, vol_moving_avg and adj_close_rolling_med, both of which are floats passed in as form data. The endpoint uses the input features to make a prediction of the trading volume using a pre-trained gradient boosting model which is trained on the stock market dataset. The predicted volume is then returned in a JSON format as the response.

ML model trained on this Dataset: https://www.kaggle.com/datasets/jacksoncrow/stock-market-dataset


Hosted on : http://3.143.219.252:8000/docs#/
