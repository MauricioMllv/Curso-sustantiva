from django.urls import path
from . import views

urlpatterns = [
     # ex: /practica/
    path('', views.index, name='index'),
    # ex: /practica/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /practica/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /pratica/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]