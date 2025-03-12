from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Categorie(models.Model):
    nom=models.CharField(max_length=200)
    date_ajout=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-date_ajout']
    def __str__(self):
        return self.nom
       

 

class Produit(models.Model):
    titre=models.CharField(max_length=200)
    prix=models.FloatField()
    prixavant=models.FloatField(default=0)   
    description=models.TextField()
    categorie= models.ForeignKey(Categorie , related_name='categories', on_delete=models.CASCADE)
    image=models.CharField(max_length=5000)
    date_ajout=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-date_ajout']
    def __str__(self):
        return self.titre    

class Commande(models.Model):
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_commande']


    def __str__(self):
        return self.nom
      
