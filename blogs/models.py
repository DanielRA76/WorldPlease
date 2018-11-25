from django.db import models

# Creamos el modelo de Blog

class Blog(models.Model):

    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title
