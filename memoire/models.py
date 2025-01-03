from django.db import models
from django.contrib.auth.hashers import make_password

from django.db import models
from django.contrib.auth.hashers import make_password

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
    pays = models.CharField(max_length=100,blank=True)
    ville= models.CharField(max_length=100,blank=True)
    tel=models.CharField(max_length=100,blank=True)
    email = models.EmailField(unique=True )
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES ,default='standard')
    cv = models.FileField(upload_to='memoires/pdf/', blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)

    photo_profil = models.ImageField(upload_to='photos_profil/', blank=True, null=True)

   
   

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Domaine(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom
from django.db import models

class Userlink(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    linkvalue=models.CharField(max_length=100, unique=True)
    userl = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='userl')
    img = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return self.nom
from django.db import models
class Userservice(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    img = models.ImageField(upload_to='profiles/', null=True, blank=True)
    servicevalue=models.CharField(max_length=100, unique=True)
    users = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return self.nom
from django.db import models
class Userskills(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    skillsvalue=models.IntegerField(default=0)
    userk = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='userk')
    img = models.ImageField(upload_to='profiles/', null=True, blank=True)
    def __str__(self):
        return self.nom
from django.db import models



class UnverifiedUserProfile(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
   
    sexe = models.CharField(max_length=1, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    type = models.CharField(max_length=50,default='standard')
    realisation_linkedin = models.URLField(null=True, blank=True)
    photo_profil = models.ImageField(upload_to='profiles/', null=True, blank=True)
    password = models.CharField(max_length=255)  # Mot de passe haché
    verification_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)


class Blog(models.Model):
    titre = models.CharField(max_length=200)
    
    userb = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='userb')
    images = models.ImageField(upload_to='memoires/images/', blank=True, null=True)
    datet = models.DateTimeField(auto_now_add=True)
    resume = models.TextField()
    state_CHOICES = [
        ('E', 'ENCOURS'),
        ('P', 'PASSER'),
       
    ]
    state = models.CharField(max_length=1, choices=state_CHOICES)
  
class Realisation(models.Model):
    titre = models.CharField(max_length=200)
    
    userealisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='userealisation')
    images = models.ImageField(upload_to='memoires/images/', blank=True, null=True)
    datet = models.DateTimeField()
    domaines = models.ManyToManyField(Domaine, related_name='Realisation')
    resume = models.TextField()
    resumer_detailler=models.TextField()
    documentation = models.FileField(upload_to='memoires/pdf/', blank=True)
    state_CHOICES = [
        ('E', 'ENCOURS'),
        ('P', 'PASSER'),
       
    ]
    state = models.CharField(max_length=1, choices=state_CHOICES)
class Realisationlinks(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    linkvalue=models.CharField(max_length=100, unique=True)
    realink = models.ForeignKey(Realisation, on_delete=models.CASCADE, related_name='realink')

    def __str__(self):
        return self.nom
from django.db import models
class Realisationimages(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    images = models.ImageField(upload_to='memoires/images/', blank=True, null=True)
    realimg = models.ForeignKey(Realisation, on_delete=models.CASCADE, related_name='realimg')
    

    def __str__(self):
        return self.nom    

