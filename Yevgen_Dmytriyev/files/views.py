from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.utils.translation import gettext as _
from django.core.mail import EmailMessage
from django.conf import settings

def index(request):
    context = {
        'title': _('Home'),
    }
    return render(request, 'main/index.html', context)

def work(request):
    context = {
        'title': _('My work'),
        'content': _("""
        Secure-Zen

        A comprehensive solution for the analysis and detection of malicious files and links,
        available as web, mobile, and desktop applications. The project is aimed at providing
        a high level of security for end-users and organizations.

        Main Components:
        Programming Language: Python.
        Web Framework: Django.
        Frontend: HTML, CSS, JavaScript.
        Application: Development of the server side, application logic, interaction with the database,
        and API integration.
        Databases: PostgreSQL.
        API Integration: For data exchange between client applications and the server.
        Application Versions:
        Web Version: Provides a user interface through a browser. Based on Django and uses HTML, CSS,
        and JavaScript for the frontend.
        Mobile Application: Developed for major mobile platforms (iOS, Android).
        Desktop Application: For Windows, macOS, and Linux.
        """),
    }
    return render(request, 'main/work.html', context)


def contact(request):
    context = {
        'title': _('Contact Information'),
        # 'content': _(
        #     "Address: Potsdam, Germany\n"
        # )
    }
    
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        
        subject = 'New message from user {}, for Yevgen'.format(name)
        message_body = '{} has sent you a new message:\n\nName: {}\nEmail: {}\nMessage:\n{}'.format(name, name, email, message)
        
        try:
            email = EmailMessage(
                subject,
                message_body,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],  # Assuming you want to send the email to yourself
            )
            email.send()
            messages.success(request, _('Thank you! Your message has been sent.'))
        except Exception as e:
            print(f"Error sending email: {e}")
            messages.error(request, _('An error occurred: ') + str(e))
            return redirect('main:contact')
        
        return redirect(reverse('main:contact'))  # Redirect the user to the contact page

    return render(request, 'main/contact.html', context)

def skills(request):
    context = {
        'title': _('My skills'),
        'content': _("""
            Technologies
            HTML
            CSS
            Python
            Object-Oriented Programming (OOP)
            Google Cloud Platform (GCP)
            Amazon Web Services (AWS)
            CI/CD
            REST API

            Databases
            Relational Database Management System (RDBMS)
            SQL & PostgreSQL

            Version Controls
            GitHub

            Frameworks
            Django

            Others
            Agile Development Project Management
        """)
    }
    return render(request, 'main/skills.html', context)

def about(request):
    context = {
        'title': _('About'),
        'content': _("""
            Hello, I'm Yevgen and I am a Python Backend Developer.
        As a Python developer who enjoys tackling technical challenges, 
        I've dedicated the past year to studying hard and honing my skills. 
        I take pride in building things properly and ensuring client satisfaction.
        My goal is to join a tech company where I can apply my knowledge 
        to solve innovative problems. I'm enthusiastic about developing 
        top-notch backend systems, not settling for mediocrity. 
        I'm seeking a position that offers opportunities to work on
        intricate projects, learn from industry experts, and 
        contribute to advancing technology for collective success.
        """)
    }
    return render(request, 'main/about.html', context)

    