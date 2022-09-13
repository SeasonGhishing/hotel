import os

from django.db import models


def upload_path(instance, filename):
    return os.path.join(
        instance.__class__.__name__, str(instance.created_at.microsecond), filename
    )


class TimeStampAbstractModel(models.Model):
    """Inherit from this class to add timestamp fields in the model class"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
