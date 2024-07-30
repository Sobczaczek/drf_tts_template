from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsAdminOrTeamLeader, IsTeamMember

from django.contrib.auth.models import User

from .models import Device, Team, CustomUser
from rest_framework.exceptions import PermissionDenied
from .serializers import DeviceSerializer, UserSerializer, TeamSerializer, CustomUserSerializer

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
# class UserViewSet(viewsets.ModelViewSet):
#     '''
#     API endpoint for `Users` to be viewed and edited.
#     '''
#     queryset=User.objects.all().order_by('-date_joined')
#     serializer_class=UserSerializer
#     permission_classes=[permissions.IsAdminUser]


# class TeamViewSet(viewsets.ModelViewSet):
#     queryset=Team.objects.all()
#     serializer_class=TeamSerializer
#     permission_classes=[permissions.IsAdminUser]

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrTeamLeader]

    def perform_create(self, serializer):
        # Only allow team leaders to add users to their own team
        team_id = serializer.validated_data.get('team_id')
        if not self.request.user.is_staff and not self.request.user.is_team_leader:
            raise PermissionDenied("Only team leaders or admins can add users.")
        
        team = Team.objects.get(team_id=team_id)
        if not self.request.user.is_staff and self.request.user.team != team:
            raise PermissionDenied("You can only add users to your own team.")

        serializer.save(team=team)

    def perform_update(self, serializer):
        serializer.save()


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrTeamLeader, IsTeamMember]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticated, IsTeamMember]
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsAdminOrTeamLeader]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]