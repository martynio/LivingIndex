# LIVING INDEX (LI)
## Project Proposal v1.0 — Ekonomia pieniędzy i czasu

**Identyfikator:** LI-PP-001  
**Data:** 9 listopada 2026  
**Status:** Propozycja projektowa do akceptacji; nie jest zgodą na implementację  
**Etap:** DISCUSS → RESEARCH  
**Branding:** Samodzielny, na razie anonimowy produkt; możliwość późniejszego oznaczenia MartynForge  
**Języki interfejsu:** polski (PL), angielski (EN), niderlandzki (NL)

---

## 1. Streszczenie projektu

**Living Index (LI)** to publiczna, lekka i responsywna aplikacja internetowa umożliwiająca analizę historycznych kosztów życia, dochodów, siły nabywczej oraz czasu pracy potrzebnego do sfinansowania codziennych wydatków. W pierwszej odsłonie użytkownik wybiera kraj i rok, a następnie widzi czytelny wykres ekonomicznego bilansu życia. Interfejs ma być prosty od pierwszego kontaktu, a szczegółowe scenariusze i wyjaśnienia — dostępne na żądanie.

Projekt powstał z potrzeby weryfikowania popularnych przekonań: „za granicą żyje się zawsze lepiej”, „poprzednim pokoleniom było łatwiej/trudniej” czy „wystarczy więcej pracować”. LI nie ma potwierdzać żadnej z tych tez z góry. Ma pokazywać dane, ich definicje, źródła i granice porównywalności.

**Główna obietnica:** porównuj nie tylko, ile kosztuje życie, ale także ile *czasu pracy* trzeba na nie przeznaczyć — z wyraźnym oddzieleniem faktów, obliczeń i braków danych.

## 2. Problem i grupy odbiorców

### Problem
- Porównania krajów opierają się często na wyrwanych z kontekstu kwotach, kursach walut lub pojedynczych przeciętnych.
- Dyskusje międzypokoleniowe pomijają różnice w wynagrodzeniach, cenach, dostępie do dóbr i sytuacji na rynku pracy.
- Popularne wykresy budżetowe rzadko pokazują koszty w godzinach pracy, a jeszcze rzadziej ujawniają niepewność danych.

### Odbiorcy
- Osoby rozważające emigrację lub powrót do kraju.
- Osoby porównujące swoją sytuację z sytuacją wcześniejszych pokoleń.
- Pracownicy i rodziny zainteresowane realną siłą nabywczą.
- Odbiorcy edukacji ekonomicznej, dziennikarze i osoby prowadzące publiczne dyskusje o kosztach życia.

### Podstawowe pytania użytkownika
1. Ile kosztował podstawowy koszyk życia w wybranym kraju i roku?
2. Jaka część typowego wynagrodzenia była potrzebna na jego pokrycie?
3. Ile godzin płatnej pracy odpowiadało tym kosztom?
4. Jak zmieniły się te proporcje między dwoma latami, krajami lub profilami — **tylko jeśli dane są porównywalne**?
5. Jak mieszkańcy oceniali zadowolenie z życia, gdy dostępne są wiarygodne badania?

## 3. Zasady produktu

1. **Najpierw prostota:** kraj + rok + podstawowy wykres na ekranie głównym; rozbudowane filtry w panelu „Szczegóły”.
2. **Średnie jako widok domyślny, nie prawda o każdej osobie:** nazwy populacji, miary (średnia/mediana) i zakresu danych są zawsze widoczne.
3. **Neutralność analityczna:** bez automatycznego wskazywania „najlepszego kraju” lub „lepszego pokolenia”.
4. **Brak wymyślanych danych:** braki pozostają brakami; nie interpolujemy milcząco kosztów życia.
5. **Metodologia obok wykresu:** źródło, rok, jednostka, definicja, status, przekształcenia i data pozyskania.
6. **Porównywalność ważniejsza niż efektowność:** nie zestawiamy bez ostrzeżenia wielkości brutto z netto, różnych populacji ani różnych metod badań.
7. **Stopniowy rozwój:** najpierw Polska i Holandia, później kolejne kraje i głębsze modele.
8. **Dostępność i szybkość:** priorytet dla smartfonu, prostych filtrów, czytelnych etykiet i obsługi klawiaturą.

