
from memoire.models import *
from django.shortcuts import render 

from django.db.models import Q, Count, Avg, Prefetch
def liste_realisations(request):
    try:
        idp = request.session['user_id']
        user = UserProfile.objects.get(id=idp)
    except UserProfile.DoesNotExist:
        return redirect("login")    

    userinfo = UserProfile.objects.prefetch_related(
        Prefetch(
            'userk',
            queryset=Userskills.objects.select_related('userk'),
            to_attr='skills_list'
        ),
        Prefetch(
            'users',
            queryset=Userservice.objects.select_related('users'),
            to_attr='service_list'
        ),
        Prefetch(
            'userl',
            queryset=Userlink.objects.select_related('userl'),
            to_attr='link_list'
        ),
        Prefetch(
            'userb',
            queryset=Blog.objects.select_related('userb'),
            to_attr='blog_list'
        ),
        Prefetch(
            'userealisation',
            queryset=Realisation.objects.select_related('userealisation'),
            to_attr='realisation_list'
        )
    ).select_related()

    for el in userinfo:
        if user.id == el.id:
            user = el

    # Récupérer tous les domaines
    domaines = Domaine.objects.all()

    context = {
        'user': user,
        'domaines': domaines,
    }

    return render(request, 'theme-particle.html', context)

def services(request):
   
    return render(request, 'js.html')
def admin_panel(request):
    try:
        
        idp=request.session['user_id']
        user = UserProfile.objects.get(id=idp)
    except:
        return redirect("login")    
  
    userinfo = UserProfile.objects.prefetch_related(
            Prefetch(
                'userk',
                queryset=Userskills.objects.select_related('userk'),
                to_attr='skills_list'
            ),
            Prefetch(
                'users',
                queryset=Userservice.objects.select_related('users'),
                to_attr='service_list'
            ), Prefetch(
                'userl',
                queryset=Userlink.objects.select_related('userl'),
                to_attr='link_list'
            ), Prefetch(
                'userb',
                queryset=Blog.objects.select_related('userb'),
                to_attr='blog_list'
            ), Prefetch(
                'userealisation',
                queryset=Realisation.objects.select_related('userealisation'),
                to_attr='realisation_list'
            )
          
          
        ).select_related(  )
    
    for el in  userinfo:
        if user.id==el.id:
            user=el
            
   
 
    context = {
        
        'user':user,
       
       
    }
    # ou récupérez l'utilisateur de la manière appropriée
    return render(request, 'admin.html', context)
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Blog

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Blog
from django.views.decorators.http import require_POST
def portfolio(request):
    userinfo = UserProfile.objects.prefetch_related(
            Prefetch(
                'userk',
                queryset=Userskills.objects.select_related('userk'),
                to_attr='skills_list'
            ),
            Prefetch(
                'users',
                queryset=Userservice.objects.select_related('users'),
                to_attr='service_list'
            ), Prefetch(
                'userl',
                queryset=Userlink.objects.select_related('userl'),
                to_attr='link_list'
            ), Prefetch(
                'userb',
                queryset=Blog.objects.select_related('userb'),
                to_attr='blog_list'
            ), Prefetch(
                'userealisation',
                queryset=Realisation.objects.select_related('userealisation'),
                to_attr='realisation_list'
            )
          
          
        ).select_related(  )
    # ou récupérez l'utilisateur de la manière appropriée
    return render(request, 'portfolio.html', {'userinfo': userinfo})
def login(request, *args, **kwargs):
  
  
    if request.method == 'POST':
        email = request.POST.get('email')
        


        # Validation des champs obligatoires
        if not email :
            messages.error(request, "Veuillez remplir tous les champs.",extra_tags="login")
            return redirect('/login')

        try:
            # Recherche de l'utilisateur par email
            user = UserProfile.objects.get(email=email)

            
                # Simule une connexion (via session)
            request.session['user_id'] = user.id
            request.session['user_email'] = user.email
            request.session['emailv'] = user.email

            messages.success(request, "Connexion réussie. Bienvenue !",extra_tags="login")

          
            return redirect('/liste_realisations')  # Page pour les administrateurs
            
       
            
        except UserProfile.DoesNotExist:
            messages.error(request, "Aucun compte trouvé avec cet email.",extra_tags="login")
            return render(request,"login.html",{"error":"Aucun compte trouvé avec cet email."})
    return render(request, "login.html")
