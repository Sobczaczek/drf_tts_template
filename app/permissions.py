# permissions.py

from rest_framework import permissions

class IsAdminOrTeamLeader(permissions.BasePermission):
    """
    Custom permission to only allow team leaders or admins to create users within a team.
    """

    def has_permission(self, request, view):
        # Admins can do anything
        if request.user and request.user.is_staff:
            return True
        # Only team leaders can create users
        if view.action == 'create':
            return request.user.is_team_leader
        return True

class IsTeamMember(permissions.BasePermission):
    """
    Custom permission to only allow members of a team to access it.
    """

    def has_object_permission(self, request, view, obj):
        # Admins can access anything
        if request.user and request.user.is_staff:
            return True
        # Team members can access their team
        return obj.users.filter(id=request.user.id).exists()
