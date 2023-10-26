from django.urls import path
from main import views

urlpatterns = [
    path('project/',views.ProJectView,name='project'),
    path('lan/',views.language,name='lan'),
    path('',views.index,name='index')
    
]
