# polcyr

A Polish Cyrillic orthography that aims for lossless conversion and etymological accuracy.

Currently achieves 99.5% losslessness on a Polish dictionary (4 mil words).

* The count excludes words containing \<q w x>, which always have to be lossy.

* 0.5% includes a variety of fail conditions I intend to work on.

## Orthography

### Some design features

* 34 letters: Аа Бб Вв Гг Ғғ Дд Ее Ѐѐ Жж Зз Ии Іі Ӥӥ Јј Кк Лл Мм Нн Оо Пп Рр Сс Тт Уу У́у́ Фф Хх Цц Чч Шш Щщ Ьь Юю Яя Я́я́.

* <у я> are used exclusively for nasal vowels, whereas /u ja/ are <оу іа>.

* Ukrainian-style <і и>.

* Etymological <ть дь ль рь> for <ć dź l rz>.

* With small modifications, becomes compatible with Ukrainian keyboards.

### Examples

> Панграм (гр. пан грамма – кажда літѐра) – кро́тке здане заверају́це вшистке літѐри данѐго язика. Може становіть забаву словну́, чясто ест еднак ро́внеж викорістиванѐ до справдзаніа поправності даних тѐкстових, поправності висветліаніа люб дроукованіа знако́в ітп. Щего́льне допрацованѐ панграми заверају́ кажду́ літѐру тилько в едним висту́пеню.

> Ло́дь – міасто на правах повіатоу в сьродковѐј Польсце. Вякшость дісејшеј Лоді знајдоуе ся в ғісторичнѐј земі лучицкеј, а невелька чясть міаста (на левим брегоу Нѐроу) в земі серадзкеј. Седіба владз воево́дзтва ло́дзкего, повіатоу ло́дзкего всходнего ораз гміни Новосольна, прејстіова седіба владз паньствових в 1945 рокоу. Осьродѐк акадѐміцкі (19 учельні), коультоуральни і премислови. Пред преміанамі політично-господарчимі в 1989 р. центроум премислоу вло́кеннічего і фільмовѐго.

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
