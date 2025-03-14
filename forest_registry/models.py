from django.db import models
from core.models.base import BaseModel
from project.models import Project
from django.core.exceptions import ValidationError

def validate_image(value):
        ext = value.name.split('.')[-1].lower()
        if ext != 'jpeg' and ext != 'jpg':
            raise ValidationError('Unsupported file extension. Only jpeg,jpg files are allowed.')
    
class WoodSupplier(BaseModel):
    registration_id = models.IntegerField()
    name = models.CharField(max_length=200)
    registration_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    registration_document = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/WoodSupplier/', null=True, blank=True, validators=[validate_image])

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='wood_suppliers')

    class Meta:
        verbose_name = "Wood Supplier"
        verbose_name_plural = "Wood Suppliers"
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class WoodSupplierDocument(models.Model):
    wood_supplier = models.ForeignKey(
        WoodSupplier,
        on_delete=models.CASCADE,
        related_name='documents'
    )
    document_name = models.CharField(max_length=255)
    document_url = models.URLField(max_length=200, blank=True, null=True)
    
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.document_name} ({self.wood_supplier})"


class ForestPlot(BaseModel):
    PLOT_TYPE_CHOICES = [
        ('national', 'National Forest'),
        ('private', 'Private Forest'),
        ('community', 'Community Forest'),
    ]

    plot_type = models.CharField(
        max_length=20,
        choices=PLOT_TYPE_CHOICES,
        default='national',
        verbose_name="Forest Plot Type"
    )
    registration_id = models.IntegerField()
    location = models.CharField(max_length=200)
    registration_date = models.DateField()
    registration_name = models.CharField(max_length=200)
    authority = models.CharField(max_length=200)
    classification = models.CharField(max_length=200)
    removal_method = models.CharField(max_length=200)
    area = models.DecimalField(max_digits=10, decimal_places=2, help_text="Area in hectares")
    distance_from_road = models.DecimalField(max_digits=10, decimal_places=2, help_text="Distance in kilometers")
    image = models.ImageField(upload_to='images/ForestPlot/', null=True, blank=True, validators=[validate_image])

    wood_supplier = models.ForeignKey(WoodSupplier, on_delete=models.CASCADE, related_name='forest_plots')

    class Meta:
        verbose_name = "Forest Plot"
        verbose_name_plural = "Forest Plots"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.registration_name} - {self.location}"


class ForestDocument(models.Model):
    forest_plot = models.ForeignKey(ForestPlot, on_delete=models.CASCADE, related_name='documents')
    document_name = models.CharField(max_length=255)
    document_url = models.URLField(max_length=200)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.document_name} ({self.forest_plot})"
