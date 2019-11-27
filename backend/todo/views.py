from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Todo_Serializer
from .models import Todo

class Todo_View(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = Todo_Serializer