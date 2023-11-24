from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,DestroyModelMixin,ListModelMixin,RetrieveModelMixin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import BlogPost,Category
from .serializers import BlogpostSerializer



#implementation of views using GenericAPIView class and mixins
class Articles(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = BlogPost.objects.select_related('category').all()
    serializer = BlogpostSerializer(queryset,many=True)
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)



class MyArticle(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    article = get_object_or_404(BlogPost,pk=id)
    serializer = BlogpostSerializer(article)
    def get(self,request ,*args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)
    
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)
    








#implementation of views using APIView class
# class Articles(APIView):
#     def get(self,request):
#         queryset = BlogPost.objects.select_related('category').all()
#         serializer = BlogpostSerializer(queryset,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         #steps 
#         #deserialize the data
#         #validate the data
#         #save the data
#         serializer = BlogpostSerializer(data=request.data)
#         #do data validation
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # serializer.validated_data
#         #the restful convention is to return the created object and a status code of 201
#         return Response(serializer.data,status=status.HTTP_201_CREATED)

# class MyArticle(APIView):
#     def get(self,request,id):
#         article = get_object_or_404(BlogPost,pk=id)
#         serializer = BlogpostSerializer(article)
#         return Response(serializer.data)
    
#     def put(self,request,id):
#         article = get_object_or_404(BlogPost,pk=id)
#         serializer = BlogpostSerializer(article,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
        




#implementation of views using function based views
# @api_view(['GET', 'POST'])
# def articles(request):
#     if request.method == 'GET':
#         queryset = BlogPost.objects.select_related('category').all()
#         serializer = BlogpostSerializer(queryset,many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         #steps 
#         #deserialize the data
#         #validate the data
#         #save the data
#         serializer = BlogpostSerializer(data=request.data)
#         #do data validation
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # serializer.validated_data
#         #the restful convention is to return the created object and a status code of 201
#         return Response(serializer.data,status=status.HTTP_201_CREATED)

    
        

# @api_view(['GET','PUT','PATCH','DELETE'])
# def myarticle(request,id):
#     article = get_object_or_404(BlogPost,pk=id)
#     # try:
#     #     article = BlogPost.objects.get(pk=id)
#     #     serializer = BlogpostSerializer(article)
#     #     return Response(serializer.data)
#     # except BlogPost.DoesNotExist:
#     #     return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = BlogpostSerializer(article)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         #steps 
#         #deserialize the data
#         #validate the data
#         #save the data
#         serializer = BlogpostSerializer(article,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
