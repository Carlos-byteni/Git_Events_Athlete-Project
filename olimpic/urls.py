
from django.urls import path, include
from .views import PersonalViewSet, EventoViewSet
from rest_framework.routers import DefaultRouter

""" Defnicção do router que opera com PersonalViewSet.
    Router envia as instâncias para a urls esportistas/ , esportistas/personal/<id>, esportistas/evento/<int:ind>
"""

router = DefaultRouter() 
router.register('personal', PersonalViewSet, basename='personal'),
router.register('evento', EventoViewSet, basename='evento'),


urlpatterns = [
    path('esportistas/', include(router.urls)),   
    path('esportistas/personal/<int:ind>', include(router.urls)),  
    path('esportistas/evento/<int:ind>', include(router.urls)),      
]