## 4. Zakres funkcjonalny pierwszej wersji (MVP)

### 4.1 Ekran główny
- Wybór kraju: **Polska / Holandia**.
- Wybór roku: wyłącznie rok lub zakres, dla którego istnieją odpowiednie dane; brak gwarancji pełnego pokrycia 1980–2026.
- Domyślny, jasno nazwany scenariusz statystyczny oparty na średnich; profil nie może sugerować, że średnia pensja pojedynczego pracownika jest średnim dochodem całego gospodarstwa.
- Wykres miesięcznego podziału kosztów życia (kategorie tylko tam, gdzie są wiarygodne dane), wartość łączna, relacja do dochodu i ewentualna kwota pozostała.
- Przełączenie jednostki: **waluta lokalna / ekwiwalent godzin pracy**.
- Sekcja z rzeczywistym wskaźnikiem zadowolenia z życia, o ile istnieje porównywalne badanie dla wybranego kraju i roku.
- Ikony ostrzeżeń pod wykresem, rozwijające uzasadnienie metodologiczne lub kontekst historyczny.
- Wskazanie źródeł, daty aktualizacji i zakresu danych.

### 4.2 Porównania
- **Kraj ↔ kraj** przy tym samym roku, gdy wskaźniki są zgodne metodologicznie.
- **Rok ↔ rok** w tym samym kraju.
- Czytelne zaznaczanie nieporównywalnych wskaźników lub braków, zamiast udawania spójności.
- Dwa scenariusze widoczne obok siebie na większych ekranach, jeden pod drugim na telefonach.

### 4.3 Szczegóły bez przeciążania interfejsu
- Panel „Rozwiń analizę” przewidziany na dodatkowe ustawienia.
- Pierwsze filtry: źródło/typ wynagrodzenia, dostępne profile oraz najem/własność **tylko po potwierdzeniu, że istnieją dane pozwalające na poprawne wyliczenie**.
- Segment wieku (np. 25 vs 50 lat), rodzinny budżet oraz różne źródła dochodu są wymaganiami docelowymi; ich udostępnienie w MVP zależy od wyniku audytu danych.
- Brak przełącznika, który dawałby pozornie precyzyjne wyniki z nieistniejących danych.

### 4.4 Udostępnianie
- Stały link zawierający ustawienia porównania, ale **bez prywatnych danych użytkownika**.
- Eksport widocznego wykresu do PNG.
- Podpis eksportu: Living Index, nazwy porównywanych miejsc i lat, źródło, rodzaj miary, data zestawu danych i czytelne zastrzeżenia metodologiczne; link do pełnej metodologii.

### 4.5 Języki
- Pełny interfejs PL/EN/NL od pierwszej publikacji.
- Nazwy wskaźników i ostrzeżenia tłumaczone spójnie; nie tłumaczymy mechanicznie nazw źródłowych ani nie zmieniamy znaczenia statystyk.

## 5. Ekonomia pieniędzy i czasu: model interpretacji

### 5.1 Bilans finansowy
- Koszty są wyświetlane w walucie właściwej dla kraju i roku (z uwzględnieniem zmian waluty i denominacji, np. PLN w 1995 r. oraz EUR w Holandii od 2002 r.).
- Kategorie docelowe: mieszkanie, żywność, energia/media, transport, zdrowie, inne koszty podstawowe. Pokrycie i definicje są uzależnione od rzeczywistych źródeł.
- **Dochód netto, wynagrodzenie brutto, dochód rozporządzalny gospodarstwa i średnia płaca pracownika to różne pojęcia.** Nie wolno stosować ich zamiennie.
- Kwota „pozostaje” pojawia się wyłącznie przy zdefiniowanym, zgodnym koszyku i dochodzie. Bez tych warunków system prezentuje koszty i zarobki osobno.

