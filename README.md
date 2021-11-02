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