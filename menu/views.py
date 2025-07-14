from django.shortcuts import render
from rest_framework import viewsets
from .models import MenuSection, MenuItem
from .serializers import MenuSectionSerializer, MenuItemSerializer

class MenuSectionViewSet(viewsets.ModelViewSet):
    queryset = MenuSection.objects.all()
    serializer_class = MenuSectionSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
