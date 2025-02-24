from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="trainers")
    description = models.TextField()