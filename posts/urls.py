from django.urls import path
from . import views
urlpatterns = [
    path("articles/",views.Articles.as_view()),
    path("articles/<int:id>/",views.myarticle,name="myarticle")
]