from django.shortcuts import get_object_or_404
from django.http import HttpResponse
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import BlogPost
from .serializers import BlogpostSerializer


@api_view()
def articles(request):
    queryset = BlogPost.objects.all()
    serializer = BlogpostSerializer(queryset,many=True)
    return Response(serializer.data)

@api_view()
def myarticle(request,id):
    # try:
    #     article = BlogPost.objects.get(pk=id)
    #     serializer = BlogpostSerializer(article)
    #     return Response(serializer.data)
    # except BlogPost.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    article = get_object_or_404(BlogPost,pk=id)
    serializer = BlogpostSerializer(article)
    return Response(serializer.data)