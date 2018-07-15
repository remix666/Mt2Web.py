# Copyright (c) 2017-2018 ferchoafta@gmail.com
# Distribuido bajo la licencia MIT Software Licence
# Mas informacion http://www.opensource.org/licenses/mit-license.php

# Importando los modelos a usar
from apps.administracion.estadisticas.models import registroConectados

# importando funciones integradas en el framework
from django.views.generic import ListView


class getRegistroOn(ListView):
    title = 'Estadisticas'
    model = registroConectados
    template_name = 'inicio.html'
    queryset = model.objects.all()

    @staticmethod
    def has_permission(request):
        """
        Returns True if the given HttpRequest has permission to view
        *at least one* page in the admin site.
        """
        return request.user.is_active and request.user.is_staff

    def get_context_data(self, **kwargs):
        context = {
                # 'site_title': "Inicio",
                'title': self.title,
                'has_permission': self.has_permission(self.request),
                'opts': {'app_label': self.title}
            }

        context.update(super(getRegistroOn, self).get_context_data(**kwargs))

        return context

