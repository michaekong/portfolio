from django.db import models
from django import forms


class UserProfile(models.Model):
    SEXE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
        ('A', 'Autre'),
    ]

    TYPE_CHOICES = [
        ('standard', 'Standard'),
        ('admin', 'Administrateur'),
    ]

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    birthday = models.DateField()
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    email = models.EmailField(unique=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    realisation_linkedin = models.URLField(max_length=200, blank=True, null=True)
    photo_profil = models.ImageField(upload_to='photos_profil/', blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nom', 'prenom', 'birthday', 'sexe', 'email', 'type', 'realisation_linkedin', 'photo_profil']
    

class Memoire(models.Model):
    titre = models.CharField(max_length=200)
    domaine = models.CharField(max_length=100)
    annee_publication = models.PositiveIntegerField()
    images = models.ImageField(upload_to='memoires/images/', blank=True, null=True)
    auteur = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='memoires')
    resume = models.TextField()
    lien_telecharger = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.titre

class Encadrement(models.Model):
    memoire = models.ForeignKey(Memoire, on_delete=models.CASCADE, related_name='encadrements')
    encadrant = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='encadrements')

    def __str__(self):
        return f"Encadrement de {self.memoire.titre} par {self.encadrant.prenom} {self.encadrant.nom}"