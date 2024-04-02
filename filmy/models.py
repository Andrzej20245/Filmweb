from django.db import models


class Film(models.Model):
    tytul = models.CharField(max_length=64, blank=False, unique=True)
    rok = models.PositiveSmallIntegerField(blank=False)
    opis = models.TextField(default="")
    premiera = models.DateField(null=True, blank=True)
    imdb_pkts = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return "{} ({})".format(self.tytul, str(self.rok))





class Ocena(models.Model):
    recenzja = models.TextField(default="", blank=True)
    gwiazdki = models.PositiveSmallIntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, null=True, blank=True)

    # <-- relacja many-to-1 z modelem 'Film'
    # Po ustaleniu relacji z modelem Film możliwa jest np. następująca
    # zmiana reprezentacji tekstowej modelu Ocena

    def __str__(self):
        rec = self.recenzja[:20] + ' ...'
        return "Film: {}, gwiazdki: {}, recenzja: {}".format(self.film.tytul, str(self.gwiazdki), rec)

    # Oceny związane z filmem można przywołać korzystając z atrybutu *film.ocena_set.all()*. s





class Aktor(models.Model):
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)
    filmy = models.ManyToManyField(Film)

    # <-- relacja many-to-many z modelem 'Film'
    # Po ustaleniu relacji z modelem Film możliwa jest np.
    # następująca zmiana reprezentacji tekstowej modelu Aktor

    def __str__(self):
        return "{} {}, gra w {} filmach z bazy danych".format(self.imie, self.nazwisko, str(self.filmy.count()))

    # Aktorów związanych z filmem można przywołać korzystając z atrybutu *film.aktor_set.all()*;<br>
    # Filmy przypisane do konkretnego aktora można przywołać korzystając z atrybutu *aktor.filmy.all()*.





class ExtraInfo(models.Model):
    GATUNEK = {
        (0, 'Inne'),
        (1, 'Horror'),
        (2, 'Komedia'),
        (3, 'Sci-fi'),
        (4, 'Dramat')
    }
    czas_trwania = models.PositiveSmallIntegerField(null=True, blank=True)
    gatunek = models.PositiveSmallIntegerField(choices=GATUNEK, null=True, blank=True)
    rezyser = models.CharField(max_length=50, blank=True, null=True)
    film = models.OneToOneField(Film, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        for g in list(self.GATUNEK):
            if g[0] == self.gatunek:
                gok = g[1]
        return "Film: {}, gatunek: {}, czas trwania: {}, reżyser: {}".format(self.film.tytul,
                                                                             gok, self.czas_trwania, self.rezyser)

    # Dodatkowe informacje związane z filmem można przywołać korzystając z atrybutu *film.extrainfo*.



