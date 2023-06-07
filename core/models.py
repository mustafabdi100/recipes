from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/images/')
    prep_time = models.IntegerField(default=0)
    cook_time = models.IntegerField(default=0)
    total_time = models.IntegerField(default=0)
    servings = models.IntegerField(default=1)
    ingredients = models.TextField(help_text="Enter each ingredient on a new line.")
    directions = models.TextField(help_text="Enter each step on a new line.")

    def __str__(self):
        return self.title
