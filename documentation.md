
# Dokumantácia

Autory: Matej Berezný, Ondrej Valo, Švenk Adam
Login: xberez03, xvaloo00, xsvenk00

## Popis dátovych sád
### COVID-19: Prehľad osôb s potvrdenou nákazou podľa hlásenia krajských hygienických staníc
**Popis:**
Dátová sada obsahujúca na základe denní incidenčný prehľad osôb s preukázanou nákazou COVID-19 podľa hlásenia krajských hygienických staníc.

**Schéma:**
| stĺpec | dátový typ | význam |
|--|--|--|
| datum: | date | dátum dňa potvrdenia ochorenia  |
| vek: | integer | vek nakazeného |
| pohlavi: | string | pohlavie nakazeného |
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
| vek: | integer | vek vyliečeného |
| pohlavi: | string | pohlavie vyliečeného |
| kraj_nuts_kod: | string | kód kraja bydliska osoby |
| okres_lau_kod: | string | kód okresu bydliska osoby |


## Implementácia riešenia
### dataset.py
### download.py
### setup.sh