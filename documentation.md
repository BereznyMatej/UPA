
# Dokumantácia

Autory: Matej Berezný, Ondrej Valo, Švenk Adam

Login: xberez03, xvaloo00, xsvenk00

## Popis dátových sád
<<<<<<< HEAD
Dáta sú čítané z neskôr uvedených zdrojov a ukladané pomocou MongoDB na zadarmo hosťovaný klaster, kde sú údaje uložené v dokumentoch BSON (binárny JSON) s dynamickou schémou. 
Dátové sady boli získane z:
https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19m
=======
>>>>>>> documentation: Added description about more data sets
### COVID-19: Prehľad osôb s potvrdenou nákazou podľa hlásenia krajských hygienických staníc
**Popis:**
Dátová sada obsahuje denní prehľad osôb s preukázanou nákazou COVID-19 podľa hlásenia krajských hygienických staníc.

**Schéma:**
| stĺpec | dátový typ | význam |
|--|--|--|
<<<<<<< HEAD
| id: | string | identifikačný reťazec  |
| datum: | string | dátum dňa potvrdenia ochorenia  |
=======
| datum: | date | dátum dňa potvrdenia ochorenia  |
>>>>>>> documentation: Added description about more data sets
| vek: | integer | vek osoby |
| pohlavi: | string | pohlavie osoby |
| kraj_nuts_kod: | string | kód kraja bydliska osoby |
| okres_lau_kod: | string | kód okresu bydliska osoby |
| nakaza_v_zahranici: | boolean | osoba sa nakazila v zahraničí |
| nakaza_zeme_csu_kod: | string | Krajina kde sa osoba nakazila |
| reportovano_khs: | boolean | reportované krajskej hygienickej stanici |

### COVID-19: Prehľad vyliečených podľa hlásenia krajských hygienických staníc
**Popis:**
Dátová sada obsahujúca záznamy o vyliečených osobách po ochorení COVID‑19 podľa hlásenia krajských hygienických staníc.

**Schéma:**
| stĺpec | dátový typ | význam |
|--|--|--|
| id: | string | identifikačný reťazec  |
| datum: | string | dátum dňa potvrdenia vyliečenia ochorenia  |
| vek: | integer | vek osoby |
| pohlavi: | string | pohlavie osoby |
| kraj_nuts_kod: | string | kód kraja bydliska osoby |
| okres_lau_kod: | string | kód okresu bydliska osoby |

### COVID-19: Prehľad úmrtí podľa hlásenia krajských hygienických staníc
**Popis:**
Dátová sada obsahuje záznamy o úmrtiach v súvislosti s ochorením COVID‑19 podľa hlásenia krajských hygienických staníc. Zahŕňa úmrtie osôb, ktoré boli pozitívne testované na COVID‑19 (metódou PCR) bez ohľadu na to, aké boli príčiny ich úmrtia, a ku ktorých úmrtiu došlo v rámci hospitalizácie alebo mimo nej.

**Schéma:**
| stĺpec | dátový typ | význam |
|--|--|--|
| id: | string | identifikačný reťazec  |
| datum: | string | dátum dňa potvrdenia úmrtia  |
| vek: | integer | vek osoby |
| pohlavi: | string | pohlavie osoby |
| kraj_nuts_kod: | string | kód kraja bydliska osoby |
| okres_lau_kod: | string | kód okresu bydliska osoby |

### COVID-19: Prehľad hospitalizovaných
**Popis:**
Dátová sada obsahuje informácie o hospitalizovaných pacientoch, a popisuje priebeh hospitalizácie (aktuálny a celkový počet hospitalizovaných, rozdelenie podľa príznakov, rozdelenie podľa podporných prístrojov, počet úmrtí).

**Schéma:**
| stĺpec | dátový typ | význam |
|--|--|--|
| id: | string | identifikačný reťazec  |
| datum: | string | dátum dňa potvrdenia vyliečenia ochorenia  |
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
Dátová sada obsahuje kumulatívne denné počty osôb s preukázaným ochorením COVID-19 v krajoch a okresoch ČR. Hlásenia boli validované krajskými hygienickými stanicami.

