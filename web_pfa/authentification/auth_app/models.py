from django.db import models

class client(models.Model):
    username=models.CharField(max_length=50)
    mot_de_passe=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
