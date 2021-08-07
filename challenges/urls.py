from django.urls import path
from . import views

# 1) Inside the list 'urlpatterns', we list all the URLs we want to support in our app, and then the VIEW ...
# ...Function that should be triggered when a request reaches the URL

urlpatterns = [
    # 2) If a client request reaches <main app name (challenges)>/january URL, execute views.index function response
    path('', views.monthly_challenge_list),
    path('<int:month>', views.monthly_challenge_by_number),
    path('<str:month>', views.monthly_challenge, name="month-challenge"),


]
