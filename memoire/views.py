from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile
from django.core.mail import send_mail
import random
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect


def register_user(request, *args, **kwargs):
    if request.method == 'POST':
        # Récupération des données du formulaire
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        birthday = request.POST.get('birthday')
        sexe = request.POST.get('sexe')
        email = request.POST.get('email')
        user_type = request.POST.get('type')
        realisation_linkedin = request.POST.get('realisation_linkedin', None)
        photo_profil = request.FILES.get('photo_profil', None)

        # Validation des champs
        if UserProfile.objects.filter(email=email).exists():
            messages.error(request, "Un utilisateur avec cet email existe déjà.")
            return redirect('/register')

        try:
            # Génération du code de vérification à 6 chiffres
            verification_code = random.randint(100000, 999999)

            # Création de l'utilisateur
            user = UserProfile.objects.create(
                nom=nom,
                prenom=prenom,
                birthday=birthday,
                sexe=sexe,
                email=email,
                type=user_type,
                realisation_linkedin=realisation_linkedin,
                photo_profil=photo_profil,
            )
            user.save()

            # Envoi de l'email avec le code de vérification
            subject = "Votre code de vérification"
            email_body = (
                f"Bonjour {prenom} {nom},\n\n"
                f"Merci pour votre inscription sur notre plateforme.\n"
                f"Voici votre code de vérification : {verification_code}\n\n"
                f"Veuillez entrer ce code pour activer votre compte.\n\n"
                "Cordialement,\nL'équipe de notre plateforme"
            )
            verification_email = EmailMessage(
                subject=subject,
                body=email_body,
                from_email='michaelndekebai@gmail.com',  # Remplacez par votre email
                to=[email],
            )

            try:
                verification_email.send()  # Envoi de l'email
                messages.success(request, "Inscription réussie ! Un code de vérification a été envoyé à votre email.")

                # Enregistrez le code de vérification en session
                request.session['verification_code'] = verification_code
                request.session['user_email'] = email  # Adresse e-mail sous forme de chaîne
                return redirect('/verification')  # Redirigez vers une page de vérification
            except Exception as e:
                messages.error(request, f"L'envoi du code de vérification a échoué : {str(e)}")
                user.delete()  # Supprimez l'utilisateur si l'email échoue
                return redirect('/register')

        except Exception as e:
            messages.error(request, f"Une erreur est survenue : {str(e)}")
            return redirect('/register')

    return render(request, "register.html")


# Create your views here.
def home(request,*args, **kwargs):
    return HttpResponse("<h2 >Options de la Carte</h2>")

    
def login (request,*args, **kwargs):
    return render( request,"login.html")

from django.db.models import Q
from .models import Memoire

def liste_memoires(request):
    # Récupérer tous les mémoires
    memoires = Memoire.objects.all()

    # Filtres de recherche
    query = request.GET.get('q')
    if query:
        memoires = memoires.filter(
            Q(titre__icontains=query) |
            Q(domaine__icontains=query) |
            Q(auteur__prenom__icontains=query) |
            Q(auteur__nom__icontains=query) |
            Q(resume__icontains=query)
        )

    # Filtres supplémentaires
    domaine = request.GET.get('domaine')
    annee = request.GET.get('annee')

    if domaine:
        memoires = memoires.filter(domaine=domaine)
    
    if annee:
        memoires = memoires.filter(annee_publication=annee)

    # Récupérer les domaines et années uniques pour les filtres
    domaines_uniques = Memoire.objects.values_list('domaine', flat=True).distinct()
    annees_uniques = Memoire.objects.values_list('annee_publication', flat=True).distinct()

    context = {
        'memoires': memoires,
        'domaines': domaines_uniques,
        'annees': annees_uniques,
        'query_params': request.GET
    }
    
    return render(request, 'memoire.html', context)
    

def common(request,*args, **kwargs):
    
    
    
    return render( request,"index.html")
def verification_page(request):
    if request.method == 'POST':
        if request.method == 'POST':
            user_email = request.session.get('user_email')
            stored_code = request.session.get('verification_code')
            input_code = request.POST.get('verification_code')

        if not user_email or not stored_code:
            messages.error(request, "Aucun utilisateur en attente de vérification.")
            return redirect('/register')

        if input_code == str(stored_code):  # Compare les codes
            # Valider l'utilisateur ou effectuer d'autres actions
            messages.success(request, "Votre compte a été vérifié avec succès.")
            del request.session['verification_code']
            del request.session['user_email']
            return redirect('/login')  # Redirigez vers la page de connexion ou d'accueil
        else:
            messages.error(request, "Code de vérification incorrect.")
            return redirect('/verify-code')  # Rechargez la page de vérification

    return render(request, 'verified.html')

