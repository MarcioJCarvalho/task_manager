from django.views.generic import TemplateView
# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

class SobreView(TemplateView):
    template_name = "paginas/sobre.html"

class UmlView(TemplateView):
    template_name = "paginas/uml.html"