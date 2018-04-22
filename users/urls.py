from django.conf.urls import url
from .views import  register
from .views import  edit

urlpatterns = [
    url(r'^register',register,name='register'),
    url(r'^edit/(?P<pk>\d)',edit,name='edit'),
]