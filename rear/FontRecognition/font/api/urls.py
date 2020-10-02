from django.urls import path
from . import views
app_name = 'font'

urlpatterns = [
    path('result/', views.get_recognition_result)
]