### 5.2 Czas pracy
- Dla scenariusza ze zdefiniowanym dochodem netto i czasem płatnej pracy:  
  **stawka netto za godzinę = miesięczny dochód netto z pracy / liczba płatnych godzin pracy w miesiącu**;  
  **godziny wymagane na wydatek = kwota wydatku / stawka netto za godzinę**.
- Wyliczenie jest **ekwiwalentem zarobkowym**, nie automatyczną oceną czasu rzeczywiście spędzonego w pracy.
- Gdy dostępne jest tylko wynagrodzenie brutto, nie wolno przedstawiać wyniku jako netto-godzin wystarczających do opłacenia wydatków. Możliwy jest odrębnie oznaczony wskaźnik brutto lub brak wyliczenia.
- Późniejsza analiza rozszerzona: dojazdy, odległość, korki, kolejki, nieodpłatne obowiązki, czas wolny. Zależna od dostępności historycznych danych i ręcznie określonych scenariuszy.

### 5.3 Porównania między krajami
- Domyślny obraz to **lokalne ceny i lokalne zarobki**.
- Do szerszego porównania siły nabywczej można użyć poprawnie dobranych miar PPP; kurs rynkowy nie jest uniwersalną miarą kosztów życia.
- Nie sumujemy koszyków z odmiennymi definicjami bez osobnego wyjaśnienia.

### 5.4 Historyczne uwarunkowania
- Ostrzeżenia mogą wskazywać np. reglamentację, niedobory, zmianę systemu gospodarczego, denominację, zmiany metodologii czy ograniczenie dostępności dóbr.
- Gdy dane o czasie oczekiwania lub dostępności produktu są niewiarygodne, pokazujemy **kontekst tekstowy**, a nie dopisujemy szacunkowych godzin do wykresu.

## 6. Zadowolenie z życia i przyszły indeks LI

### Priorytet A — pomiar rzeczywisty
- Ankiety prowadzone przez uznane instytucje: odsetek osób deklarujących zadowolenie **albo** średnia ocena na skali np. 0–10, zgodnie z definicją źródła.
- Wynik skali 0–10 **nie jest procentem**. Nie przeliczamy go automatycznie na „procent zadowolonych”.
- Dostępne podziały (wiek, dochód, kraj) pokazujemy tylko w zakresie rzeczywiście zbadanym.
- Użytkownik może zmieniać scenariusz ekonomiczny, lecz **nie może zmienić wyniku ankiety przez ustawienie wag**.

### Priorytet B — model obliczany (poza MVP)
- Autorski, eksperymentalny indeks warunków życia, np. uwzględniający budżet, dostępność dóbr oraz czas.
- Publiczna definicja, normalizacja, wagi, badanie wrażliwości i rozdzielenie od danych ankietowych.
- Może być wizytówką projektu dopiero po walidacji. Nie wolno nazywać go „realnym zadowoleniem ludzi”.

## 7. Geografia, historia i plan rozwoju

**Kolejność krajów:** 1) Holandia i Polska; 2) Niemcy; 3) Wielka Brytania; 4) Francja; 5) USA; 6) Kanada; 7) Zjednoczone Emiraty Arabskie.

**Ambicja historyczna:** docelowo lata **1980–ostatni kompletny okres**, ale zakres jest ustalany **oddzielnie dla kraju i wskaźnika**. Historyczne CPI nie dowodzi dostępności historycznego koszyka, wynagrodzenia netto ani zadowolenia z życia.

**Rozszerzenia funkcjonalne, bez obietnicy terminu:** segmenty wieku, struktura gospodarstw, zakup vs najem, emigracja z dwoma perspektywami (typowa lokalna sytuacja oraz hipotetyczna przeprowadzka), rozszerzony bilans czasu, trend historyczny, dalsze państwa, artykuły o specyfice życia i pracy.

## 8. Dane, źródła i pochodzenie informacji

### 8.1 Wstępnie sprawdzone oficjalne źródła — stan rozpoznania 9.11.2026

