# polcyr

A Polish Cyrillic orthography that aims for lossless conversion and etymological accuracy.

Currently achieves 99.5% losslessness on a Polish dictionary (4 mil words). (Starts failing on borrowings.)

## Orthography

### Some design features

* <у я> are used exclusively for nasal vowels, whereas /u ja/ are <оу іа>.

* Ukrainian-style <і и>.

* Etymological <ть дь ль рь> for <ć dź l rz>.

* With small modifications, becomes compatible with Ukrainian keyboards.

### Examples

> Панграм (гр. пан грамма – кажда літера) – кро́ткє зданє завєрая́це вшисткє літери данего язика. Може становіть забаву словну́, чусто єст єднак ро́внєж викорістиване до справдзаніа поправності даних текстових, поправності висвєтліаніа люб дроукованіа знако́в ітп. Шчего́льнє допрацоване панграми завєрая́ кажду́ літеру тилько в єдним висту́пєню.

> Ло́дь – міасто на правах повіатоу в сьродковеј Польсце. Вякшость дісєјшеј Лоді знајдоує ся в ғісторичнеј зємі лучицкєј, а нєвєлька чусть міаста (На лєвим брєгоу Нероу) в зємі сєрадзкєј. Сєдіба владз воєво́дзтва ло́дзкєго, повіатоу ло́дзкєго всходнєго ораз гміни Новосольна, прєјстіова сєдіба владз паньствових в 1945 рокоу. Осьродек академіцкі (19 оучельні), коультоуральни і прємислови. Прєд прєміанамі політично-господарчимі в 1989 р. центроум прємислоу вло́кєннічего і фільмовего.

## Requirements

* Python >= 3.13

* pdm (you can install it with `pip install pdm`).

## Installation and usage

```bash
git clone https://github.com/AcipenserSturio/polcyr
cd polcyr
pdm install
pdm run main.py
```

Alter the `__main__` block to your needs.

# License

polcyr is licensed under the GNU General Public License Version 3.
