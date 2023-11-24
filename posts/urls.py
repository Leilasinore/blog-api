from django.urls import path
from . import views
urlpatterns = [
    path("articles/",views.Articles.as_view(),name="Articles"),
    path("articles/<int:id>/",views.MyArticle.as_view(),name="MyArticle")
]