from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:pk>/', views.project_details, name='project_details'),
    path('filter-projects/', views.filter_projects, name='filter_projects'),
    path('submit_contact_form/', views.submit_contact_form, name='submit_contact_form'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)