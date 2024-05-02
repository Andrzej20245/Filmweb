from django.forms import ModelForm, IntegerField, CharField
from .models import Film, ExtraInfo, Ocena, Aktor
from django.core.validators import MinValueValidator

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['tytul', 'rok', 'opis', 'premiera', 'imdb_pkts']


class FilmFormNowy(ModelForm):
     rok = IntegerField(validators=[MinValueValidator(2000, message="Film nie może pochodzić sprzed 2000 roku!!!!")])
     class Meta:
                model = Film
                fields = ['tytul', 'rok', 'opis', 'premiera', 'imdb_pkts']

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['tytul', 'rok', 'opis', 'premiera', 'imdb_pkts']


class FilmFormNowy(ModelForm):
    rok = IntegerField(validators=[MinValueValidator(2000, message="Film nie może pochodzić sprzed 2000 roku!!!!")])
    class Meta:
        model = Film
        fields = ['tytul', 'rok', 'opis', 'premiera', 'imdb_pkts']


class ExtraInfoForm(ModelForm):
    class Meta:
        model = ExtraInfo
        fields = '__all__'


class ExtraInfoForm2(ModelForm):
    class Meta:
        model = ExtraInfo
        exclude = ['film']


class OcenaForm2(ModelForm):
    class Meta:
        model = Ocena
        exclude = ['film']


class AktorForm2(ModelForm):
    imie = CharField(label='Aktor: imię ')
    nazwisko = CharField(label='Aktor: nazwisko ')
    class Meta:
        model = Aktor
        fields = ['imie', 'nazwisko']