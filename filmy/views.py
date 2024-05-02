
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Film
from .forms import FilmForm, FilmFormNowy , ExtraInfoForm2, OcenaForm2, AktorForm2
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
@login_required
@permission_required("filmy.add_film")
def nowy_nowy(request):
    form = FilmFormNowy(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(wszystkie)
    return render(request, 'filmy/nowy.html', {'form': form})


@login_required
@permission_required("filmy.add_film")
def nowy2(request):
    form = FilmForm(request.POST or None)
    form_einfo = ExtraInfoForm2(request.POST or None)
    form_ocena = OcenaForm2(request.POST or None)
    form_aktor = AktorForm2(request.POST or None)
    if all([form.is_valid(), form_einfo.is_valid(), form_ocena.is_valid(), form_aktor.is_valid()]):
        film = form.save()
        einfo = form_einfo.save(commit=False)
        einfo.film = film
        einfo.save()
        ocena = form_ocena.save(commit=False)
        ocena.film = film
        ocena.save()
        aktor = form_aktor.save()
        aktor.filmy.add(film.id)
        aktor.save()
        return redirect(wszystkie)
    return render(request, 'filmy/nowy2.html', {'form': form, 'form_einfo':form_einfo, 'form_ocena': form_ocena, 'form_aktor': form_aktor})


