from django.contrib.auth.models import AbstractUser
from django.db import models

USER_TYPE_CHOICES = (
    ('superuser', 'Superuser'),
    ('admin', 'Admin'),
    ('staff', 'Staff'),
    ('supplier', 'Supplier'),
)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    project = models.ForeignKey('project.Project', on_delete=models.SET_NULL, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # required when creating superuser

    def __str__(self):
        return self.email