**Schéma:**
| stĺpec | dátový typ | význam |
|--|--|--|
<<<<<<< HEAD
| id: | string | identifikačný reťazec  |
| datum: | string | dátum dňa údajov |
=======
| datum: | date | dátum dňa potvrdenia vyliečenia ochorenia  |
| vek: | integer | vek osoby |
| pohlavi: | string | pohlavie osoby |
>>>>>>> documentation: Added description about more data sets
| kraj_nuts_kod: | string | kód kraja bydliska osoby |
| okres_lau_kod: | string | kód okresu bydliska osoby |
| kumulativni_pocet_nakazenych: | integer | kumulatívny počet nakazených v okrese |
| kumulativni_pocet_vylecenych: | integer | kumulatívny počet vyliečených v okrese |
| kumulativni_pocet_umrti: | integer | kumulatívny počet úmrtí v okrese |

### COVID-19: Prehľad hospitalizácií na JIP s ohľadom na vykázané očkovania
**Popis:**
Dátová sada obsahuje počet, percento a priemerný vek osôb hospitalizovaných na jednotke intenzívnej starostlivosti (JIP). Každý riadok udáva súhrnné údaje osôb v daný deň rozdelených do skupín podľa stavu očkovanosti: bez očkovania, s nedokončeným očkovaním, s dokončeným očkovaním alebo s dokončeným očkovaním vrátane posilňujúcej dávky.

**Schéma:**
| stĺpec | dátový typ | význam |
|--|--|--|
| id: | string | identifikačný reťazec  |
| datum: | string | dátum dňa údajov |
| jip_celkem: | integer | celkový počet osôb na JIP |
| jip_bez_ockovani: | integer | počet neočkovaných osôb na JIP |
| jip_bez_ockovani_relativni_pocet: | number | počet neočkovaných osôb ku celkovému počtu na JIP |
| jip_bez_ockovani_vek_prumer: | integer | vekový priemer neočkovaných osôb na JIP |
| jip_nedokoncene_ockovani: | integer | počet očkovaných osôb s 1 dávkou na JIP |
| jip_nedokoncene_ockovani_relativni_pocet: | number | počet očkovaných osôb s 1 dávkou ku celkovému počtu na JIP |
| jip_nedokoncene_ockovani_vek_prumer: | integer | vekový priemer očkovaných osôb s 1 dávkou na JIP |
| jip_dokoncene_ockovani: | integer | počet očkovaných osôb s 2 dávkou na JIP |
| jip_dokoncene_ockovani_relativni_pocet: | number | počet očkovaných osôb s 2 dávkou ku celkovému počtu na JIP |
| jip_dokoncene_ockovani_vek_prumer: | integer | vekový priemer očkovaných osôb s 2 dávkou na JIP |
| jip_posilujici_davka: | integer | počet očkovaných osôb s 3 dávkou na JIP |
| jip_posilujici_davka_relativni_pocet: | number | počet očkovaných osôb s 3 dávkou ku celkovému počtu na JIP |
| jip_posilujici_davka_vek_prumer: | integer | vekový priemer očkovaných osôb s 3 dávkou na JIP |

### COVID-19: Prehľad hospitalizácií s ohľadom na vykázané očkovania
**Popis:**
Dátová sada obsahuje počet, percento a priemerný vek hospitalizovaných osôb. Každý riadok udáva súhrnné údaje osôb v daný deň rozdelených do skupín podľa stavu očkovanosti: bez očkovania, s nedokončeným očkovaním, s dokončeným očkovaním alebo s dokončeným očkovaním vrátane posilňujúcej dávky.

