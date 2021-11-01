
# Dokumantácia

Autory: Matej Berezný, Ondrej Valo, Švenk Adam

Login: xberez03, xvaloo00, xsvenk00

## Popis dátových sád
Dáta sú čítané z neskôr uvedených zdrojov a ukladané pomocou MongoDB na zadarmo hosťovaný klaster, kde sú údaje uložené v dokumentoch BSON (binárny JSON) s dynamickou schémou. 
Dátové sady boli získane z:
https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19
https://data.gov.cz/datov%C3%A9-sady?dotaz=covid-19
### COVID-19: Prehľad osôb s potvrdenou nákazou podľa hlásenia krajských hygienických staníc
**Popis:**
Dátová sada obsahujúca na základe denní incidenčný prehľad osôb s preukázanou nákazou COVID-19 podľa hlásenia krajských hygienických staníc.

**Schéma:**
| stĺpec | dátový typ | význam |
|--|--|--|
| datum: | date | dátum dňa potvrdenia ochorenia  |
| vek: | integer | vek osoby |
| pohlavi: | string | pohlavie osoby |
| kraj_nuts_kod: | string | kód kraja bydliska osoby |
| okres_lau_kod: | string | kód okresu bydliska osoby |
| nakaza_v_zahranici: | boolean | osoba sa nakazila v zahraničí |
| nakaza_zeme_csu_kod: | string | Krajina kde sa osoba nakazila |

### COVID-19: Prehľad vyliečených podľa hlásenia krajských hygienických staníc
**Popis:**
Dátová sada obsahujúca záznamy o vyliečených po ochorení COVID‑19 podľa hlásenia krajských hygienických staníc.

**Schéma:**
| stĺpec | dátový typ | význam |
|--|--|--|
| datum: | date | dátum dňa potvrdenia vyliečenia ochorenia  |
| vek: | integer | vek osoby |
| pohlavi: | string | pohlavie osoby |
| kraj_nuts_kod: | string | kód kraja bydliska osoby |
| okres_lau_kod: | string | kód okresu bydliska osoby |

### COVID-19: Prehľad úmrtí podľa hlásenia krajských hygienických staníc
**Popis:**
Dátová sada obsahujúca záznamy o úmrtiach v súvislosti s ochorením COVID‑19 podľa hlásenia krajských hygienických staníc. Zahŕňa úmrtie osôb, ktoré boli pozitívne testované na COVID‑19 (metódou PCR) bez ohľadu na to, aké boli príčiny ich úmrtia, a ku ktorých úmrtiu došlo v rámci hospitalizácie alebo mimo nej.

**Schéma:**
| stĺpec | dátový typ | význam |
|--|--|--|
| datum: | date | dátum dňa potvrdenia úmrtia  |
| vek: | integer | vek osoby |
| pohlavi: | string | pohlavie osoby |
| kraj_nuts_kod: | string | kód kraja bydliska osoby |
| okres_lau_kod: | string | kód okresu bydliska osoby |

### COVID-19: Prehľad hospitalizovaných
**Popis:**
Dátová sada obsahujúca dáta hospitalizovaných pacientov popisujúca priebeh hospitalizácie (aktuálny a celkový počet hospitalizovaných, rozdelenie podľa príznakov, rozdelenie podľa podporných prístrojov, počet úmrtí).

**Schéma:**
| stĺpec | dátový typ | význam |
|--|--|--|
| datum: | date | dátum dňa potvrdenia vyliečenia ochorenia  |
| pacient_prvni_zaznam: | integer | prvý krát hospitalizovaný |
| kum_pacient_prvni_zaznam: | integer | kumulatívny počet prvý krát hospitalizovaných |
| pocet_hosp: | integer | celkový počet hospitalizovaných |
| stav_bez_priznaku: | integer | hospitalizovaný bez príznakov |
| stav_lehky: | integer | hospitalizovaný s ľahkými príznakmi |
| stav_stredni: | integer | hospitalizovaný s strednými príznakmi |
| stav_tezky: | integer | hospitalizovaný s závažnými príznakmi |
| jip: | integer | hospitalizovaný na jednote intenzívneho opatrenia |
| kyslik: | integer | hospitalizovaný na lôžkach vybavených zdrojom kyslíka |
| hfno: | integer | hospitalizovaný na lôžku s oxygenátorom(High-Flow Nasal Oxygen) |
| upv: | integer | umelá pľúcna ventilácia |
| ecmo: | integer | mimotelový obeh pre náhradu funkcie pľúc |
| tezky_upv_ecmo: | integer | ťažký prípad z nasadením ecmo a upv |
| umrti: | integer | počet úmrtí hospitalizovaných |
| kum_umrti: | integer |kumulatívny počet počet úmrtí hospitalizovaných |

### COVID-19: Prehľad epidemiologickej situácie podľa hlásenia krajských hygienických staníc podľa okresu
**Popis:**
Dátová sada podľa krajov a okresov ČR obsahujúca kumulatívne denné počty osôb s preukázaným ochorením COVID-19 podľa validovaných hlásení krajských hygienických staníc, kumulatívne denné počty vyliečených po ochorení COVID-19 podľa hlásenia krajských hygienických staníc a kumulatívne denné počty úmrtí v súvislosti s ochorením COVID 19 podľa hlásenia krajských hygienických staníc a hospitalizačných úmrtí.

**Schéma:**
| stĺpec | dátový typ | význam |
|--|--|--|
| datum: | date | dátum dňa údajov |
| kraj_nuts_kod: | string | kód kraja bydliska osoby |
| okres_lau_kod: | string | kód okresu bydliska osoby |
| kumulativni_pocet_nakazenych: | integer | kumulatívny počet nakazených v okrese |
| kumulativni_pocet_vylecenych: | integer | kumulatívny počet vyliečených v okrese |
| kumulativni_pocet_umrti: | integer | kumulatívny počet úmrtí v okrese |

## Implementácia riešenia
### dataset.py
Obsahuje potrebné funkcie pre prácu k dátovým sadám a dátami ako napríklad stiahnutie dát a ich následné vkladanie do databázy, parsovanie dát, alebo ich mazanie.
### download.py
Pracuje s funkciami v *dataset.py* a interaguje s databázou. Príklad na spustenie:
**python3 download.py**
rgumenty:
    **-u**, **--update** Aktualizuje zadanú kolekciu v db. Na aktualizáciu každej kolekcie použite „všetky“.
	**-d**, **--download** Vymaže databázu a stiahne množiny údajov uložené v súbore datasets.json
	**-c**, **--clear** Vymaže databázu
	**-s**, **--fetch** Načíta zadanú kolekciu z db

### setup.sh
Skript na stiahnutie potrebných knižníc a závislostí pre fungovanie riešenia
### datasets.json
Obsahuje potrebné linky na stiahnutie dátových sád.