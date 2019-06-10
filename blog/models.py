from django.db import models
from django.forms import ModelForm
from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.
class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=['mp4'])], null=True, verbose_name="")

    def __str__(self):
    	return str(self.videofile)
        