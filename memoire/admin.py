from django.contrib import admin
from .models import *
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'type', 'sexe')
    list_filter = ('type', 'sexe')
    search_fields = ('nom', 'prenom', 'email')
@admin.register(Realisation)
class RealisationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'datet' )
    list_filter = ('datet', 'titre')
    search_fields = ('titre', 'resume', 'userealisation')    
@admin.register(Realisationimages)
class RealisationimagesAdmin(admin.ModelAdmin):
    list_display = ('nom', 'realimg')
    list_filter = ('nom', 'realimg')
    search_fields = ('nom', 'realimg')
@admin.register(Realisationlinks)
class RealisationlinksAdmin(admin.ModelAdmin):
    list_display = ('nom', 'realink')
    list_filter = ('nom', 'realink')
    search_fields = ('nom', 'realink')

@admin.register(Userservice)
class UserserviceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'servicevalue')
    list_filter = ('nom', 'servicevalue')
    search_fields = ('nom', 'servicevalue')
@admin.register(Userlink)
class UserlinkAdmin(admin.ModelAdmin):
    list_display = ('nom', 'linkvalue')
    list_filter = ('nom', 'linkvalue')
    search_fields = ('nom', 'linkvalue')
@admin.register(Userskills)
class UserskillsAdmin(admin.ModelAdmin):
    list_display = ('nom', 'skillsvalue')
    list_filter = ('nom', 'skillsvalue')
    search_fields = ('nom', 'skillsvalue')

@admin.register(Domaine)
class DomaineAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('titre', 'datet')
    list_filter = ('titre', 'datet')
    search_fields = ('titre', 'resume')
   

@admin.register(UnverifiedUserProfile)
class UnverifiedUserProfileAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'created_at', 'verification_code')
    search_fields = ('nom', 'prenom', 'email')
    list_filter = ('created_at',)