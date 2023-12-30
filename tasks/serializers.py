from rest_framework import serializers
from .models import Task, TaskImage

class Taskserializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields =('__all__')

class Taskimageserializer(serializers.ModelSerializer):
    class Meta:
        model= TaskImage
        fields =('__all__')