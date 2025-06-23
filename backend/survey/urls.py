from django.urls import path
from . import views

urlpatterns = [
    path('survey/submit/', views.submit_survey, name='submit_survey'),
    path('survey/stats/', views.survey_stats, name='survey_stats'),
    path('health/', views.health_check, name='health_check'),
]
