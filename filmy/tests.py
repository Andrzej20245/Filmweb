from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from .views import wszystkie, szczegoly, nowy, nowy_nowy, nowy2, usun, edytuj
from .models import Film, ExtraInfo

class FilmyTests(TestCase):


    def setUp(self):
        User.objects.create_superuser(username='admin', password='admin')

# Testowanie urls
    def test_urls_wszystkie(self):
        url = reverse('wszystkie')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, wszystkie)


    def test_urls_szczegoly(self):
        url = reverse('szczegoly', args=[61])
        self.assertEquals(resolve(url).func, szczegoly)

    def test_urls_nowy(self):
        url = reverse('nowy')
        self.assertEquals(resolve(url).func, nowy)

    def test_urls_nowy_nowy(self):
        url = reverse('nowy_nowy')
        self.assertEquals(resolve(url).func, nowy_nowy)

    def test_urls_nowy2(self):
        url = reverse('nowy2')
        self.assertEquals(resolve(url).func, nowy2)

    def test_urls_edytuj_film(self):
        url = reverse('edytuj', args=[31])
        self.assertEquals(resolve(url).func, edytuj)

    def test_urls_usun(self):
        url = reverse('usun', args=[3])
        self.assertEquals(resolve(url).func, usun)

# Testowanie views
    def test_views_wszystkie(self):
        client = Client()
        response = client.get(reverse('wszystkie'))
        self.assertEquals(response.status_code,200)

    def test_views_wszystkie_templates(self):
        client = Client()
        response = client.get(reverse('wszystkie'))
        self.assertTemplateUsed(response, 'filmy/wszystkie.html')

    def test_views_szczegoly(self):
        Film.objects.create(tytul="Film testowy", rok=2000)
        client = Client()
        response = client.get(reverse('szczegoly', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_views_szczegoly_templates(self):
        Film.objects.create(tytul="Film testowy", rok=2000)
        client = Client()
        response = client.get(reverse('szczegoly', args=[1]))
        self.assertTemplateUsed(response, 'filmy/szczegoly.html')

    def test_views_nowy(self):
        client = Client()
        client.login(username="admin", password="admin")
        response = client.get(reverse('nowy'))
        self.assertEquals(response.status_code, 200)

    def test_views_nowy_templates(self):
        client = Client()
        client.login(username="admin", password="admin")
        response = client.get(reverse('nowy'))
        self.assertTemplateUsed(response, 'filmy/nowy.html')

    def test_views_edytuj(self):
        film = Film.objects.create(tytul="Film testowy", rok=2000)
        client = Client()
        client.login(username="admin", password="admin")
        response = client.get(reverse('edytuj', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_views_edytuj_templates(self):
        film = Film.objects.create(tytul="Film testowy", rok=2000)
        client = Client()
        client.login(username="admin", password="admin")
        response = client.get(reverse('edytuj', args=[1]))
        self.assertTemplateUsed(response, 'filmy/nowy.html')

    def test_views_usun(self):
        film = Film.objects.create(tytul="Film testowy", rok=2000)
        client = Client()
        client.login(username="admin", password="admin")
        response = client.get(reverse('usun', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_views_usun_templates(self):
        film = Film.objects.create(tytul="Film testowy", rok=2000)
        client = Client()
        client.login(username="admin", password="admin")
        response = client.get(reverse('usun', args=[1]))
        self.assertTemplateUsed(response, 'filmy/usun.html')

# Testowanie models
    def test_models_film_jako_text(self):
        film = Film.objects.create(tytul="Film testowy", rok=2000)
        self.assertEquals(str(film), "{} ({})".format(film.tytul, str(film.rok)))

    def test_models_nowy_film_nie_jest_pusty(self):
        film = Film.objects.create(tytul="Film testowy", rok=2000)
        self.assertNotEquals(film, None)

    def test_models_film_jest_unikalny(self):
        film1 = Film.objects.create(tytul="Film testowy", rok=2000)
        with self.assertRaises(Exception):
            film2 = Film.objects.create(tytul="Film testowy", rok=2000)

    def test_models_nowy_film_jest_tylko_1(self):
        Film.objects.create(tytul="Film testowy", rok=2000)
        self.assertEquals(Film.objects.all().count(), 1)

    def test_models_extrainfo_czy_jest_w_choice(self):
        GATUNEK = [0, 1, 2, 3, 4]
        einfo = ExtraInfo.objects.create(gatunek=1, czas_trwania=90)
        self.assertIn(einfo.gatunek, GATUNEK)