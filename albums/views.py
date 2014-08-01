from django.shortcuts import render
from .models import Album
# Create your views here.
from rest_framework import viewsets

class AlbumViewSet(viewsets.ModelViewSet):
	model = Album