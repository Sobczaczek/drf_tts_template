from rest_framework import serializers

from django.contrib.auth.models import User, Group
from drf_writable_nested import WritableNestedModelSerializer

from app.models import Device, Team, CustomUser


# DEVICE CLASS SERIALIZER ============================================================================================ # 
class DeviceSerializer(WritableNestedModelSerializer, serializers.HyperlinkedModelSerializer):
    # Meta --------------------------------------------------------------------------------------- #
    class Meta:
        model = Device
        owner = serializers.ReadOnlyField(source='owner.username')
        
        fields = (
            'device_id', 'dev_eui', 'url', 'added_by', 'team_owner', 'added_at', 'updated_at',)\
            #+ tuple(fields_ext)


    # Initialization ----------------------------------------------------------------------------- #
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

        # for extra_field in fields_ext:
        #     self.fields[extra_field] = globals()[f'{extra_field.capitalize()}Serializer']()


    # Get ---------------------------------------------------------------------------------------- #
    def get_object(self, instance):
        return instance
    
    # Update ------------------------------------------------------------------------------------- #
    def update(self, instance, validated_data):
        
        # for extra_field in fields_ext:
        #     if extra_field in validated_data:
        #         nested_serializer = self.fields[extra_field]
        #         nested_instance = getattr(instance, extra_field)
        #         nested_data = validated_data.pop(extra_field)

        #         nested_serializer.update(nested_instance, nested_data)

        instance.save()
        return instance
    

# USER CLASS SERIALIZER ============================================================================================== #
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Meta --------------------------------------------------------------------------------------- #
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


# class TeamSerializer(serializers.HyperlinkedModelSerializer):
#     # Meta --------------------------------------------------------------------------------------- #
#     class Meta:
#         model = Team
#         fields = ['url', 'name', 'team_id', 'users', 'leaders']


class CustomUserSerializer(serializers.ModelSerializer):
    team_id = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'team', 'team_id', 'is_team_leader', 'password']
        read_only_fields = ['team']

    def create(self, validated_data):
        team_id = validated_data.pop('team_id')
        password = validated_data.pop('password')
        team = Team.objects.get(team_id=team_id)
        user = CustomUser(**validated_data)
        user.team = team
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        team_id = validated_data.pop('team_id', None)
        password = validated_data.pop('password', None)
        
        if team_id:
            team = Team.objects.get(team_id=team_id)
            instance.team = team

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)
            
        instance.save()
        return instance

class TeamSerializer(serializers.ModelSerializer):
    users = CustomUserSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['team_id', 'name', 'users']