
# Dokumantácia

Autory: Matej Berezný, Ondrej Valo, Švenk Adam

Login: xberez03, xvaloo00, xsvenk00

## Popis dátových sád
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

## Implementácia riešenia
### dataset.py
### download.py
### setup.sh