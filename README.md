Autory: Matej Berezný, Ondrej Valo, Švenk Adam

Login: xberez03, xvaloo00, xsvenk00

## Príprava
Pred spustením riešenia treba spustiť `setup.sh` pomocou príkazového riadka, pre nainštalovanie potrebných knižníc a závislostí. 
```sh 
./setup.sh
```
Medzi podporované systémy patria Ubuntu, Fedora, CentOS, Rhel8.
## Spustenie
Pred spustením riešenia treba spustiť `setup.sh` pre nainštalovanie potrebných knižníc a závislostí.
```sh 
python3 download.py [-h][--update UPDATE] [--download] [--clear] [--fetch FETCH]
	-h, --help Zobrazí túto pomocnú správu a ukončí sa
  -u UPDATE, --update UPDATE Aktualizuje zadanú kolekciu v db. Na aktualizáciu každej kolekcie použite „all“.
  -d, --download Vymaže databázu a stiahne množiny údajov uložené v súbore datasets.json
  -c, --clear Vymaže databázu
  -s FETCH, --fetch FETCH Načíta zadanú kolekciu z db
```