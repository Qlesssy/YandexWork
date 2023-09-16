import configuration
import requests
import data

def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

def get_information_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_INFORMATION_ORDER_PATH + str(track_number))