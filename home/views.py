from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Contact

def index(request):
    return render(request, 'index.html')
def about(request):  
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def team(request):
    return render(request, 'team.html')

def contact_form_submission(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to database
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        # Send email
        send_mail(
            subject=f"New Contact Form Submission: {subject}",
            message=f"Name: {name}\nEmail: {email}\nMessage: {message}",
            from_email='your_email@example.com',
            recipient_list=['heyprshnt@gmail.com'],
            fail_silently=False,
        )

        return HttpResponse('Form submitted successfully!')

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        return redirect('/')

    return render(request, 'index.html')