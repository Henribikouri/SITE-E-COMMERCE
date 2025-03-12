from django.contrib import admin
from .models import Categorie,Produit,Commande
 

# Register your models here.
class AdminCategorie(admin.ModelAdmin):
    list_display= ('nom', 'date_ajout')

class AdminProduit(admin.ModelAdmin):
    list_display= ('titre', 'prix', 'categorie', 'date_ajout')

class AdminCommande(admin.ModelAdmin):
    list_display = ('items','nom','email','address', 'ville', 'pays','total', 'date_commande', )    

admin.site.register(Produit, AdminProduit)
admin.site.register(Categorie, AdminCategorie)
admin.site.register(Commande, AdminCommande)