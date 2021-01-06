# Ekploracja danych internetowych (Web Mining)
Przedmiot realizowany na Politechnice Łódzkiej na kierunku Informatyka Stosowana w roku akademickim 2020/2021 na studiach II stopnia. 

# Ćwiczenie nr 1

## Eksploracja użycia na podstawie pliku logów
1. Przygotować wybrany plik logów do zastosowania algorytmów eksploracji danych.
2. Wyodrębnić użytkowników i ich sesje.
3. Dokonać grupowania użytkowników.
4. Dokonać grupowania sesji.
5. Zbudować reguły asocjacyjne dla użytkowników i sesji.
6. Dokonać analizy wyników.


# Ćwiczenie nr 2
1. Użyć dowolnego programu typu crawler (np. WebSphinx) dla ściągnięcia stron z
dowolnej domeny.
2. Zapisać strony w pojedynczym pliku.
3. Przekształcić otrzymany plik do formatu „plain text”.
4. Korzystając z dowolnego narzędzia zapisać za pomocą reprezentacji: TF, TFIDF,
boolowskiej lub wykorzystać do tego celu oprogramowanie Weka w następujący sposób:
    - Plik tekstowy otrzymany jako konkatenacja stron internetowych przekształcić do formatu ``arff``, przyjmując dwa atrybuty: tytuł dokumentu, zawartość dokumentu obydwa typu string.

        Przykład takiego pliku:
        ```
        @relation dokumenty
        @attribute tytul string
        @attribute zawartosc string
        @data
        “dokument 1”, “Zawartosc tresci nr 1”
        „dokument 2”, „ Zawartosc tresci nr 2”
        ```
    - Otworzyć plik w programie „Weka”. Przekształcić pierwszy atrybut do typu nominalnego, stosując filtr StringToNominal (Choose, Filters, Unsupervised,Attribute, StringToNominal, parametr : first, Apply). Dokonać przekształcenia drugiego atrybutu do postaci wektorowej (Choose, Filters, Unsupervised, Attribute, StringToWordVector, Apply). 
    - Zbadać wynik działania ostatniej operacji, w zależności od ustawienia parametrów: IDFTransform, TFTransform, outputWordCounts, useStoplist. Wykonać analizę otrzymanej tabeli (funkcja Edit). Porównać z wynikami otrzymanymi dla reprezentacji boolowskiej (opcja NumericToBinary).
5. Dokonać analizy klastrowej dokumentów, porównać wyniki dla różnego rodzaju
atrybutów. 

# Ćwiczenie nr 3

1. Wykorzystać użytkowników z ćwiczenia nr 1. Jako atrybuty przyjąć strony na które wchodzili.
2. Losowo utworzyć użytkownika.
3. Znaleźć najbliższą mu grupę.
4. Zarekomendować mu strony, na które wchodziła większość użytkowników grupy.