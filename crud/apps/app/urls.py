from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name = 'index'),
    url(r'^create_pet/', CreatePet.as_view(), name='create_pet'),
    url(r'^show_pet/', ShowPet.as_view(), name='show_pet'),
    url(r'^update_pet/(?P<pk>\d+)/$',UpdatePet.as_view(),name='update_pet'),
    url(r'^delete_pet/(?P<pk>\d+)/$',DeletePet.as_view(),name='delete_pet'),
]