| Instytucja / zbiór | Co potwierdza | Ograniczenie |
|---|---|---|
| CBS: CPI 1900=100, `71905ned` | Holenderska, łączona historyczna seria cen od 1900 r. | Przybliżony łańcuch serii, a nie kompletny koszyk wydatków. |
| GUS: przeciętne wynagrodzenie 1950–2025 | Historyczna średnia płaca w polskiej gospodarce. | Nie jest to pensja netto, mediana ani dochód gospodarstwa. |
| OECD: Average annual wages | Wskaźnik płac w przeliczeniu na pełny etat, porównywalny według metod OECD. | Średnia, nie mediana i nie dochód do dyspozycji. |
| Eurostat: EU-SILC `ilc_pw01` | Wyniki ankietowego zadowolenia z życia na skali 0–10, m.in. rok 2022. | Nie należy zakładać rocznej, kompletnej serii od 1980 r. |
| CBS: Trends in geluk en tevredenheid | Historyczne odsetki zadowolonych dorosłych, m.in. 1997–2018. | Definicja i skala mogą różnić się od badań Eurostatu. |
| Eurostat: API | Publiczny dostęp programistyczny do danych i metadanych. | Aktualne zbiory mogą być korygowane; potrzebne migawki/wersjonowanie. |

**Źródła i odnośniki:**
1. CBS historyczne CPI: https://www.cbs.nl/nl-nl/cijfers/detail/71905NED
2. CBS API/dataset: https://dataportal.cbs.nl/detail/CBS/71905ned
3. GUS wynagrodzenia 1950–2025: https://stat.gov.pl/obszary-tematyczne/rynek-pracy/pracujacy-zatrudnieni-wynagrodzenia-koszty-pracy/przecietne-miesieczne-wynagrodzenie-w-gospodarce-narodowej-w-latach-1950-2025,2,1.html
4. OECD Average annual wages: https://www.oecd.org/en/data/indicators/average-annual-wages.html
5. Eurostat satysfakcja 2022, `ilc_pw01`: https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20240115-1
6. CBS satysfakcja 1997–2018: https://www.cbs.nl/nl-nl/longread/statistische-trends/2019/trends-in-geluk-en-tevredenheid/tabellenbijlage
7. Eurostat API: https://ec.europa.eu/eurostat/en/web/user-guides/data-browser/api-data-access/api-introduction

### 8.2 Obowiązkowa karta każdego wskaźnika
- Źródło i bezpośredni identyfikator danych.
- Kraj/region, okres, badana populacja i jednostka.
- Typ miary: nominalna/realna, brutto/netto, średnia/mediana, ankietowa/modelowana.
- Definicja koszyka lub kategorii; zakres uwzględnionych i wyłączonych kosztów.
- Metoda transformacji i jej wersja.
- Data odczytu, data publikacji, status rewizji.
- Status jakości: **źródłowe**, **przetworzone/rekonstruowane**, **niedostępne/nieporównywalne**; kolor uzupełniony tekstem i symbolem.
- Uprawnienia/licencja na publikację i wymagania atrybucji — sprawdzane w RESEARCH.

### 8.3 Zasady aktualizacji
- Import ręczny lub półautomatyczny, walidacja i kontrola operatora przed publikacją.
- Osobne przechowanie surowych migawek danych i wersji wyprowadzonych wskaźników.
- Aktualizacja nie może bez śladu zmieniać historycznych wyników udostępnionych linkami.
- Zmiana metodologii źródła wywołuje ponowną ocenę porównywalności (np. CBS zmienił bazę CPI na 2025=100 i klasyfikację od 2026 r.).

## 9. Architektura wstępna — do oceny po RESEARCH

**Warstwa prezentacji:** semantyczny HTML, Bootstrap 5+, Pinegrow, lekki JavaScript i Chart.js.  
**Warstwa danych:** wersjonowane JSON-y o jawnej strukturze, rozdzielone od kodu UI.  
**Hosting:** statyczny hosting, bez wymaganego serwera aplikacyjnego w MVP.  
**Lokalizacja:** PL/EN/NL, niezależne słowniki tłumaczeń.  
**Eksport:** PNG i URL z jawnym opisem metadanych zestawu.  
**Prywatność:** brak kont i gromadzenia prywatnych budżetów w MVP; scenariusze użytkownika nie są przesyłane do usługi analitycznej.

