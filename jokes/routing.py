from django.urls import path
from .consumer import JokesConsumer

ws_urlpatterns = [
    path('ws/jokes/', JokesConsumer.as_asgi())
]