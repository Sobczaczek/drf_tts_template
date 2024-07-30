"""
@brief          Views for extended Device models.

@file           api/ext/views_ext.py
@author         Dawid Sobczak
@created_at     
@updated_at     30.06.2023
"""

# Imports ============================================================================================================ #
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions

from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle 

from django.contrib.auth.models import User, Group

# import your models and serializers here -------------------------------------------------------- #
# from .models_ext import Measurement
# from .serializers_ext import MeasurementSerializer


# Create views here ================================================================================================== #
# (?) EXAMPLE View ------------------------------------------------------------------------------- #
"""
class MeasurementViewSet(viewsets.ModelViewSet):

    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]
"""

    