from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255, default='Hi')
    pub_date = models.DateTimeField()
    body = models.TextField(default='Hi')
    image = models.ImageField(upload_to="images/")

