from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate
from django.contrib.auth import login
from rest_framework.response import Response
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.template.response import TemplateResponse
# Create your views here.
from django.core.mail import EmailMessage, send_mail
from django.template.loader import get_template
from rest_framework.decorators import api_view



def registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        getmail=request.POST['email']
        User.objects.create_user(first_name=request.POST['first_name'], last_name="",
                                        password=request.POST['password'],
                                        username=request.POST['email'],
                                        email=request.POST['email'],
                                        is_active=True)
        obj=Registration()
        obj.name=request.POST['first_name']
        obj.email_id=request.POST['email']
        obj.save()
        send_mail(
            'Registration confirmation',
            get_template('email_template.html').render(
                dict({
                    'Username': first_name
                })
            ),

            'test.udaykumar@gmail.com',
            [getmail],
            fail_silently=False,
        )

        return render(request, 'signup.html')
    return render(request, 'signup.html')


def login_user(request):
    user_details = authenticate(username=request.POST['username'],
                   password=request.POST['password']
                   )
    if user_details is not None:
        login(request, user_details)
        return render(request, 'loginlandingpage.html')
    else:
        return render(request, "signup.html")


@login_required
def logout_user(request):
    logout(request)
    return render(request, 'signup.html')


@login_required
@api_view(['POST'])
def reset_password(request):
   print('************************',request.user)
   a=User.objects.get(username=request.user)
   a.set_password(request.data['pwd1'])
   a.save()
   return  render_to_response('signup.html')