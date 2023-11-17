from django.urls import path
from . import views
urlpatterns = [
    path("articles/",views.articles,name="articles"),
    path("articles/<int:id>/",views.myarticle,name="myarticle")
]