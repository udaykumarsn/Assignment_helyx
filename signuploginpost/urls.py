from django.conf.urls import url
from rest_framework.authtoken import views
from .views import *

urlpatterns = [
    url(r'^signup/$', registration),
    url(r'^login/$', login_user),
    url(r'logout/$', logout_user),
    url(r'resetpassword/$', reset_password)
]
