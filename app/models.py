from django.db import models
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404

# TODO validators
# from .validators import DeviceIdValidator, DeviceEuiValidator
from django.core.validators import RegexValidator


# Create your models here.

# DEVICE MODEL CLASS ================================================================================================= #
class Device(models.Model):

    # fields ------------------------------------------------------------------------------------- #
    device_id=models.CharField(
        max_length=36,
        unique=True,
        validators=[RegexValidator(
            regex='^[a-z0-9](?:[-]?[a-z0-9]){2,}$'
        )]
    )
    dev_eui=models.CharField(
        max_length=16, 
        unique=True
    )
    added_by=models.ForeignKey(
        'auth.User',
        related_name="devices",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    group_owner=models.ForeignKey(
        Group,
        related_name="devices",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    added_at=models.DateTimeField(
        auto_now=True
    )
    updated_at=models.DateTimeField(
        auto_now=True
    )

    # methods ------------------------------------------------------------------------------------ #
    def save(self, *args, **kwargs):
        device_id=self.device_id and {'device_id': self.device_id}
        dev_eui=self.dev_eui and {'dev_eui': self.dev_eui}

        super().save(*args, **kwargs)

    
    def get_object(self):
        obj=get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
    
    # meta --------------------------------------------------------------------------------------- #
    class Meta:
        app_label = 'app'