**Schéma:**
| stĺpec | dátový typ | význam |
|--|--|--|
| id: | string | identifikačný reťazec  |
| datum: | string | dátum dňa údajov |
| hospitalizovani_celkem: | integer | celkový počet hospitalizovaných osôb |
| hospitalizovani_bez_ockovani: | integer | počet hospitalizovaných neočkovaných osôb |
| hospitalizovani_bez_ockovani_relativni_pocet: | number | počet hospitalizovaných neočkovaných osôb ku celkovému počtu |
| hospitalizovani_bez_ockovani_vek_prumer: | integer | vekový priemer hospitalizovaných neočkovaných osôb |
| hospitalizovani_nedokoncene_ockovani: | integer | počet hospitalizovaných očkovaných osôb s 1 dávkou |
| hospitalizovani_nedokoncene_ockovani_relativni_pocet: | number | počet hospitalizovaných očkovaných osôb s 1 dávkou ku celkovému počtu |
| hospitalizovani_nedokoncene_ockovani_vek_prumer: | integer | vekový priemer hospitalizovaných očkovaných osôb s 1 dávkou |
| hospitalizovani_dokoncene_ockovani: | integer | počet hospitalizovaných očkovaných osôb s 2 dávkou |
| hospitalizovani_dokoncene_ockovani_relativni_pocet: | number | počet hospitalizovaných očkovaných osôb s 2 dávkou ku celkovému počtu |
| hospitalizovani_dokoncene_ockovani_vek_prumer: | integer | vekový priemer hospitalizovaných očkovaných osôb s 2 dávkou |
| hospitalizovani_posilujici_davka: | integer | počet hospitalizovaných očkovaných osôb s 3 dávkou |
| hospitalizovani_posilujici_davka_relativni_pocet: | number | počet hospitalizovaných očkovaných osôb s 3 dávkou ku celkovému počtu |
| hospitalizovani_posilujici_davka_vek_prumer: | integer | vekový priemer hospitalizovaných očkovaných osôb s 3 dávkou |

### COVID-19: Prehľad úmrtí s ohľadom na vykázané očkovania
**Popis:**
Dátová sada obsahuje počet, percento a priemerný vek zosnulých. Každý riadok udáva súhrnné údaje osôb v daný deň rozdelených do skupín podľa stavu očkovanosti: bez očkovania, s nedokončeným očkovaním, s dokončeným očkovaním alebo s dokončeným očkovaním vrátane posilňujúcej dávky.

**Schéma:**
| stĺpec | dátový typ | význam |
|--|--|--|
| id: | string | identifikačný reťazec  |
| datum: | string | dátum dňa údajov |
| zemreli_celkem: | integer | celkový počet zosnulých osôb |
| zemreli_bez_ockovani: | integer | počet zosnulých neočkovaných osôb |
| zemreli_bez_ockovani_relativni_pocet: | number | počet zosnulých neočkovaných osôb ku celkovému počtu |
| zemreli_bez_ockovani_vek_prumer: | integer | vekový priemer zosnulých neočkovaných osôb |
| zemreli_nedokoncene_ockovani: | integer | počet zosnulých očkovaných osôb s 1 dávkou |
| zemreli_nedokoncene_ockovani_relativni_pocet: | number | počet zosnulých očkovaných osôb s 1 dávkou ku celkovému počtu |
| zemreli_nedokoncene_ockovani_vek_prumer: | integer | vekový priemer zosnulých očkovaných osôb s 1 dávkou |
| zemreli_dokoncene_ockovani: | integer | počet zosnulých očkovaných osôb s 2 dávkou |
| zemreli_dokoncene_ockovani_relativni_pocet: | number | počet zosnulých očkovaných osôb s 2 dávkou ku celkovému počtu |
| zemreli_dokoncene_ockovani_vek_prumer: | integer | vekový priemer zosnulých očkovaných osôb s 2 dávkou |
| zemreli_posilujici_davka: | integer | počet zosnulých očkovaných osôb s 3 dávkou |
| zemreli_posilujici_davka_relativni_pocet: | number | počet zosnulých očkovaných osôb s 3 dávkou ku celkovému počtu |
| zemreli_posilujici_davka_vek_prumer: | integer | vekový priemer zosnulých očkovaných osôb s 3 dávkou |

