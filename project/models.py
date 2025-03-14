from django.db import models
from django.core.exceptions import ValidationError
from core.models.base import BaseModel

class Project(BaseModel):
    def validate_image(value):
        ext = value.name.split('.')[-1].lower()
        if ext != 'jpeg' and ext != 'jpg':
            raise ValidationError('Unsupported file extension. Only jpeg,jpg files are allowed.')

    project_id = models.CharField(max_length=200, primary_key=True)
    project_name = models.CharField(max_length=200 )
    resource = models.CharField(max_length=200 )
    image = models.ImageField(upload_to='images/project/', null=True, blank=True, validators=[validate_image])
    capacity_ac = models.DecimalField(max_digits=10, decimal_places=2 )
    capacity_dc = models.DecimalField(max_digits=10, decimal_places=2)
    utility_company = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    longitude = models.CharField(max_length=20,null=True, blank=True)
    latitude = models.CharField(max_length=20,null=True, blank=True)
    altitude = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    

class Task(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
