from django.db import models

# Create your models here.

User_Permissions=(
    ('admin','admin'),
    ('developer','developer'),
    ('client','client'),

    )

class Regisration(models.Model):
    user_roll = models.CharField(max_length=120 , choices=User_Permissions)
    username = models.CharField(max_length=120 , unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    
    