from django.db import models
from stdimage.models import StdImageField
from uuid import uuid4

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid4()}.{ext}'
    return filename

# Create your models here.
class Image(models.Model):
    descricao = models.CharField("Descrição", max_length=100)
    image = StdImageField('Image', upload_to=get_file_path, variations={'thumb':{'width':480, 'height':480, 'crop': True}})

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
    
    def __str__(self) -> str:
        return self.descricao