def blog_list(request):
    try:
        
        idp=request.session['user_id']
        user = UserProfile.objects.get(id=idp)
    except:
        return redirect("login")    
    userinfo = UserProfile.objects.prefetch_related(
            Prefetch(
                'userk',
                queryset=Userskills.objects.select_related('userk'),
                to_attr='skills_list'
            ),
            Prefetch(
                'users',
                queryset=Userservice.objects.select_related('users'),
                to_attr='service_list'
            ), Prefetch(
                'userl',
                queryset=Userlink.objects.select_related('userl'),
                to_attr='link_list'
            ), Prefetch(
                'userb',
                queryset=Blog.objects.select_related('userb'),
                to_attr='blog_list'
            ), Prefetch(
                'userealisation',
                queryset=Realisation.objects.select_related('userealisation'),
                to_attr='realisation_list'
            )
          
          
        ).select_related(  )
    
    for el in  userinfo:
        if user.id==el.id:
            user=el
            
   
 
    context = {
        
        'user':user,
        
       
       
    }
  
    return render(request, 'blog_list.html', context)  # Remplacez par le chemin correct
def add_blog(request):
    try:
        
        idp=request.session['user_id']
        user = UserProfile.objects.get(id=idp)
    except:
        return redirect("login")    
    if request.method == 'POST':
        titre = request.POST.get('titre')
        userb = user
        resume = request.POST.get('resume')
        state = request.POST.get('state')
        images = request.FILES.get('image')

        # Créer un nouvel objet Blog
        blog = Blog(
            titre=titre,
            userb=user,
            resume=resume,
            state=state,
            images=images,
        )
        blog.save()  # Enregistrer le blog
        return redirect('blog_list')  # Rediriger vers la liste des blogs
    
    # Si la méthode n'est pas POST, afficher la page d'ajout (vous pouvez créer une vue dédiée)
    return render(request, 'add_blog.html', {'userprofiles': userprofiles})  # Créez un template pour le formulaire
def edit_blog(request, blog_id):
    try:
        
        idp=request.session['user_id']
        user = UserProfile.objects.get(id=idp)
    except:
        return redirect("login")  
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        blog.titre = request.POST.get('titre', blog.titre)
        blog.userb=user
        blog.resume = request.POST.get('resume', blog.resume)
        blog.state = request.POST.get('state', blog.state)
        blog.images = request.FILES.get('image', blog.images)  # Mettre à jour l'image seulement si une nouvelle est fournie
        
        blog.save()  # Enregistrer les modifications
        return redirect('blog_list')

    return render(request, 'edit_blog.html', {'blog': blog, 'userprofiles': userprofiles})  # Créez un template pour le formulaire
@require_POST  # Pour s'assurer que cette vue ne traite que les requêtes POST
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()  # Supprimer le blog
    return redirect('blog_list')  # Rediriger vers la liste des blogs

def realisation_list(request):
    try:
        
        idp=request.session['user_id']
        user = UserProfile.objects.get(id=idp)
    except:
        return redirect("login")    
  
    userinfo = UserProfile.objects.prefetch_related(
            Prefetch(
                'userk',
                queryset=Userskills.objects.select_related('userk'),
                to_attr='skills_list'
            ),
            Prefetch(
                'users',
                queryset=Userservice.objects.select_related('users'),
                to_attr='service_list'
            ), Prefetch(
                'userl',
                queryset=Userlink.objects.select_related('userl'),
                to_attr='link_list'
            ), Prefetch(
                'userb',
                queryset=Blog.objects.select_related('userb'),
                to_attr='blog_list'
            ), Prefetch(
                'userealisation',
                queryset=Realisation.objects.select_related('userealisation'),
                to_attr='realisation_list'
            )
          
          
        ).select_related(  )
    domaines = Domaine.objects.all()
    
    for el in  userinfo:
        if user.id==el.id:
            user=el
            
   
 
    context = {
        
        'user':user,
        'domaines':domaines,
        
       
       
    }
  
    return render(request, 'realisation_list.html', context)  # Remplacez par le chemin correct
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Realisation, UserProfile
from django.utils import timezone

