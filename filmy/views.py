
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Film
from .forms import FilmForm
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, permission_required

def wszystkie(request):
    filmy=Film.objects.all()
    context = {'filmy': filmy}
    return render(request, 'filmy/wszystkie.html', context)




def szczegoly(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    field_names = [f.name for f in Film._meta.get_fields()]
    for i,f in enumerate(field_names):
        if f == "ocena":
            field_names[i] = "ocena_set"
        elif f == "aktor":
            field_names[i] = "aktor_set"
    return render(request, 'filmy/szczegoly.html', {'film': film, 'field_names': field_names})
@login_required
@permission_required('filmy.add_film')
def nowy(request):
    form = FilmForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(wszystkie)
    return render(request, 'filmy/nowy.html', {'form': form})
@login_required
@permission_required('filmy.change_film')
def edytuj(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    form = FilmForm(request.POST or None, instance=film)
    if form.is_valid():
        form.save()
        return redirect(wszystkie)
    return render(request, 'filmy/nowy.html', {'form':form})
@login_required
@permission_required('filmy.delete_film')
def usun(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    if request.method=="POST":
        film.delete()
        return redirect(wszystkie)
    return render(request, 'filmy/usun.html', {'film': film})

def logout_view(request):
  logout(request)
  return HttpResponseRedirect(reverse('login'))


