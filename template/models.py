from django.db import models

class MediaUser(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images', default='images/images.jpg')

    def __str__(self) -> str:
        return self.last_name

class Post(models.Model):
    owner = models.ForeignKey(MediaUser, null=True, on_delete=models.CASCADE)
    text = models.CharField()
