import json
from .email_send_otp import send_email_async
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.

from django.contrib.auth.models import User

u = User.objects.get(username='Prem')
u.set_password('idiot_04')
u.save()

def home(request):
    projects = Project.objects.all().prefetch_related('tech_stack', 'screenshots')
    for project in projects:
        print(project.title, project.image)
        
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)

def project_details(request, pk):
    project = Project.objects.get(pk=pk)
    project_tech_stack = project.tech_stack.all()
    project_screenshots = project.screenshots.all()
    print(project.features)
    context = {
        'project': project,
        'tech_stack': project_tech_stack,
        'screenshots': project_screenshots
    }
    return render(request, 'project_details.html', context)

import json
from django.http import JsonResponse

def filter_projects(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        domain = data.get('domain')
        print("DOMAIN:", domain)

        if domain == 'all':
            projects = Project.objects.all()
        elif domain == "web":
            projects = Project.objects.filter(domain="Web Dev")
        elif domain == "Python":
            projects = Project.objects.filter(domain="Python")
        elif domain == "ML":
            projects = Project.objects.filter(domain="ML")
        else:
            projects = Project.objects.all()

        result = []

        for project in projects:
            result.append({
                "id": project.id,
                "title": project.title,
                "short_description": project.short_description,
                "image": project.image.url,
                "github": project.github_link,
                "tech_stack": [tech.name for tech in project.tech_stack.all()]
            })

        return JsonResponse(result, safe=False)

    return JsonResponse({"error": "Invalid request"}, status=400)

def submit_contact_form(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        print(f"Received contact form submission: Email={email}, Subject={subject}, Message={message}" )
        if not email or not subject or not message:
            return JsonResponse({"error": "All fields are required."}, status=400)
        
        # Here you can handle the form data, e.g., save it to the database or send an email
        try:
            send_email_async(subject, message)
            messages.success(request, "Your email has been sent successfully!")
        except Exception as e:
            messages.error(request, "There was an error sending your email. Please try again later.")
            return JsonResponse({"error": "Failed to send email."}, status=500)
            
        return redirect('home')

    return JsonResponse({"error": "Invalid request"}, status=400)
