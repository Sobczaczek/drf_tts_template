from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from django.contrib.auth.models import User, Group

from .models import Device
from .serializers import DeviceSerializer, UserSerializer

# Create your views here.



# DEVICE VIEW CLASS ================================================================================================== #
class LocalDeviceSet(viewsets.ModelViewSet):
    '''
    API endpoint for `Devices` to be viewed and edited.
    '''
    queryset=Device.objects.all()
    serializer_class=DeviceSerializer
    #permission_classes=[permissions.IsAuthenticated]

    # TODO POST override ------------------------------------------------------------------------- #
    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     return super().perform_create(serializer)

    # TODO GET ALL override ---------------------------------------------------------------------- #
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    # TODO GET override -------------------------------------------------------------------------- #
    # def retrieve(self, request, *args, **kwargs):
    #     return super().retrieve(request, *args, **kwargs)

    # TODO PUT override -------------------------------------------------------------------------- #
    # def update(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)

    # TODO PATCH override ------------------------------------------------------------------------ #
    # def partial_update(self, request, *args, **kwargs):
    #     return super().partial_update(request, *args, **kwargs)

    # TODO DELETE override ----------------------------------------------------------------------- #
    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)

    # TODO QUERY with user filter ---------------------------------------------------------------- #
    def get_queryset(self):
        return super().get_queryset()


# USER VIEW CLASS ==================================================================================================== # 
class UserViewSet(viewsets.ModelViewSet):
    '''
    API endpoint for `Users` to be viewed and edited.
    '''
    queryset=User.objects.all().order_by('-date_joined')
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAdminUser]
