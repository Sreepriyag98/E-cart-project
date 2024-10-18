from django.db import models

# Themes

class SiteSetting(models.Model):
    banner=models.ImageField(upload_to='media/site/')
    caption=models.TextField()


