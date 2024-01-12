import requests
from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer


 
#this is a asynchronous function that we have to call in below sync function
#for that we have to make this sync function using async to sync conversion
channel_layer = get_channel_layer()  

@shared_task
def get_joke():
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url).json()
    joke = response['value']
    print(joke)
    async_to_sync(channel_layer.group_send)('jokes', {'type': 'send_jokes', 'text': joke})
    
    # print('Hello Sineeth Kumar')
    # return joke