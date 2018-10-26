from django.shortcuts import render, get_object_or_404
from .models import Job
from .models import Blog

# Create your views here.
def deb(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/home.html')

def blog(request):
    blogs = Blog.objects
    return render(request, 'jobs/blog.html', {'blogs': blogs})