Istotne ograniczenie: struktura danych i rozdzielenie źródeł od wyliczeń mają umożliwiać późniejsze API i bazę danych, ale **nie uzasadniają tworzenia backendu w MVP**. Dokładny projekt techniczny powstaje dopiero po audycie danych i repozytorium.

## 10. Granice zakresu (Out of Scope dla MVP)

- Konta, logowanie, zapisywanie prywatnych profili na serwerze.
- „Ocena, gdzie żyje się najlepiej” lub automatyczne werdykty polityczne i pokoleniowe.
- Autorski syntetyczny wskaźnik zadowolenia (B).
- Artykuły o kulturze pracy i stylu życia.
- Pełny historyczny model kolejek, korków, opieki nad dziećmi i obowiązków domowych.
- Szczegółowy model kredytów hipotecznych, cen zakupu nieruchomości i akumulacji majątku.
- Wszystkie kraje poza PL/NL; dalsza ekspansja dopiero etapowo.
- Obietnica kompletnego okresu 1980–2026 dla każdego wskaźnika.
- Backend, AI, prognozowanie, automatyczne „uzupełnianie luk”, scraping bez oceny warunków prawnych.

## 11. Weryfikacja, mierniki i kryteria akceptacji MVP

MVP jest gotowe do demonstracji/publicznego pilota, gdy:

1. Ekran główny pozwala szybko wybrać PL/NL i dostępny rok; lata nieobsługiwane są jasno rozpoznawalne.
2. Podstawowe wykresy przedstawiają wyłącznie dane o opisanych źródłach, populacji i definicjach.
3. Użytkownik potrafi porównać dwa poprawne scenariusze; niekompatybilne przypadki są zablokowane lub oznaczone.
4. Godziny pracy są wyliczane wyłącznie z właściwie zdefiniowanej stawki i podanych godzin pracy; brak mylenia brutto z netto.
5. Rzeczywista satysfakcja z życia zachowuje źródłową skalę i definicję, a w razie braku danych ma stan „brak danych”.
6. Każde ostrzeżenie da się otworzyć, a każda użyta liczba prowadzi do śladu źródła.
7. Link odtwarza ten sam scenariusz w ramach określonej wersji danych lub jawnie informuje o zmianie wersji.
8. Eksport PNG zawiera tytuł, jednostki, lata, etykiety źródłowe i ostrzeżenia istotne dla interpretacji.
9. Interfejs PL/EN/NL jest spójny i responsywny; wykres posiada dostępną alternatywę tabelaryczną.
10. Przechodzą testy transformacji, obliczeń, braków danych, porównań, tłumaczeń i funkcji eksportu; krytyczne błędy metodologiczne = blokada publikacji.

**Cele niefunkcjonalne do weryfikacji:** szybki pierwszy ekran na średnim smartfonie, obsługa klawiaturą, czytelny kontrast i standard WCAG 2.2 AA jako cel projektowy. Konkretne limity wydajności zostaną ustalone po prototypie i pomiarach, nie deklarowane bez testów.

## 12. Główne ryzyka i zabezpieczenia

| Ryzyko | Sposób ograniczenia |
|---|---|
| Brak kompletnego koszyka historycznego dla PL/NL | Audyt zakresu danych przed implementacją; częściowe wykresy bez imputacji. |
| Nieporównywalne dochody i ceny | Jawne definicje, jednostki i blokady błędnych zestawień. |
| Pomylenie wyniku ankiety z autorskim indeksem | Oddzielne moduły A i B; priorytet A. |
| Średnia maskuje nierówności | Widoczne etykiety średniej; mediana i przedziały w kolejnych iteracjach. |
| Gospodarstwo domowe ≠ jeden pracownik | Odmiennie modelowane i oznaczane jednostki analizy. |
| Historyczne niedobory i zmiany walut | Ostrzeżenia kontekstowe, poprawne jednostki i daty. |
| Korekty danych i zmiany API | Migawki, wersjonowanie, testy regresyjne i nadzór operatora. |
| Nieczytelny ekran | Zasada jednej głównej wizualizacji + rozwijane szczegóły. |
| Prawa do redystrybucji danych | Audyt licencji i zasad atrybucji przed publikacją. |

