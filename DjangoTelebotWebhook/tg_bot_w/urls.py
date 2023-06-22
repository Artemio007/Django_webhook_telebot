from tg_bot_w.views import UpdateBot
from django.urls import path

urlpatterns = [
    path('', UpdateBot.as_view(), name='update'),
]