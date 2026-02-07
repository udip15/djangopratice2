from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    info = models.CharField(max_length=1000)

    def __str__(self):
        # return self.title
        return f"{self.title}-{self.info}"