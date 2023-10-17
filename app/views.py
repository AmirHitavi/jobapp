from django.shortcuts import render
from app.models import JobPost

# Create your views here.


def job_list(request):
    jobs = JobPost.objects.all()
    return render(request, "app/home_page.html", {"jobs": jobs})


def job_detail(request, slug):
    job = JobPost.objects.get(slug=slug)
    return render(request, "app/job_detail.html", {"job": job})
