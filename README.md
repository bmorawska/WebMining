### Ćwiczenie nr 1

##### Zajęcia nr 1

* [X] Zainstalować oprogramowanie weka (Open Source) http://www.cs.waikato.ac.nz/ml/weka/ 
* [X] Zapoznać się z funkcjami oprogramowania (Preprocess, Cluster, Associate)
* [X] Ze strony ftp://ita.ee.lbl.gov/html/contrib/ pobrać wybrany plik logów
* [X] Obciąć wybrany plik do 50000 rekordów
* [X] Powtórzyć algorytmy analizy klastrowej i budowania reguł asocjacyjnych

__Wybrane dane:__ ``NASA-HTTP.html`` -> Jul 01 to Jul 31, ASCII format, 20.7 MB gzip compressed.
Jego skrócona wersja (do 50000 rekordów) to ``short.csv``.

### Ćwiczenie nr 2

#### Zajęcia nr 2

* [X] Wyodrębnić zmienne: data, godzina, metoda, adres strony, protokół
* [X] Wybrać rekordy o metodzie GET
* [X] Wybrać rekordy o kodzie statusu 200
* [X] Usunąć rekordy zawierające odwołania do plików graficznych (jpg, gif, bmp, xmb itp.)
* [X] Zidentyfikować użytkowników (``users.csv``)
* [X] Wyodrębnić sesje, przyjmując wybrany odstęp czasowy (``sessions_singles_removed.csv`` -> w ``sessions.csv``
są tylko te rekordy, w których w założonym czasie odwiedzono więcej niż jedną stronę. W ``sessions_singles_removed.csv``
nie są usunięte te przypadki, w których w czasie sesji odwiedzona została tylko jedna strona)
* [X] Wybrać najbardziej popularne strony, wyznaczyć liczbę odwołań do nich (``most_popular_sites.csv``)
 i obliczyć jaki jest to procent całości (``percent_of_occurences.csv``)
 
### Ćwiczenie nr 3

#### Zajęcia nr 3

* [X] Wybrać strony dla których liczba odwiedzin była większa niż 0.5% (skrypt ``trending.py``, 
a wynik w ``percent_of_occurences.csv`` )
* [X] Nadać atrybuty sesjom:
    * [X] Czas sesji
    * [X] Liczba działań w czasie sesji
    * [X] Przeciętny czas na stronę
    * [X] Zmienne flagowe dla stron wybranych w p. 1 (przeprowadzić transformację
koszykową)
* [X] Zapisać plik danych w formacie arff (przykłady w katalogu „Data” programu Weka)
* [X] Wykonać analizę klastrową sesji przy pomocy programu „Weka” (Działa tylko trzeba wywalić z ``session_attributes.arff``
w Wece pola ``sessionID``, ``user``, ``start_time``, ``end_time``).
* [ ] ***Wyciągnąć wnioski***
* [X] Dla każdego zidentyfikowanego użytkownika nadać mu atrybuty odpowiadające
odwiedzanym stronom (cały plik, który to robi to ``mining_users.py``, a wynik jest w ``user_attributes.arff``)  
* [X] Dokonać analizy klastrowej użytkowników. (Działa po usunięciu w Wece pola ``userID``)
* [ ] ***Wyciągnąć wnioski***

---
**NOTE**

Nie do końca wiem dlaczego, ale zarówno w analizie koszykowej występuje
**czasami** dosyć dziwny błąd. Mianowicie w ``mining_users.py`` we
fragmencie

```python
for i, row in data.iterrows():
    vp = row.sites
    for site in vp:
        if site in sites:
            attributes.iloc[i][site] = 1
```

oraz w ``adding_attributes.py`` w

```python
for i, row in sessions.iterrows():
    vp = ast.literal_eval(row.visited_pages)
    for site in vp:
        if site in sites:
            attributes.loc[i][site] = 1

```

żeby program działał trzeba ustawić się debuggerem w ostatniej linijce każdego z kodów.
Kiedy debugger się zatrzyma to można go "zdjąć" i puścić program do końca. Będzie działał.
Na pewno jest to do poprawy, ale nie mam zupełnie pomysłu o co może chodzić.
---
