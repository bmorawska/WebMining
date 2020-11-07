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
w Wece pola ``sessionID``).
* [ ] ***Wyciągnąć wnioski***
    * dla 2 klastrów
        ```text
        === Model and evaluation on training set ===
        
        Clustered Instances
        
        0      2174 ( 73%)
        1       813 ( 27%)   
        ```
    * dla 5 klastrów
        ```text
        === Model and evaluation on training set ===

        Clustered Instances
        
        0       176 (  6%)
        1       193 (  6%)
        2       840 ( 28%)
        3       372 ( 12%)
        4      1406 ( 47%)
        ```
    * dla 10 klastrów
       ```text
       === Model and evaluation on training set ===
        
        Clustered Instances
        
        0       111 (  4%)
        1       185 (  6%)
        2       301 ( 10%)
        3       819 ( 27%)
        4       536 ( 18%)
        5       180 (  6%)
        6       236 (  8%)
        7       181 (  6%)
        8       103 (  3%)
        9       335 ( 11%)
       ```

        ***Wnioski ???***

* [X] Dla każdego zidentyfikowanego użytkownika nadać mu atrybuty odpowiadające
odwiedzanym stronom (cały plik, który to robi to ``mining_users.py``, a wynik jest w ``user_attributes.arff``)  
* [X] Dokonać analizy klastrowej użytkowników. (Działa po usunięciu w Wece pola ``userID``)
* [ ] ***Wyciągnąć wnioski***
    * dla 10 klastrów:
        ```text
        === Model and evaluation on training set ===

        Clustered Instances
        
         0       400 ( 11%)
         1       421 ( 11%)
         2      1932 ( 51%)
         3       136 (  4%)
         4       313 (  8%)
         5        57 (  2%)
         6       174 (  5%)
         7        33 (  1%)
         8       251 (  7%)
         9        65 (  2%)
        ```
    * dla 5 klastrów:
        ```text
        === Model and evaluation on training set ===

        Clustered Instances
        
        0       546 ( 14%)
        1      1196 ( 32%)
        2      1638 ( 43%)
        3       337 (  9%)
        4        65 (  2%)
        ```
    * dla 2 klastrów
        ```text
        === Model and evaluation on training set ===

        Clustered Instances
        
        0      1652 ( 44%)
        1      2130 ( 56%)
        ```

        ***Wnioski ???***


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


### Ćwiczenie nr 4

#### Zajęcia nr 4 - Znajdowanie reguł asocjacyjnych
* [X] Zamienić atrybuty sesji na typu kategorycznego (dokonać dyskretyzacji)
* [X] Przy pomocy programu „Weka” znaleźć reguły asocjacyjne dla poszczególnych sesji. 
Weka wypluła to:
```text
Best rules found:

 1. /history/apollo/apollo-13/apollo-13-info.html=0 /history/apollo/apollo-13/=0 2859 ==> /history/apollo/apollo-13/images/=0 2855    <conf:(1)> lift:(1.03) lev:(0.02) [69] conv:(14.74)
 2. /history/apollo/apollo-13/apollo-13-info.html=0 /history/apollo/apollo-13/images/=0 2863 ==> /history/apollo/apollo-13/=0 2855    <conf:(1)> lift:(1.02) lev:(0.01) [43] conv:(5.75)
 3. /history/apollo/apollo-13/apollo-13-info.html=0 2873 ==> /history/apollo/apollo-13/images/=0 2863    <conf:(1)> lift:(1.02) lev:(0.02) [64] conv:(6.73)
 4. /software/winvn/winvn.html=0 /history/apollo/apollo-13/apollo-13-info.html=0 2848 ==> /history/apollo/apollo-13/images/=0 2838    <conf:(1)> lift:(1.02) lev:(0.02) [63] conv:(6.67)
 5. /history/apollo/apollo-13/apollo-13-info.html=0 2873 ==> /history/apollo/apollo-13/=0 2859    <conf:(1)> lift:(1.01) lev:(0.01) [37] conv:(3.46)
 6. /history/apollo/apollo-13/apollo-13-info.html=0 2873 ==> /history/apollo/apollo-13/=0 /history/apollo/apollo-13/images/=0 2855    <conf:(0.99)> lift:(1.03) lev:(0.03) [75] conv:(4.91)
 7. /history/apollo/apollo-13/images/=0 2910 ==> /history/apollo/apollo-13/=0 2890    <conf:(0.99)> lift:(1.01) lev:(0.01) [32] conv:(2.51)
 8. /software/winvn/winvn.html=0 /history/apollo/apollo-13/images/=0 2885 ==> /history/apollo/apollo-13/=0 2865    <conf:(0.99)> lift:(1.01) lev:(0.01) [32] conv:(2.48)
 9. /shuttle/missions/sts-67/mission-sts-67.html=0 2866 ==> /software/winvn/winvn.html=0 2842    <conf:(0.99)> lift:(1) lev:(-0) [0] conv:(0.96)
10. /history/apollo/apollo-13/=0 2933 ==> /software/winvn/winvn.html=0 2908    <conf:(0.99)> lift:(1) lev:(-0) [0] conv:(0.94)
```

A jak się zostawi tylko kategorie ``session_time_categories``, ``session_avarage_time_per_site_categories``,
``done_things_caegories``:

```text
Best rules found:

 1. session_average_time_per_site_categories=t<1min 1700 ==> session_time_categories=t<1min 1700    <conf:(1)> lift:(1.76) lev:(0.25) [732] conv:(732.47)
 2. session_time_categories=t<1min 1700 ==> session_average_time_per_site_categories=t<1min 1700    <conf:(1)> lift:(1.76) lev:(0.25) [732] conv:(732.47)
 3. session_average_time_per_site_categories=t<1min done_things_categories=x<=3 1080 ==> session_time_categories=t<1min 1080    <conf:(1)> lift:(1.76) lev:(0.16) [465] conv:(465.34)
 4. session_time_categories=t<1min done_things_categories=x<=3 1080 ==> session_average_time_per_site_categories=t<1min 1080    <conf:(1)> lift:(1.76) lev:(0.16) [465] conv:(465.34)
 5. session_average_time_per_site_categories=1min<=t<2min 656 ==> session_time_categories=1min<=t<2min 656    <conf:(1)> lift:(4.55) lev:(0.17) [511] conv:(511.93)
 6. session_time_categories=1min<=t<2min 656 ==> session_average_time_per_site_categories=1min<=t<2min 656    <conf:(1)> lift:(4.55) lev:(0.17) [511] conv:(511.93)
 7. session_average_time_per_site_categories=2min<=t<5min 473 ==> session_time_categories=3min<=t<5min 473    <conf:(1)> lift:(6.32) lev:(0.13) [398] conv:(398.1)
 8. session_time_categories=3min<=t<5min 473 ==> session_average_time_per_site_categories=2min<=t<5min 473    <conf:(1)> lift:(6.32) lev:(0.13) [398] conv:(398.1)
 9. session_average_time_per_site_categories=t<1min done_things_categories=3<=t<6 415 ==> session_time_categories=t<1min 415    <conf:(1)> lift:(1.76) lev:(0.06) [178] conv:(178.81)
10. session_time_categories=t<1min done_things_categories=3<=t<6 415 ==> session_average_time_per_site_categories=t<1min 415    <conf:(1)> lift:(1.76) lev:(0.06) [178] conv:(178.81)
```