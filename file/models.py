from django.db import models

class file_file(models.Model):
    name = models.CharField(max_length=255)
    files = models.FileField(upload_to='file/%Y/%m/%d')
    

    def __unicode__(self):  
        return self.name



