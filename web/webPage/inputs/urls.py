from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('inputs/', views.inputs_list),
    path('inputscreate/', csrf_exempt(views.createInput), name='createInput'),
]