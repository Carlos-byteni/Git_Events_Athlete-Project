# Importação dos pacotes de operação
from django.contrib import admin
from django.urls import path, include
from olimpic.views import populate_db


# Urls do projeto, associadas à app.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('olimpic.urls')),
    path('popular/', populate_db),
]

