Autory: Matej Berezný, Ondrej Valo, Švenk Adam

Login: xberez03, xvaloo00, xsvenk00
## Príprava
Pred spustením riešenia treba spustiť `setup.sh` pomocou príkazového riadka, pre nainštalovanie potrebných knižníc a závislostí. 
```sh 
./setup.sh
```
Medzi podporované systémy patria Ubuntu, Fedora, CentOS, RHEL8, RHEL9.
## Spustenie
Pred spustením riešenia treba spustiť `setup.sh` pre nainštalovanie potrebných knižníc a závislostí.
```sh 
python3 download.py [-h][--update COLLECTION_NAME] [--download] [--clear] [--fetch COLLECTION_NAME]
	-h, --help Zobrazí túto pomocnú správu a ukončí sa
  -u COLLECTION_NAME, --update COLLECTION_NAME Aktualizuje zadanú kolekciu v db. Na aktualizáciu každej kolekcie použite „all“.
  -d, --download Vymaže databázu a stiahne množiny údajov uložené v súbore datasets.json
  -c, --clear Vymaže databázu
  -s COLLECTION_NAME, --fetch COLLECTION_NAME Načíta zadanú kolekciu z db
```
### prepare_data.py
Skript pre prípravu dát, kde pre každý dotaz v rámci zadania extrahuje dáta z serveru upraví ich a uloží ich do .cvs súborov.
```
python3 prepare_data.py [--query_list QUERY1 QUERY2...]
```
```
	-q QUERY_LIST, --query_list QUERY_LIST vygeneruje .csv súbor pre jeden z zadaných dotazov 
```
### plot.py
Skript na vykresľovanie grafov z lokálne uložených .cvs súborov. Pokiaľ nenájde potrebné .csv súbory, sám si ich vygeneruje pomocou *prepare_data.py*.
```
python3 plot.py [--query_list QUERY1 QUERY2...]
```
```
	-q QUERY_LIST, --query_list QUERY_LIST vygeneruje .csv súbor pre jeden z zadaných dotazov 
```