# Python_Django_Final_task_Objektu_katalogas
# Prekių katalogas

Tai Django pagrindu sukurta Retų meno dirbinių prekių katalogo aplikacija. 
Ji leidžia atvaizduoti prekes su jų aprašymu, kaina ir kategorija. 
Naudojama SQLite duomenų bazė, taip pat pridedama statistika pagal kategorijas.

## Technologijos
- Python
- Django
- SQLite
- HTML/CSS

## Instrukcija kaip paleisti projektą

1. Suinstaliuokite priklausomus paketų sąrašus:
   pip install -r requirements.txt

2. Paleiskite Django serverį terminale:
python manage.py runserver

3. Prieiti prie administratoriaus sąsajos galite naudodami šią komandą:
python manage.py createsuperuser

4. Aplikacija bus pasiekiama naršyklėje adresu:
http://127.0.0.1:8000


UZDUOTIS:

Objektų katalogas naudojant Django
🔹 Projekto tema
Sukurkite Django aplikaciją, kuri atvaizduoja pasirinktų objektų katalogą, pvz.: prekių,
muzikos įrašų, knygų ar kitų objektų sąrašą ir informaciją apie juos.
🔹 Minimalus funkcionalumas (pažymys 5):
1. Sukurkite Django projektą ir aplikaciją (pvz. katalogas).
2. Sukurkite SQLite duomenų bazę su viena lentele, kurioje yra bent 15 objektų (įrašų).
3. Lentelė gali turėti tokius laukus kaip: id, pavadinimas, aprasymas, kaina,
kategorija.
4. Duomenis galima užpildyti per Django admin sąsają arba naudojant manage.py
shell.
5. Sukurkite pagrindinį puslapį, kuriame naudojant views.py ir templates
atvaizduojami visi katalogo įrašai (naudojant Django šablonų sistemą).
🔹 Pažymys 6:
Papildomai prie 5 balų reikalavimų:
1. Pridėkite paieškos laukelį, leidžiantį filtruoti įrašus pagal pavadinimą arba
kategoriją.
2. Paieška turi veikti per GET parametrus (pvz., ?kategorija=Knyga).
3. Jei paieška neįvesta, rodomi visi įrašai.
🔹 Pažymys 7–8:
Papildomai prie aukščiau nurodytų reikalavimų:1. Pridėkite galimybę pridėti naują objektą naudojant Django ModelForm.
2. Pridėkite galimybę redaguoti esamą objektą (naudojant UpdateView).
3. Pridėkite galimybę ištrinti objektą (naudojant DeleteView).
4. Pagrindiniame puslapyje objektų sąrašas turi būti atnaujinamas po kiekvieno
veiksmo.
🔹 Pažymys 8–10:
Papildomai:
1. Sukurkite antrinę lentelę, pavyzdžiui Kategorija, kuri turi ryšį su objektų lentele
(ForeignKey).
2. Sukurkite statistikos puslapį, kuriame būtų apskaičiuojama:
a. kiek objektų priklauso kiekvienai kategorijai;
b. vidutinė kaina pagal kategoriją;
c. brangiausias objektas;
d. pigiausias objektas.
3. Naudokite annotate(), Count(), Avg(), Max() iš Django ORM.
🔹 Galimos katalogo temos
• Muzikos albumai
• Prekės
• Knygos
• Elektroniniai įrenginiai
• Meno kūriniai