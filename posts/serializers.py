from rest_framework import serializers
from .models import Category,BlogPost

# class BlogpostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length = 255)
#     body = serializers.CharField(max_length=500)
   
#now that we have this serializer we will use it to convert a post object to a python dictionary 

class BlogpostSerializer(serializers.ModelSerializer):
    class Meta:
        model  = BlogPost
        fields =['title','body','category']
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length = 255)
    # body = serializers.CharField(max_length=500)

    
    # def create(self, validated_data):
    #     blogpost = BlogPost(**validated_data)
    #     blogpost.other = 1
    #     blogpost.save()
    #     return blogpost