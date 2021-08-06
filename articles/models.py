from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
        

class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title