from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Task
"""
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from tasks.models import Task
from tasks.serializers import Taskserializer
from rest_framework import status
#from django.views.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView


class BlogList(APIView):

    def get(self, request, format=None):
        snippets = Task.objects.all()
        serializer = Taskserializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Taskserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return self.retrieve(request)

    def put(self, request):
        return self.update(request)

    def delete(self, request):
        return self.destroy(request)



"""


# Create your views here.
class HomeView(ListView):
    model = Task
    template_name = "pages/home.html"