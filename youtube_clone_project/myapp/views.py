from django.shortcuts import render
from .serializers import ReplySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from models import Reply

# Create your views here.