def add_realisation(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        try:
            user = UserProfile.objects.get(id=user_id)

            titre = request.POST.get('titre')
            resume = request.POST.get('resume')
            resumer_detailler = request.POST.get('resumed')
            datet = request.POST.get('datet')
            state = request.POST.get('state')
            domaines_ids = request.POST.getlist('domaines')  # Récupération des IDs des domaines
            images = request.FILES.get('images')
            documentation = request.FILES.get('documentation')

            # Créer la nouvelle réalisation
            realisation = Realisation(
                titre=titre,
                userealisation=user,
                resume=resume,
                resumer_detailler=resumer_detailler,
                datet=timezone.datetime.strptime(datet, '%Y-%m-%d'),
                state=state,
                images=images,
                documentation=documentation,
            )
            realisation.save()

            # Ajouter les domaines sélectionnés
            if domaines_ids:
                realisation.domaines.set(domaines_ids)

            messages.success(request, 'La réalisation a été ajoutée avec succès.')
            return redirect('liste_realisations')

        except UserProfile.DoesNotExist:
            messages.error(request, 'Utilisateur non trouvé.')
            return redirect('login')

    return redirect('liste_realisations')
def edit_realisation(request, realisationid):
    try:
        idp = request.session['user_id']
        user = UserProfile.objects.get(id=idp)
    except UserProfile.DoesNotExist:
        return redirect("login") 

    realisation = get_object_or_404(Realisation, pk=realisationid)

    if request.method == 'POST':
        # Mettre à jour les champs de la réalisation
        realisation.titre = request.POST.get('titre', realisation.titre)
        realisation.userealisation = user
        realisation.resume = request.POST.get('resume', realisation.resume)
        realisation.resumer_detailler = request.POST.get('resumed', realisation.resumer_detailler)
        realisation.state = request.POST.get('state', realisation.state)
        
        # Mise à jour des fichiers uniquement si de nouveaux fichiers sont fournis
        if 'image' in request.FILES:
            realisation.images = request.FILES['image']
        if 'documentation' in request.FILES:
            realisation.documentation = request.FILES['documentation']
        
        realisation.datet = request.POST.get('datet', realisation.datet)
        
        # Gérer la mise à jour des domaines
        domaines_ids = request.POST.getlist('domaines')  # Liste des domaines sélectionnés
        realisation.domaines.set(domaines_ids)  # Mettre à jour la relation ManyToMany 

        realisation.save()  # Enregistrer les modifications
        messages.success(request, 'La réalisation a été mise à jour avec succès.')
        return redirect('realisation_list')

    # Récupérer tous les domaines pour afficher dans le formulaire
    domaines = Domaine.objects.all()

    context = {
        'realisation': realisation,
        'domaines': domaines,
    }

    return render(request, 'edit_realisation.html', context)  # Utiliser le bon template
@require_POST  # Pour s'assurer que cette vue ne traite que les requêtes POST
def delete_realisation(request, realisationid):
    realisation = get_object_or_404(Realisation, pk=realisationid)
    realisation.delete()  # Supprimer le blog
    return redirect('realisation_list')  # Rediriger vers la liste des blogs
def skills_list(request):
    try:
        
        idp=request.session['user_id']
        user = UserProfile.objects.get(id=idp)
    except:
        return redirect("login")    
  
    userinfo = UserProfile.objects.prefetch_related(
            Prefetch(
                'userk',
                queryset=Userskills.objects.select_related('userk'),
                to_attr='skills_list'
            ),
            Prefetch(
                'users',
                queryset=Userservice.objects.select_related('users'),
                to_attr='service_list'
            ), Prefetch(
                'userl',
                queryset=Userlink.objects.select_related('userl'),
                to_attr='link_list'
            ), Prefetch(
                'userb',
                queryset=Blog.objects.select_related('userb'),
                to_attr='blog_list'
            ), Prefetch(
                'userealisation',
                queryset=Realisation.objects.select_related('userealisation'),
                to_attr='realisation_list'
            )
          
          
        ).select_related(  )
    
    for el in  userinfo:
        if user.id==el.id:
            user=el
            
   
 
    context = {
        
        'user':user,
        
       
       
    }
  
    return render(request, 'skills_list.html', context)  # Remplacez par le chemin correct
def add_skills(request):
    try:
        
        idp=request.session['user_id']
        user = UserProfile.objects.get(id=idp)
    except:
        return redirect("login")    
    if request.method == 'POST':
        nom = request.POST.get('nom')
       
     
        skillsvalue = request.POST.get('skillsvalue')
       
        images = request.FILES.get('image')
        
        

        # Créer un nouvel objet Blog
        skills = Userskills(
            nom=nom,
            userk=user,
         
           skillsvalue=skillsvalue,
            img=images,
        )
        skills.save()  # Enregistrer le blog
        return redirect('skills_list')  # Rediriger vers la liste des blogs
    
    # Si la méthode n'est pas POST, afficher la page d'ajout (vous pouvez créer une vue dédiée)
    return render(request, 'add_skills.html', ) 
def edit_skills(request, skillsid):
    try:
        
        idp=request.session['user_id']
        user = UserProfile.objects.get(id=idp)
    except:
        return redirect("login") 
    skills= get_object_or_404(Userskills, pk=skillsid)
    if request.method == 'POST':
    
        skills.nom = request.POST.get('nom',skills.nom)
       
     
        skills.skillsvalue = request.POST.get('skillsvalue',skills.skillsvalue)
       
        skills.img = request.FILES.get('image',skills.img)
         
        skills.save()  # Enregistrer les modifications
        return redirect('skills_list')

    return render(request, 'edit_blog.html', {'blog': blog}  )# Créez un template pour le formulaire
@require_POST  # Pour s'assurer que cette vue ne traite que les requêtes POST
def delete_skills(request, skillsid):
    skills = get_object_or_404(Userskills, pk=skillsid)
    skills.delete()  # Supprimer le blog
    return redirect('skills_list')  # Rediriger vers la liste des blogs
def link_list(request):
    try:
        
        idp=request.session['user_id']
        user = UserProfile.objects.get(id=idp)
    except:
        return redirect("login")    
  
    userinfo = UserProfile.objects.prefetch_related(
            Prefetch(
                'userk',
                queryset=Userskills.objects.select_related('userk'),
                to_attr='skills_list'
            ),
            Prefetch(
                'users',
                queryset=Userservice.objects.select_related('users'),
                to_attr='service_list'
            ), Prefetch(
                'userl',
                queryset=Userlink.objects.select_related('userl'),
                to_attr='link_list'
            ), Prefetch(
                'userb',
                queryset=Blog.objects.select_related('userb'),
                to_attr='blog_list'
            ), Prefetch(
                'userealisation',
                queryset=Realisation.objects.select_related('userealisation'),
                to_attr='realisation_list'
            )
          
          
        ).select_related(  )
    
    for el in  userinfo:
        if user.id==el.id:
            user=el
            
   
 
    context = {
        
        'user':user,
        
       
       
    }
  
    return render(request, 'link_list.html', context)  # Remplacez par le chemin correct
def add_link(request):
    try:
        
        idp=request.session['user_id']
        user = UserProfile.objects.get(id=idp)
    except:
        return redirect("login")    
    if request.method == 'POST':
        nom = request.POST.get('nom')
       
     
        linkvalue = request.POST.get('linkvalue')
       
        images = request.FILES.get('image')
        
        

        # Créer un nouvel objet Blog
        link= Userlink(
            nom=nom,
            userl=user,
         
           linkvalue=linkvalue,
            img=images,
        )
        link.save()  # Enregistrer le blog
        return redirect('link_list')  # Rediriger vers la liste des blogs
    
    # Si la méthode n'est pas POST, afficher la page d'ajout (vous pouvez créer une vue dédiée)
    return render(request, 'add_link.html', ) 
def edit_link(request, linkid):
    try:
        
        idp=request.session['user_id']
        user = UserProfile.objects.get(id=idp)
    except:
        return redirect("login") 
    link= get_object_or_404(Userlink, pk=linkid)
    if request.method == 'POST':
    
        link.nom = request.POST.get('nom',link.nom)
       
     
        link.linkvalue = request.POST.get('linkvalue',link.linkvalue)
       
        link.img = request.FILES.get('image',link.img)
         
        link.save()  # Enregistrer les modifications
        return redirect('link_list')

    return render(request, 'edit_blog.html'  )# Créez un template pour le formulaire
@require_POST  # Pour s'assurer que cette vue ne traite que les requêtes POST
def delete_link(request, linkid):
    link = get_object_or_404(Userlink, pk=linkid)
    link.delete()  # Supprimer le blog
    return redirect('link_list')  # Rediriger vers la liste des blogs
def service_list(request):
    try:
        
        idp=request.session['user_id']
        user = UserProfile.objects.get(id=idp)
    except:
        return redirect("login")    
  
    userinfo = UserProfile.objects.prefetch_related(
            Prefetch(
                'userk',
                queryset=Userskills.objects.select_related('userk'),
                to_attr='skills_list'
            ),
            Prefetch(
                'users',
                queryset=Userservice.objects.select_related('users'),
                to_attr='service_list'
            ), Prefetch(
                'userl',
                queryset=Userlink.objects.select_related('userl'),
                to_attr='link_list'
            ), Prefetch(
                'userb',
                queryset=Blog.objects.select_related('userb'),
                to_attr='blog_list'
            ), Prefetch(
                'userealisation',
                queryset=Realisation.objects.select_related('userealisation'),
                to_attr='realisation_list'
            )
          
          
        ).select_related(  )
    
    for el in  userinfo:
        if user.id==el.id:
            user=el
            
   
 
    context = {
        
        'user':user,
        
       
       
    }
  
    return render(request, 'service_list.html', context)  # Remplacez par le chemin correct
def add_service(request):
    try:
        
        idp=request.session['user_id']
        user = UserProfile.objects.get(id=idp)
    except:
        return redirect("login")    
    if request.method == 'POST':
        nom = request.POST.get('nom')
       
     
        servicevalue = request.POST.get('servicevalue')
       
        images = request.FILES.get('image')
        
        

        # Créer un nouvel objet Blog
        service= Userservice(
            nom=nom,
            users=user,
         
           servicevalue=servicevalue,
            img=images,
        )
        service.save()  # Enregistrer le blog
        return redirect('service_list')  # Rediriger vers la liste des blogs
    
    # Si la méthode n'est pas POST, afficher la page d'ajout (vous pouvez créer une vue dédiée)
    return render(request, 'add_service.html', ) 
def edit_service(request, serviceid):
    try:
        
        idp=request.session['user_id']
        user = UserProfile.objects.get(id=idp)
    except:
        return redirect("login") 
    service= get_object_or_404(Userservice, pk=serviceid)
    if request.method == 'POST':
    
        service.nom = request.POST.get('nom',service.nom)
       
     
        service.servicevalue = request.POST.get('servicevalue',service.servicevalue)
       
        service.img = request.FILES.get('image',service.img)
         
        service.save()  # Enregistrer les modifications
        return redirect('service_list')

    return render(request, 'edit_blog.html'  )# Créez un template pour le formulaire
@require_POST  # Pour s'assurer que cette vue ne traite que les requêtes POST
def delete_service(request, serviceid):
    link = get_object_or_404(Userservice, pk=serviceid)
    link.delete()  # Supprimer le blog
    return redirect('service_list')  # Rediriger vers la liste des bservice
def domaine_list(request):
    try:
        
        idp=request.session['user_id']
        user = UserProfile.objects.get(id=idp)
    except:
        return redirect("login")    
  
    
    domaines= Domaine.objects.all()
  
   
 
    context = {
        
        'domaines':domaines,
        
       
       
    }
  
    return render(request, 'domaine_list.html', context)  # Remplacez par le chemin correct
def add_domaine(request):
    try:
        
        idp=request.session['user_id']
        user = UserProfile.objects.get(id=idp)
    except:
        return redirect("login")    
    if request.method == 'POST':
        nom = request.POST.get('nom')
       
     
      
        

        # Créer un nouvel objet Blog
        domaine = Domaine(
            nom=nom,
         
        )
        domaine.save()  # Enregistrer le blog
        return redirect('domaine_list')  # Rediriger vers la liste des blogs
    
    # Si la méthode n'est pas POST, afficher la page d'ajout (vous pouvez créer une vue dédiée)
    return render(request, 'add_domaine.html', ) 
def edit_domaine(request, domaineid):
    try:
        
        idp=request.session['user_id']
        user = UserProfile.objects.get(id=idp)
    except:
        return redirect("login") 
    domaine= get_object_or_404(Domaine, pk=domaineid)
    if request.method == 'POST':
    
        domaine.nom = request.POST.get('nom',domaine.nom)
       
         
        domaine.save()  # Enregistrer les modifications
        return redirect('domaine_list')

    return render(request, 'edit_blog.html', {'blog': blog}  )# Créez un template pour le formulaire
@require_POST  # Pour s'assurer que cette vue ne traite que les requêtes POST
def delete_domaine(request, domaineid):
    domaine = get_object_or_404(Domaine, pk=domaineid)
    domaine.delete()  # Supprimer le blog
    return redirect('domaine_list')  # Rediriger vers la liste des blogs
def link_realisation(request, realisationid):
    try:
        
        idp=request.session['user_id']
      
    except:
        return redirect("login") 
    realisation= get_object_or_404(Realisation, pk=realisationid)
    if request.method == 'POST':
        nom = request.POST.get('nom')
       
     
        linkvalue = request.POST.get('linkvalue')
     
        
        

        # Créer un nouvel objet Blog
        link = Realisationlinks(
            nom=nom,
           linkvalue=linkvalue,
         realink=realisation,
           
           
        )
        link.save()  # Enregistrer le blog
        return redirect('realisation_list')  # Rediriger vers la liste des blogs
    
    # Si la méthode n'est pas POST, afficher la page d'ajout (vous pouvez créer une vue dédiée)
    return render(request, 'add_skills.html', ) # Créez un template pour le formulaire
def img_realisation(request, realisationid):
    try:
        
        idp=request.session['user_id']
      
    except:
        return redirect("login") 
    realisation= get_object_or_404(Realisation, pk=realisationid)
    if request.method == 'POST':
        nom = request.POST.get('nom')
       
     
        images = request.FILES.get('image')
     
        
        

        # Créer un nouvel objet Blog
        img = Realisationimages(
            nom=nom,
           images=images,
         realimg=realisation,
           
           
        )
        img.save()  # Enregistrer le blog
        return redirect('realisation_list')  # Rediriger vers la liste des blogs
    
    # Si la méthode n'est pas POST, afficher la page d'ajout (vous pouvez créer une vue dédiée)
    return render(request, 'add_skills.html', ) # Créez un template pour le formulaire



def delete_link(request, link_id):
    link = get_object_or_404(Realisationlinks, pk=link_id)
    link.delete()
    return redirect('realisation_list')

def delete_image(request, image_id):
    image = get_object_or_404(Realisationimages, pk=image_id)
    image.delete()
    return redirect('realisation_list')
def edit_user_profile(request, ):
    try:
        
        idp=request.session['user_id']
      
    except:
        return redirect("login") 
    user = get_object_or_404(UserProfile, pk=idp)

    if request.method == 'POST':
        # Mettre à jour les champs avec les données du formulaire
        user.nom = request.POST.get('nom', user.nom)
        user.prenom = request.POST.get('prenom', user.prenom)
        user.pays = request.POST.get('pays', user.pays)
        user.ville = request.POST.get('ville', user.ville)
        user.tel = request.POST.get('tel', user.tel)
        user.email = request.POST.get('email', user.email)
        user.sexe = request.POST.get('sexe', user.sexe)
        user.type = request.POST.get('type', user.type)
        user.description = request.POST.get('description', user.description)

        # Gérer le fichier CV
        if 'cv' in request.FILES:
            user.cv = request.FILES['cv']

        # Gérer la photo de profil
        if 'photo_profil' in request.FILES:
            user.photo_profil = request.FILES['photo_profil']

        # Sauvegarder les modifications
        user.save()
        return redirect('liste_realisations')  # Redirection vers la vue de profil ou une autre page appropriée

    return render(request, 'user_list.html', {'user': user})