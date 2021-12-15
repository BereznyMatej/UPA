
# Dokumantácia

Autory: Matej Berezný, Ondrej Valo, Švenk Adam

Login: xberez03, xvaloo00, xsvenk00

## Popis dátových sád
Dáta sú čítané z neskôr uvedených zdrojov a ukladané pomocou MongoDB na zadarmo hosťovaný klaster, kde sú údaje uložené v dokumentoch BSON (binárny JSON) s dynamickou schémou. 
Dátové sady boli získane z:
https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19m
https://www.czso.cz/csu/czso/obyvatelstvo-podle-petiletych-vekovych-skupin-a-pohlavi-v-krajich-a-okresech
### COVID-19: Prehľad osôb s potvrdenou nákazou podľa hlásenia krajských hygienických staníc
**Popis:**
Dátová sada obsahuje denní prehľad osôb s preukázanou nákazou COVID-19 podľa hlásenia krajských hygienických staníc.

**Schéma:**
| stĺpec | dátový typ | význam |
|--|--|--|
| id: | string | identifikačný reťazec  |
| datum: | string | dátum dňa potvrdenia ochorenia  |
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
| id: | string | identifikačný reťazec  |
| datum: | string | dátum dňa údajov |
| kraj_nuts_kod: | string | kód kraja bydliska osoby |
| okres_lau_kod: | string | kód okresu bydliska osoby |
| kumulativni_pocet_nakazenych: | integer | kumulatívny počet nakazených v okrese |
| kumulativni_pocet_vylecenych: | integer | kumulatívny počet vyliečených v okrese |
| kumulativni_pocet_umrti: | integer | kumulatívny počet úmrtí v okrese |

### Obyvateľstvo podľa päťročných vekových skupín a pohlaví v krajoch a okresoch
**Popis:**
Dátová sada obsahuje časový rad so štatistickými údajmi od roku 2010 o vekovom zložení mužov a žien (päťročnej vekovej skupiny) s trvalým alebo dlhodobým pobytom, a to podľa stavu k 31. 12. Údaje sú publikované za okresy, kraje a Českú republiku.

**Schéma:**
| stĺpec | dátový typ | význam |
|--|--|--|
| idhod: | string | unikátny identifikátor údajov verejnej databázy ČSU |
| hodnota: | number | zistená hodnota |
| stapro_kod: | string | kód štatistickej premenej v systéme SMS UKAZ |
| pohlavi_cis: | string | číselník pre pohlavie |
| pohlavi_kod: | string | kód pohlavia |
| vek_cis: | string | číselník pre vek |
| vek_kod: | string | kód veku |
| vuzemi_cis: | string | kód číselníka pre referenčné územie, číselní odpovedá typológii územia, okresy majú kód 101, správne obvody ORP 65 |
| vuzemi_kod: | string | kód položky z číselníku pre referenčné územie |
| casref_do: | date | referenčné obdobie, vo formáte RRRR-MM-DD |
| pohlavi_txt: | string | text položky z číselníka pohlavia |
| vek_txt: | string | text položky pre vek |
| vuzemi_txt: | string | text z číselníka pre referenčné územie |

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

### COVID-19: Očkovacie miesta v ČR
**Popis:**
Dátová sada poskytuje zoznam verejných očkovacích miest v ČR, kde sú podávané očkovacie látky proti ochoreniu COVID-19.

**Schéma:**
| stĺpec | dátový typ | význam |
|--|--|--|
| ockovaci_misto_id: | string | identifikačný reťazec očkovacieho miesta |
| ockovaci_misto_nazev: | string | názov očkovacieho miesta |
| okres_nuts_kod: | string | kód kraja očkovacieho miesta |
| operacni_status: | boolean | operačný status očkovacieho miesta |
| ockovaci_misto_adresa: | string | adresa očkovacieho miesta |
| latitude: | string | latitude očkovacieho miesta |
| longitude: | string | longitude očkovacieho miesta |
| ockovaci_misto_typ: | string | typ očkovacieho miesta |
| nrpzs_kod: | string | kód národného registra
poskytovateľov zdravotných služieb |
| minimalni_kapacita: | integer | minimálna kapacita osôb očkovacieho miesta |
| bezbarierovy_pristup: | boolean | možnosť bezbariérového prístupu |

