from django.urls import path

from . import views


app_name = 'poll'
urlpatterns = [
    #http://127.0.0.1:8000/poll/
    path('', views.home, name='home'),
    #http://127.0.0.1:8000/poll/1/vote
    path('<int:q_id>/vote/', views.vote, name='vote'),
    #http://127.0.0.1:8000/poll/1/result
    path('<int:q_id>/result/', views.result, name='result')
]