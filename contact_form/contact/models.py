from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=50, name = 'First Name')
    last_name = models.CharField(max_length=50, name = 'Last Name')
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email