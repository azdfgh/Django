from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
import time
from calendar import month_name
from blog.models import *
from django.forms import ModelForm
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.forms import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.forms import AuthenticationForm

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
                    return redirect('/')
            else:
                return redirect('/')
    else:
        formulario = AuthenticationForm()
    context = {'formulario': formulario}
    return render(request,'login.html', context)

@login_required(login_url='/login/')
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    if request.method == 'POST':  
        form = SignUpForm(request.POST)  
        if form.is_valid():  
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            user = User.objects.create_user(username, email, password)
            user.save()
    	return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
 
    data = {
        'form': form,
    }
    return render_to_response('registro.html', data, context_instance=RequestContext(request))


def ponentrada(request):
	  if request.method == 'POST':
		  entradanueva = Entrada()	
		  formulario = FormularioEntrada(request.POST, instance = entradanueva)
		  if formulario.is_valid():
		  	formulario.save()
		        return HttpResponseRedirect('/')
	  else:
	  	formulario = FormularioEntrada()
	  return render_to_response('nuevo.html',dict(formulario=formulario), context_instance=RequestContext(request))

#@login_required(login_url='/login/')
def poncomentario(request, pk):

    """Add a new comment."""
    p = request.POST

    if 'mensaje' in p:
        autor = "Anonymous"
        if p["autor"]: autor = p["autor"]

        comentario = Comentario(identrada=Entrada.objects.get(pk=pk))
        cf = FormularioComentario(p, instance=comentario)
        cf.fields["autor"].required = False

        comentario = cf.save(commit=False)
        comentario.autor = autor
        comentario.save()
    return HttpResponseRedirect(reverse("blog.views.entrada", args=[pk]))

def entrada(request, pk):
    identrada = Entrada.objects.get(pk=int(pk))
    comentario = Comentario.objects.filter(identrada = identrada)
    d = dict(entrada= identrada,comentario = comentario,form=FormularioComentario(),usuario=request.user)
    d.update(csrf(request))
    return render_to_response("entrada.html",d)
    
def main(request):

    entrada = Entrada.objects.all().order_by("-fecha")
    paginator = Paginator(entrada,3)

    try: pagina = int(request.GET.get("page",'1'))
    except ValueError: pagina = 1

    try:
        entrada = paginator.page(pagina)
    except (InvalidPage, EmptyPage):
        entrada = paginator.page(paginator.num_pages)

    return render_to_response("listado.html",dict(entrada = entrada, user = request.user,entrada_list = entrada.object_list))



