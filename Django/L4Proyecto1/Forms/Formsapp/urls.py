from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/<int:question_id>/', views.detail, name='detail'),
    path('question/<int:question_id>/results/', views.results, name='results'),
    path('question/<int:question_id>/vote/', views.vote, name='vote'),
    path('question/', views.question, name='question'),
    path('success/', views.success, name='success'),
    path('back-to-home/', views.back_to_home, name='back_to_home'),
]
    