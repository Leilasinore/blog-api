from django.shortcuts import get_object_or_404
from django.http import HttpResponse
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import BlogPost,Category
from .serializers import BlogpostSerializer



@api_view(['GET', 'POST'])
def articles(request):
    if request.method == 'GET':
        queryset = BlogPost.objects.select_related('category').all()
        serializer = BlogpostSerializer(queryset,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        #steps 
        #deserialize the data
        #validate the data
        #save the data
        serializer = BlogpostSerializer(data=request.data)
        #do data validation
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # serializer.validated_data
        #the restful convention is to return the created object and a status code of 201
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
        

@api_view(['GET','PUT','PATCH','DELETE'])
def myarticle(request,id):
    article = get_object_or_404(BlogPost,pk=id)
    # try:
    #     article = BlogPost.objects.get(pk=id)
    #     serializer = BlogpostSerializer(article)
    #     return Response(serializer.data)
    # except BlogPost.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BlogpostSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        #steps 
        #deserialize the data
        #validate the data
        #save the data
        serializer = BlogpostSerializer(article,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
