from multiprocessing import context
from django.shortcuts import render
from projects.models import Project

# Create your views here.

# The information on the preview of the projects cards on the
# projects landing page
def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

# Detailed(expanded) info view of the preview
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

