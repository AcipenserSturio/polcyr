# polcyr

A Polish Cyrillic orthography that aims for lossless conversion and etymological accuracy.

Currently achieves 99.92% losslessness on a Polish dictionary (4 mil words).

* The count excludes words containing \<q w x>, which always have to be lossy.

* 0.08% includes a variety of fail conditions, mostly related to borrowings.

## Orthography

### Some design features

* 35 letters: Аа Бб Вв Гг Ғғ Дд Ее Єє Жж Зз Ии Іі Її Јј Кк Лл Мм Нн Оо Пп Рр Сс Тт Уу У́у́ Фф Хх Цц Чч Шш Щщ Ьь Юю Яя Я́я́.

* /u ja/ are usually <оу іа>; <у я> are used for nasal vowels.

  * (<у я> are used for /u ja/ in environments where nasal vowels never occur: <у> word initially and in diphthongs, <я> after a vowel.)

* Ukrainian-style <і и>.

* Etymological <ть дь ль рь> for <ć dź l rz>.

* With small modifications, becomes compatible with Ukrainian keyboards.

* <ї>, unlike its use in Ukrainian, is used as a non-palatalising /i/ in /ri di ti/, mostly in borrowings and morpheme boundaries.

### Examples

> Панграм (гр. пан грамма – кажда літера) – кро́ткє зданє завєрају́це вшисткє літери данего язика. Може становіть забаву словну́, чясто єст єднак ро́внєж викорістиване до справдзаніа поправності даних текстових, поправності висвєтліаніа люб дроукованіа знако́в ітп. Щего́льнє допрацоване панграми завєрају́ кажду́ літеру тилько в єдним висту́пєню.

> Ло́дь – міасто на правах повіатоу в сьродковеј Польсце. Вякшость дісєјшеј Лоді знајдоує ся в ғісторичнеј зємі лучицкєј, а нєвєлька чясть міаста (на лєвим брєгоу Нероу) в зємі сєрадзкєј. Сєдіба владз воєво́дзтва ло́дзкєго, повіатоу ло́дзкєго всходнєго ораз гміни Новосольна, прєјстіова сєдіба владз паньствових в 1945 рокоу. Осьродек академіцкі (19 учельні), коультоуральни і прємислови. Прєд прєміанамі політично-господарчимі в 1989 р. центроум прємислоу вло́кєннічего і фільмовего.

> Знакі диякритичне, диякритикі (стгр. διακριτικός „одро́жніају́ци”) – знакі графічне уживане в альфабетах і інних системах пісма, умєщане над, под літеру́, обок люб вевну́трь нєј, змєніају́це спосо́б одчитоу теј літери і творя́це прєз то нову́ літеру. В альфабетах силіабових могу́ змєніть значенє цалеј силіаби.

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
