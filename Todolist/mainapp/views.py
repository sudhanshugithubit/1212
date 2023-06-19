from django.shortcuts import render
from rest_framework import  generics
from  .serializers import *
from  .models import *


# Create your views here.
#CRUD Operations by  


class ListToDo(generics.ListAPIView):      #Read
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DetailTodo(generics.RetrieveUpdateAPIView):  #update
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class CreateTodo(generics.CreateAPIView):     #create 
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DeleteTodo(generics.DestroyAPIView):    #Delete
    queryset = ToDo.objects.all() 
    serializer_class = ToDoSerializer



     
