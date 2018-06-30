from django.contrib import admin
from .models import Redes
from .models import Intereses
from .models import Estudio
from .models import Experiencia

admin.site.register(Redes)
admin.site.register(Intereses)
admin.site.register(Estudio)
admin.site.register(Experiencia)