### COVID-19: Prehľad vykázaných očkovaní podľa očkovacích miest ČR
**Popis:**
Dátová sada poskytuje riadkové dáta o vykázaných očkovaniach na jednotlivých očkovacích miestach ČR. Každý riadok prehľadu popisuje jedno vykázané očkovanie v danom dni a vekovej skupine, s použitím vybranej očkovacej látky, na konkrétnom očkovacom mieste a vo vybranom kraji.

**Schéma:**
| stĺpec | dátový typ | význam |
|--|--|--|
| id: | string | identifikačný reťazec očkovania |
| datum: | string | dátum dňa očkovania |
| vakcina: | string | názov vakcíny |
| kraj_nuts_kod: | string | kód kraja očkovacej stanice |
| kraj_nazev: | string | názov kraja očkovacej stanice |
| zarizeni_kod: | string | kód očkovacieho miesta |
| zarizeni_nazev: | string | názov očkovacieho miesta |
| poradi_davky: | integer | poradie očkovacej dávky |
| vekova_skupina: | string | veková skupina zaočkovaného |

### COVID-19: Očkovacie zriadenie
**Popis:**
Dátová sada poskytuje zoznam očkovacích zriadení v ČR ako doplnenie zoznamu očkovacích miest, kde sú podávané očkovacie látky proti ochoreniu COVID-19. Jedná sa predovšetkým o praktických lekárov, ale aj ďalších, kde sa očkovanie vykonáva.

**Schéma:**
| stĺpec | dátový typ | význam |
|--|--|--|
| id: | string | identifikačný reťazec zriadenia |
| zarizeni_kod: | string | kód zriadenia |
| zarizeni_nazev: | string | názov zriadenia |
| provoz_zahajen: | boolean | fungovanie zriadenia |
| kraj_nuts_kod: | string | kód kraju kde sa nachádza zriadenie |
| kraj_nazev: | string | názov kraja kde sa nachádza zriadenie |
| okres_lau_kod: | string | kód okresu kde sa nachádza zriadenie |
| okres_nazev: | string | názov okresu kde sa nachádza zriadenie |
| zrizovatel_kod: | integer | kód zriaďovateľa zriadenia |
| zrizovatel_nazev: | string | názov zriaďovateľa zriadenia |
| provoz_ukoncen: | string | dátum ukončenia prevádzky zriadenia |
| prakticky_lekar: | boolean | prítomnosť praktického lekára |

