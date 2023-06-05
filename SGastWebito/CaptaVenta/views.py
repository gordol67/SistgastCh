#from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import date


# def primera(request):
#    return HttpResponse("Primerita bien")
class EntradaVieW(TemplateView):
     template_name = "entrada.html"
     
     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['fecha']= date.today()
          return context
          

def index(request):
     return render(request,'SGastWebito/template/PBase.html')
# def index(request):
#    return HttpResponse('SGastWebito/template/PBase.html')
# def entvent(request):
#    context = {
#        'fecha': date.today()}
#    return render(request,'template/Entrada.html',context)
