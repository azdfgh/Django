from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.conf import settings
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View
from django.views.generic import TemplateView

#Destinatarios

def verDestinatarios (request):
	dest = Destinatario.objects.all()
	context = {'destinatarios':dest}
	return render(request, 'destinatario.html', context)


def DetallesDestinatario (request, destinatario_id):
	dest = Destinatario.objects.get(pk=destinatario_id)
	context = {'destinatarioDetalle':dest}
	return render(request, 'detalleDestinatario.html', context)


@login_required(login_url='/login/')
def addDestinatario(request):
	if request.method == 'POST' :
		dest = Destinatario()
		formulario = DestinatarioForm (request.POST, instance = dest)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else :
		formulario = DestinatarioForm()
	return render_to_response ('addDestinatario.html', {'formulario':formulario}, context_instance = RequestContext(request))


#Paquetes

def verPaquetes (request):
	paq = Paquete.objects.all()
	context = {'paquetes':paq}
	return render(request, 'paquete.html', context)

def detallesPaquete (request, paquete_id):
	paq=Paquete.objects.get(pk=paquete_id)
	context={'paqueteDetalle':paq}
	return render(request,'detallesPaquete.html',context)

@login_required(login_url='/login')
def addPaquete(request):
	if request.method == 'POST' :
		paq = Paquete()
		formulario = PaqueteForm (request.POST, instance = paq)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else :
		formulario = PaqueteForm()
	return render_to_response ('addPaquete.html', {'formulario':formulario}, context_instance = RequestContext(request))

@login_required(login_url='/login')
def editarPaquete(request, Paquete_id):
	paquete = get_object_or_404(Paquete, pk = Paquete_id)
	if request.method == 'POST':
		formulario = PaqueteForm(request.POST, instance = paquete)
 
		if formulario.is_valid():
			formulario.save()
           	return HttpResponseRedirect('/')
	else:
 
		formulario = PaqueteForm(instance = paquete)
        context = { 'formulario': formulario,}
	return render_to_response('editarPaquete.html', context,  context_instance=RequestContext(request))


#Rutas (Como funciones)

#def verRuta(request):
#    rutas = Ruta.objects.all()
#    return render_to_response('rutas.html', {'rutas':rutas})


#def addRuta (request):
#	if request.method=='POST':
#		formulario = RutaForm(request.POST,request.FILES)
#		if formulario.is_valid():
#			formulario.save()
#			return HttpResponseRedirect('/')
#	else:
#		formulario = RutaForm()
#	context={'formulario':formulario}
#	return render(request,'addRuta.html',context)


#def detallesRuta (request,ruta_):
#	ruta=get_object_or_404 (Ruta, pk=ruta_)
#	context={'rutaDetalle':ruta}
#	return render_to_response('detallesRuta.html',context)



#Rutas (con Vistas basadas en clases)

class verRuta(View):
    template_name = 'rutas.html'
    def get(self, request, *args, **kwargs):
        rutas = Ruta.objects.all()
        return render(request, self.template_name, {'rutas':rutas})


class addRuta(View):
    form_class = RutaForm
    template_name = 'addRuta.html'

    def get(self, request, *args, **kwargs):
        formulario = self.form_class()        
        return render(request, self.template_name, {'formulario': formulario})

    def post(self, request, *args, **kwargs):
        formulario = self.form_class(request.POST, request.FILES)
        if formulario.is_valid():    
            formulario.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'formulario': formulario})


class detallesRuta(View):
    template_name = 'detallesRuta.html'

    def get(self, request, *arg, **kwargs):
        id = self.kwargs['Ruta_id']
        ruta = get_object_or_404(Ruta, pk = id)     
        return render(request,self.template_name,{'rutaDetalle':ruta,'user':request.user})


#Usuarios

def userLogin(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            user = request.POST['username']
            passwd = request.POST['password']
            access = authenticate(username=user, password=passwd)
            if access is not None:
                if access.is_active:
                    login(request, access)
                    return redirect('/')
                else:
                    return render(request, 'inactive.html')
            else:
                return render(request, 'nouser.html')
    else:
        formulario = AuthenticationForm()
    context = {'formulario': formulario}
    return render(request,'login.html', context)


@login_required(login_url='/login')
def userLogout(request):
    logout(request)
    return redirect('/')


