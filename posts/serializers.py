from rest_framework import serializers
from .models import Category

class BlogpostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length = 255)
    body = serializers.CharField(max_length=500)
    # category = serializers.PrimaryKeyRelatedField(
    #     queryset=Category.objects.all()
    # )

#now that we have this serializer we will use it to convert a post object to a python dictionary 
