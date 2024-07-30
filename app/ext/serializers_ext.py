"""
@brief          Serializers for extended Device models.

@file           api/ext/serializers_ext.py
@author         Dawid Sobczak
@created_at     
@updated_at     30.06.2023
"""

# Imports ============================================================================================================ #
from rest_framework import serializers

# import your models here ------------------------------------------------------------------------ #
# from .models_ext import Measurement


# Create serializers here ============================================================================================ #
# (?)EXAMPLE Class model serializer -------------------------------------------------------------- #
"""
class MeasurementSerializer(serializers.HyperlinkedModelSerializer):

    # Meta --------------------------------------------------------------------------------------- #    
    class Meta:
        model = Measurement
        fields = '__all__'

    # Update ------------------------------------------------------------------------------------- #
    def update(self, instance, validated_data):
        instance.temp = validated_data.get('temp', instance.temp)

        instance.save()
        return instance
"""    

"""
# Configuration Class Serializer ================================================================= #
class ConfigurationSerializer(serializers.HyperlinkedModelSerializer):

    # Meta --------------------------------------------------------------------------------------- #
    class Meta:
        model = Configuration
        fields = '__all__'

    # Update ------------------------------------------------------------------------------------- #
    def update(self, instance, validated_data):
        instance.L = validated_data.get('L', instance.L)

        instance.save()
        return instance
""" 
    