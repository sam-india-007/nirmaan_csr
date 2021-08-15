from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    #ContactListView,
    ContactDetailView,
    ContactCreateView,
    ContactUpdateView,
    ContactDeleteView
)

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('contact/new/', ContactCreateView.as_view(), name='contact-create'),
    path('contact/<int:pk>/update/', ContactUpdateView.as_view(), name='contact-update'),
    path('contact/<int:pk>/delete/', ContactDeleteView.as_view(), name='contact-delete'),
    path('table', views.table, name='contact-table'),
    path('testmail', views.test_mail, name='testmail'),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)