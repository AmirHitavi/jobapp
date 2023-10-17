from django.urls import path
from app import views

app_name = "app"
subscribe_name = "subscribe"


urlpatterns = [
    path("", views.job_list, name="job-list"),
    path("job/<slug:slug>", views.job_detail, name="job-detail"),
]
