from django.urls import path, include
from api.views import *

urlpatterns = [
    path('', apiOverview, name = 'apiOverview'),
    path('memes/', Memes, name = 'Memes'),
    path('memes/<int:pk>', oneMeme, name = 'oneMeme'),
]