## Implementácia riešenia
### dataset.py
Obsahuje potrebné funkcie pre manipuláciu s dátovými sadami, ako napríklad ich sťahovanie, spracovanie, odstránenie z DB, vkladanie či načítanie z DB.
### download.py
Pracuje s funkciami v *dataset.py* a interaguje s databázou. Príklad na spustenie:
```sh 
python3 download.py [-h][--update COLLECTION_NAME] [--download] [--clear] [--fetch COLLECTION_NAME] [--workers INTEGER]
	  -h, --help Zobrazí túto pomocnú správu a ukončí sa
	  -u COLLECTION_NAME, --update COLLECTION_NAME Aktualizuje zadanú kolekciu v db. Na aktualizáciu každej kolekcie použite „all“.
	  -d, --download Vymaže databázu a stiahne množiny údajov uložené v súbore datasets.json
	  -c, --clear Vymaže databázu
	  -s COLLECTION_NAME, --fetch COLLECTION_NAME Načíta zadanú kolekciu z db
	  -w INTEGER, --workers INTEGER určuje počet vytvorenćh vlákien pre ukladanie dát do databázi
```
### setup.sh
Skript na stiahnutie potrebných knižníc a závislostí pre fungovanie riešenia
### datasets.json
Obsahuje potrebné linky na stiahnutie dátových sád.
### prepare_data.py
Skript pre prípravu dát, kde pre každý dotaz v rámci zadania extrahuje dáta z serveru upraví ich a uloží ich do .cvs súborov.
```
python3 prepare_data.py [--query_list QUERY1 QUERY2...]
	-q QUERY_LIST, --query_list QUERY_LIST vygeneruje .csv súbor pre jeden z zadaných dotazov 
```
### plot.py
Skript na vykresľovanie grafov z lokálne uložených .cvs súborov. Pokiaľ nenájde potrebné .csv súbory, sám si ich vygeneruje pomocou *prepare_data.py*.
```
python3 plot.py [--query_list QUERY1 QUERY2...]
	-q QUERY_LIST, --query_list QUERY_LIST vygeneruje .csv súbor pre jeden z zadaných dotazov 
```
## Doplnenie nedostatkov 1. zadania
V rámci druhého zadania boli taktiež opravené aktualizácie dát a indexácia dát kolekcií.
## Vyhotovené úlohy zadania 
### 1. dotaz skupiny A
Dáta boli pripravené pomocov skriptu *prepare_data.py* ktorý načítal kolekcie *hospitalizovany* a *statistika_celkovo* z nami spravovanej databázy, v ktorý boli dáta zoskupené podľa dátumu a následne pomocou dátumu prepojené. Taktiež boli premenované niektoré názvy stĺpcovú pre lepšiu prehľadnosť, a táto spojená kolekcia uložená do .csv súboru. Pomocou skriptu  *plot.py* bol uložený .csv súbor zobrazený v nasledujúcom grafe, predstavujúci vývoj Covid-19 v priebehu času.
![Vývoj Covid-19 v priebehu času.](https://cdn.discordapp.com/attachments/290943108303290368/920426783524937748/Q2.png)
### 2. dotaz skupiny A
Dáta boli pripravené pomocov skriptu *prepare_data.py* ktorý načítal kolekciu *nakazeny_kraj* z nami spravovanej databázy a upravil názvy stĺpcov pre lepšiu prehľadnosť a následne uložil túto kolekciu ako .csv súbor. Ďalej pomocou skriptu *plot.py* bol vygenerovaný nasledovný graf z uloženého .csv súboru, ktorý predstavuje vekové rozloženie pacientov pozitívnych na covid-19 podľa regiónu.
![Vekové rozloženie pacientov pozitívnych na covid-19 podľa regiónu.](https://cdn.discordapp.com/attachments/290943108303290368/920419090793906176/Q1.png)
### Dotaz skupiny B
Skript *prepare_data.py* načítal kolekcie *'obyvatelia* a *nakazeny_kraj* upravil niektoré názvy stĺpcov a zoskupil dáta podľa dátumov a pridal nový stĺpec predstavujúci prepočítaný počet nakazených na jedného obyvateľa. Následne v skripte *plot.py* boli tabuľky prepojené pomocou regiónu a vygenerovaný graf predstavujúci pozitívne prípady Covid-19 na celkovú populáciu v regiónoch.![Pozitívne prípady Covid-19 na celkovú populáciu v regiónoch.](https://media.discordapp.net/attachments/290943108303290368/920432189211025469/query_b.png?width=1340&height=670)
### Vlastný dotaz 1
Pomocou skriptu *prepare_data.py* boli z databáze načítané kolekcie *hospitalizovani_ockovanie*, *zemreli_ockovanie*, *jip_ockovanie*, *ockovanie_kraj* a *obyvatelia*, následne upravené niektoré stĺpce a uložené do jedného .csv súboru. Ďalej skript *plot.py* z uloženého .csv súboru generoval graf pomerov úmrtia, JIP a hospitalizácie medzi očkovanými a neočkovanými osobami.![Pomer úmrtia/JIP/hospitalizácie medzi očkovanými a neočkovanými osobami](https://cdn.discordapp.com/attachments/290943108303290368/920432189445914654/query_custom1.png)
### Vlastný dotaz 2
Za pomoci *prepare_data.py* boli načítané a upravené kolekcie *hospitalizovany*, *statistika_celkovo*. Údaje v oboch kolekciách zoskupené a následne prepojené pomocou dátumu a nakoniec uložené ako .csv súbor. Pokračujúc skript *plot.py* generoval graf predstavujúci porovnanie medzi novými kritickými prípadmi a celkovo novými prípadmi COVID-19.
![Porovnanie medzi novými kritickými prípadmi a celkovo novými prípadmi COVID-19.](https://cdn.discordapp.com/attachments/290943108303290368/920432189752107148/query_custom2.png)
