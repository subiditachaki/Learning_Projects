# from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
	"""
	API end point that allows users to be viewed or edited
	"""

	queryset = User.Objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	"""
	API end point that allows groups to be viewed or edited
	"""

	queryset = Groups.objects.all()
	serializer_class = GroupSerializer

# Create your views here.
