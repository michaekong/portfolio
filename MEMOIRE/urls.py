from django.urls import path
from memoire.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
app_name = 'memoire'

urlpatterns = [
    # Page principale du portfolio
    path('liste_realisations/', liste_realisations, name='liste_realisations'),
    path('services', services, name='services'),
    path('admins/', admin_panel, name='admin_panel'),
    path('portfolio/', portfolio, name='portfolio'),
    path('',login, name='login'),
    path('login',login, name='login'),
   path('admin/', admin.site.urls),
   path('portfolio/<str:username>/', portfolio_view, name='portfolio_view'),

    # User Profile URLs
     path('blogs/', blog_list, name='blog_list'),
    path('add/', add_blog, name='add_blog'),
    path('edit/<int:blog_id>/', edit_blog, name='edit_blog'),
    path('delete/<int:blog_id>/', delete_blog, name='delete_blog'),
    path('Realisations/', realisation_list, name='realisation_list'),
    path('addrealisation/', add_realisation, name='add_realisation'),
    path('editrealisation/<int:realisationid>/', edit_realisation, name='edit_realisation'),
    path('deleterealisation/<int:realisationid>/', delete_realisation, name='delete_realisation'),
     path('skills/', skills_list, name='skills_list'),
      path('addskills/', add_skills, name='add_skills'),
    path('editskills/<int:skillsid>/', edit_skills, name='edit_skills'),
    path('deleteskills/<int:skillsid>/', delete_skills, name='delete_skills'),
      path('link/', link_list, name='link_list'),
      path('addlink/', add_link, name='add_link'),
    path('editlink/<int:linkid>/', edit_link, name='edit_link'),
    path('deletelink/<int:linkid>/', delete_link, name='delete_link'),
    path('service/', service_list, name='service_list'),
      path('addservice/', add_service, name='add_service'),
    path('editservice/<int:serviceid>/', edit_service, name='edit_service'),
    path('deleteservice/<int:serviceid>/', delete_service, name='delete_service'),
    path('domaine/', domaine_list, name='domaine_list'),
      path('adddomaine/', add_domaine, name='add_domaine'),
      path('edit_user_profile/', edit_user_profile, name='edit_user_profile'),

    path('editdomaine/<int:domaineid>/', edit_domaine, name='edit_domaine'),
    path('deletedomaine/<int:domaineid>/', delete_domaine, name='delete_domaine'),
    path('link_realisation/<int:realisationid>/', link_realisation, name='link_realisation'),
    path('img_realisation/<int:realisationid>/', img_realisation, name='img_realisation'),
     path('link/delete/<int:link_id>/', delete_link, name='delete_link'),
    path('image/delete/<int:image_id>/', delete_image, name='delete_image'),

    
]

# Serve media and static files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