### COVID-19: Prehľad vykázaných očkovaní podľa krajov ČR
**Popis:**
Dátová sada poskytuje agregované dáta o vykázaných očkovaniach na úrovni krajov ČR. Každý riadok prehľadu popisuje počet vykázaných očkovaní v danom dni, za vekovú skupinu, s použitím vybranej očkovacej látky a vo vybranom kraji.

<<<<<<< HEAD
**Schéma:**
| stĺpec | dátový typ | význam |
|--|--|--|
| id: | string | identifikačný reťazec  |
| datum: | string | dátum dňa údajov |
| vakcina: | string | názov vakcíny |
| kraj_nuts_kod: | string | kód kraja bydliska osoby |
| kraj_nazev: | string | názov kraja bydliska osoby |
| vekova_skupina: | string | veková skupina zaočkovaného |
| prvnich_davek: | integer | počet prvej dávky|
| druhych_davek: | integer | počet druhej dávky |
| celkem_davek: | integer | celkový počet zaočkovaní |
=======
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
| pacient_prvni_zaznam: | integer |  |
| kum_pacient_prvni_zaznam: | integer |  |
| pocet_hosp: | integer |  |
| stav_bez_priznaku: | integer |  |
| stav_lehky: | integer |  |
| stav_stredni: | integer |  |
| stav_tezky: | integer |  |
| jip: | integer |  |
| kyslik: | integer |  |
| hfno: | integer |  |
| upv: | integer |  |
| ecmo: | integer |  |
| tezky_upv_ecmo: | integer |  |
| umrti: | integer |  |
| kum_umrti: | integer |  |

### COVID-19: Prehľad úmrtí podľa hlásenia krajských hygienických staníc
**Popis:**
Dátová sada podľa krajov a okresov ČR obsahujúca kumulatívne denné počty osôb s preukázaným ochorením COVID-19 podľa validovaných hlásení krajských hygienických staníc, kumulatívne denné počty vyliečených po ochorení COVID-19 podľa hlásenia krajských hygienických staníc a kumulatívne denné počty úmrtí v súvislosti s ochorením COVID 19 podľa hlásenia krajských hygienických staníc a hospitalizačných úmrtí.

**Schéma:**
| stĺpec | dátový typ | význam |
|--|--|--|
| datum: | date | dátum dňa potvrdenia úmrtia  |
| kraj_nuts_kod: | string | kód kraja bydliska osoby |
| okres_lau_kod: | string | kód okresu bydliska osoby |
| kumulativni_pocet_nakazenych: | integer |  |
| kumulativni_pocet_vylecenych: | integer |  |
| kumulativni_pocet_umrti: | integer |  |
>>>>>>> documentation: Added description about more data sets

## Implementácia riešenia
### dataset.py
Obsahuje potrebné funkcie pre manipuláciu s dátovými sadami, ako napríklad ich sťahovanie, spracovanie, odstránenie z DB, vkladanie či načítanie z DB.
### download.py
Pracuje s funkciami v *dataset.py* a interaguje s databázou. Príklad na spustenie:
```sh 
python3 download.py [-h][--update COLLECTION_NAME] [--download] [--clear] [--fetch COLLECTION_NAME]
	-h, --help Zobrazí túto pomocnú správu a ukončí sa
  -u COLLECTION_NAME, --update COLLECTION_NAME Aktualizuje zadanú kolekciu v db. Na aktualizáciu každej kolekcie použite „all“.
  -d, --download Vymaže databázu a stiahne množiny údajov uložené v súbore datasets.json
  -c, --clear Vymaže databázu
  -s COLLECTION_NAME, --fetch COLLECTION_NAME Načíta zadanú kolekciu z db
```

### setup.sh
Skript na stiahnutie potrebných knižníc a závislostí pre fungovanie riešenia
### datasets.json
Obsahuje potrebné linky na stiahnutie dátových sád.