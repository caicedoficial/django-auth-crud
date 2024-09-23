from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import TaksForm
from .models import Tasks
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def registrar(request):
    if request.method == 'GET':
        return render(request, 'signup.html', 
                      {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Registrer user
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password2']
                )
                user.save()
                login(request, user)
                return redirect('tareas')
            except:
                return render(request, 'signup.html', 
                      {'form': UserCreationForm,
                       'error': 'El usuario ya existe'})
            
        return render(request, 'signup.html', 
                      {'form': UserCreationForm,
                       'error': 'Las contraseñas no son iguales'})
    
@login_required
def tareas(request):

    tasks = Tasks.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html',{
        'tasks': tasks
    })

@login_required
def tareas_completadas(request):

    tasks = Tasks.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks.html',{
        'tasks': tasks
    })

@login_required
def tareas_detalles(request, task_id):
    
    if request.method == 'GET':
        task = get_object_or_404(Tasks, pk=task_id, user=request.user)
        form = TaksForm(instance=task)

        return render(request, 'task_detail.html',{
            'task': task,
            'form': form
            })
    else:
        try:
            task = get_object_or_404(Tasks, pk=task_id, user=request.user)
            form = TaksForm(request.POST, instance=task)
            form.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'task_detail.html',{
            'task': task,
            'form': form,
            'error': 'Hubo un error actualizando la tarea'
            })

@login_required  
def completar_tareas(request, task_id):
    task = get_object_or_404(Tasks, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tareas')

@login_required
def eliminar_tareas(request, task_id):
    task = get_object_or_404(Tasks, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tareas')

@login_required
def crear_tarea(request):

    if request.method == 'GET':
        return render(request, 'create_task.html',
                  {'form': TaksForm})
    else:
        try:
            form = TaksForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tareas')
        except:
            return render(request, 'create_task.html',
                  {'form': TaksForm,
                   'error': 'Por favor... Ingrese datos validos'})

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'signin.html', 
                {'form': AuthenticationForm
    })

    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'signin.html', 
                  {'form': AuthenticationForm,
                   'error': 'El usuario o contraseña son incorrectos'})
        else:
            login(request, user)
            return redirect('tareas')