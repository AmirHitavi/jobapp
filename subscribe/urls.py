from django.urls import path
from subscribe import views

app_name = "subscribe"

urlpatterns = [
    path("subscribe/", views.subscribe, name="subscribe"),
    path("thanks/", views.thanks, name="thanks")
]