## 13. Plan etapów i bramki decyzyjne

| Etap | Rezultat | Warunek przejścia |
|---|---|---|
| **DISCUSS — obecny** | Project Proposal v1.0 | Akceptacja definicji produktu i granic zakresu. |
| **RESEARCH** | Matryca danych PL/NL (wskaźnik × rok × źródło × jakość), legalność użycia, definicje | Minimum jeden wiarygodny, spójny scenariusz bazowy dla każdego kraju; uczciwie określony zakres porównań. |
| **DECIDE** | Zatwierdzenie szczegółowego MVP, schematu danych, kontraktu wyliczeń i kryteriów DONE | Brak niezamkniętych krytycznych konfliktów metodologicznych. |
| **REPO CHECK** | Audyt branchy, historii, struktury, zmian i testów | Bezpieczna baza implementacji i checkpoint. |
| **EXECUTE** | Minimalna strona, dane, wykresy, linki, eksport | Realizacja tylko zatwierdzonego zakresu. |
| **VERIFY** | Testy, audyt źródeł, porównania, poprawność eksportu, UX | PASS lub jawne ISSUES z blokadą wydania. |
| **COMMIT / RELEASE GATE** | Zweryfikowany checkpoint i decyzja publikacyjna | Publikacja dopiero po akceptacji operatora. |

Nie ustalono sztywnych terminów ani kosztorysu. Decyzja o rozpoczęciu implementacji nie wynika automatycznie z przyjęcia Proposal.

## 14. Decyzje uzgodnione i pytania badawcze

### Uzgodnione
- Nazwa **Living Index (LI)**.
- Publiczne, neutralne narzędzie, na początku bez oznaczeń MartynForge.
- PL/EN/NL; technologia zgodna ze standardem MartynForge.
- Polska i Holandia jako pierwsze kraje.
- Widok oparty na średnich, z opcjami rozwijanymi.
- Prawdziwe badania zadowolenia z życia jako priorytet.
- Stopniowy rozwój, bez backendu w MVP, linki do porównań i PNG.
- Rzetelność, jawne braki danych, ostrzeżenia i brak pojedynczej oceny „najlepszego kraju”.

### Do rozstrzygnięcia na etapie RESEARCH — nie są nowymi pytaniami o wizję
- Jakie dokładnie historyczne **kategorie wydatków** da się uzyskać dla PL i NL, w jakich latach i według jakich definicji?
- Czy istnieją porównywalne szeregi historycznych **dochodów netto** i godzin pracy wystarczające do publikacji wskaźnika czasu?
- Jakie lata i podziały są dostępne w wiarygodnych **badaniach ankietowych satysfakcji**?
- Jak liczyć i prezentować koszyk podstawowy bez fałszywego sugerowania, że oznacza średni budżet jednej realnej osoby?
- Jakie licencje, atrybucje i zasady aktualizacji obowiązują dla konkretnych źródeł?

---

### Ostateczna definicja sukcesu

**Living Index odnosi sukces, jeżeli użytkownik w ciągu kilkunastu sekund potrafi zobaczyć użyteczny, poprawnie opisany obraz kosztów życia w wybranym kraju i roku, a następnie samodzielnie odkryć, skąd wzięły się liczby, jakie mają ograniczenia oraz jak ich finansowy ciężar przekłada się na czas pracy — bez przedstawiania braków i szacunków jako faktów.**

**Najbliższa praca po zaakceptowaniu dokumentu:** RESEARCH / Data Feasibility Matrix PL–NL. **Nie** implementacja ani TASK dla Codexa.