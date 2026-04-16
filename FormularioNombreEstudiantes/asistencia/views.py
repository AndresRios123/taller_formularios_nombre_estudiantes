from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import AsistenciaForm

def formulario_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmacion')
    else:
        form = AsistenciaForm()

    return render(request, 'asistencia/formulario.html', {'form': form})


def confirmacion(request):
    return render(request, 'asistencia/confirmacion.html')