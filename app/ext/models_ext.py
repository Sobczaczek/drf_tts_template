"""
@brief          Models for extended Device fields.

@file           api/ext/models_ext.py
@author         Dawid Sobczak
@created_at     
@updated_at     30.06.2023
"""

# Imports ============================================================================================================ #
from django.db import models
from app.models import Device
from django_auto_one_to_one import AutoOneToOneModel


# Create custom models here ========================================================================================== #
# (?) EXAMPLE class model definiton -------------------------------------------------------------- #
"""
class Measurement(AutoOneToOneModel(Device)):

    temp = models.CharField(
        max_length = 8,
        default = "-",
        verbose_name = "Air temperature"
        )
    
    updated_at = models.DateTimeField(
        auto_now = True,
        verbose_name = "Updated at"
    ) 
"""

"""    
class Configuration(AutoOneToOneModel(Device)):
    # sub-class fields
    L = models.CharField(
        max_length = 8,
        default = "-",
        verbose_name = "Min Moisture"
        )
    
    updated_at = models.DateTimeField(
        auto_now = True,
        verbose_name = "Updated at"
    ) 
"""    