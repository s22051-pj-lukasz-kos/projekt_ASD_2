# readme

# Kody Huffmana

Drugi projekt na zaliczenie Algorytmów i struktur danych (ASD) na 4 semestrze PJATK w Gdańsku. 

## Wstęp

Kody Huffmana to metoda kompresji tekstu, która zastępuje znaki o stałej długości (binarnej) na znaki o zmiennej długości. Znaki częściej występujące w tekście mają krótszy zapis binarny. W efekcie tekst zapisany tą metodą jest sumarycznie krótszy od standardowego kodowania i zajmuje mniej miejsca.

Algorytm polega na zliczaniu częstotliwości występowania poszczególnych znaków w tekście i tworzeniu na bazie tej informacji drzewa binarnego. 

Drzewo binarne składa się z węzłów reprezentowanych przez obiekt Node zawierający pola dotyczące znaków, częstotliwości występowania, lewego dziecka, prawego dziecka i wygenerowanego kodu Huffmana. 

Algorytm Huffmana wykorzystuje kolejkę priorytetową typu min do szybkiego znajdowania najmniejszych wartości. Kolejka priorytetowa typu min opiera się na koncepcji kopca binarnego typu min. 

Z kolejki wyodrębniane są dwie najmniejsze wartości (najrzadziej występujące znaki), które stanowią lewe i prawe dziecko nowego węzła. Nowy węzeł zostaje umieszczony na końcu kopca, po czym zostaje wywoływana funkcja, która przywraca własność kopca typu min. Algorytm dokonuje tych operacji do momentu gdy zostaje jeden element zawierający całą strukturę drzewa (korzeń drzewa). 

Na bazie tego elementu program wylicza kody Huffmana dla poszczególnych znaków w zależności od ‘drogi’ przebytej od korzenia do węzła reprezentującego pojedynczy znak: przejście przez lewe dziecko dodaje 0 do kodu, przejście przez prawe dziecko dodaje 1 do kodu. 

Po wygenerowaniu kodów dla poszczególnych znaków dokonujemy konwersji tekstu na ciąg binarny.

## Implementacja i spostrzeżenia

Drzewo binarne zaimplementowano jako tablicę (`list`) obiektów Node. 0 (*zerowy*) indeks tablicy służy do przechowywania wartości wielkości kopca (`heapsize`), gdyż Python nie posiada możliwości tworzenia wskaźników i musiałem znaleźć sposób, aby wzajemnie odwołujące się do siebie funkcje poza wartościami przekazywały jeszcze wiekość kopca. Uznałem, że przeznaczenie pierwszej komórki tablicy reprezentującej kopiec do tego celu jest bardziej eleganckim rozwiązaniem od zwracania tablicy wartości przy każdym `return`. 

W celu sortowania drzewa posłużono się kolejką prorytetową typu min oraz algorytmami na przywracanie własności kopca typu min. Ich implementacja wymagała odwoływania się do pól węzła (Node) więc kod nie jest uniwersalny i nie zadziała np. na tabeli liczb Integer. 

Na samym początku pliku wynikowego w sposób jawny został zapisany słownik znaków (kody Huffmana).

Potem przy pomocy tego słownika przekonwertowano zawartość pliku źródłowego na ciąg binarny. Z racji tego, że ten ciąg był typu String, należało go przekonwertować do ciągu bajtów. Do tego celu służy funkcja bytes(data). Dopiero tak przygotowane dane można było zapisać binarnie do pliku wyjściowego.