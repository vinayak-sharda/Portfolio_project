from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255, default='Hi')
    pub_date = models.DateTimeField()
    body = models.TextField(default='Hi')
    image = models.ImageField(upload_to="images/")

    def summary(self):
        return self.body[:100]

    def pretty_time(self):
        return self.pub_date.strftime('%a %b %e %Y')

    def __str__(self):
        return self.title
