from rest_framework import serializers

from django.contrib.auth.models import User, Group
from drf_writable_nested import WritableNestedModelSerializer

from app.models import Device


# DEVICE CLASS SERIALIZER ============================================================================================ # 
class DeviceSerializer(WritableNestedModelSerializer, serializers.HyperlinkedModelSerializer):
    # Meta --------------------------------------------------------------------------------------- #
    class Meta:
        model = Device
        owner = serializers.ReadOnlyField(source='owner.username')
        
        fields = (
            'device_id', 'dev_eui', 'url', 'added_by', 'group_owner', 'added_at', 'updated_at',)\
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