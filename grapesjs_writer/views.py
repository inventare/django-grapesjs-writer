from django.views import View
from django.shortcuts import render

class EmailTemplateView(View):
    http_method_names = ['get', 'post']
    
    def get(self, request):
        context = {}
        template_name = 'grapesjs_writer/email.html'
        return render(request, template_name, context=context)
