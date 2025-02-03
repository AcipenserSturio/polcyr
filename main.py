import requests
from tqdm import tqdm
import pandas as pd
import re


# DICT = "https://raw.githubusercontent.com/sigo/polish-dictionary/master/dist/pl.txt"
# dictionary = requests.get(DICT).content.decode("utf8")
# with open("dict.txt", "w") as f:
#     f.write(dictionary.lower())

alphabet = {
    "b": "б",
    "c": "ц",
    "č": "ч",
    "d": "д",
    "f": "ф",
    "g": "г",
    "ɣ": "ғ",
    "h": "х",
    "j": "ј",
    "k": "к",
    "l": "л",
    "m": "м",
    "n": "н",
    "p": "п",
    "r": "р",
    "s": "с",
    "š": "ш",
    "t": "т",
    "w": "в",
    "z": "з",
    "ž": "ж",
    # "v": "в",
    # "q": "кв",
    # "x": "кс",
}


# converts polish latin to cyrillic
def encode(w):
    # First, to avoid wrong matches, let us convert digraph consonants
    # to a less error-prone view:
    w = re.sub(r"(?<!c)h", "ɣ", w)
    w = w.replace("ch", "h")
    w = w.replace("cz", "č")
    w = w.replace("sz", "š")
    w = w.replace("ż", "ž")  # just for letter consistency
    w = re.sub("rz(?!i)", "ř", w)  # exclude rzi: its actually r-zi

    # some <i> in Polish is borrowed, and doesn't trigger palatalisation.
    # This is an Udmurt letter lol sorry
    w = re.sub("(?<=[dtr])i", "ӥ", w)
    w = re.sub("(?<=l)i(?=[aeioóuyąę])", "ӥ", w)

    # <i> is ь with vowels, and ьy /ʲɨ/ elsewhere
    w = re.sub("i(?![aeioóuyąę])", "ьy", w)
    w = w.replace("i", "ь")

    # Intervocalic j will also be represented by the "soft" vowel series.
    w = re.sub(r"(?<=[aeoóuyąę])j(?=[aeoóuyąę])", "ь", w)

    # While we are at it, split apart the palatalisation from acute consonants.
    w = w.replace("ć", "tь")
    w = w.replace("ń", "nь")
    w = w.replace("ś", "sь")
    w = w.replace("ź", "zь")

    # Polish treats lь vs l as orthographic l vs ł,
    # and rь as rz. Let's undo that
    w = re.sub("l(?![ьӥ])", "lь", w)  # Have to be fancy to avoid lььy and lьӥ
    w = w.replace("ł", "l")
    w = w.replace("ř", "rь")

    # Polish prefers affricate representation of /tj dj/, let's undo it
    w = w.replace("cь", "tь")
    w = w.replace("dzь", "dь")

    # *sv *zv *st *zd was palatalised in its entirety,
    # so lets remove the redundant ь.
    w = re.sub(r"(?<=[sz])ь(?=wь)", "", w)
    w = re.sub(r"(?<=s)ь(?=tь)", "", w)
    # w = re.sub(r"(?<=z)ь(?=dь)", "", w)

    # Let's insert historic palatalisation for retroflexes.
    # w = w.replace("č", "čь")
    # w = w.replace("š", "šь")
    # w = w.replace("ž", "žь")
    # j at the beginnings of words will be turned into ь,
    # for ease of vowel representation.
    w = re.sub(r"^j", "ь", w)

    # Now, let's cyrillicise the vowels:
    w = w.replace("ьa", "іа")
    w = w.replace("ьe", "є")
    w = w.replace("ьo", "іо")
    w = w.replace("ьu", "ю")
    w = w.replace("ьó", "іо́")
    w = w.replace("ьę", "я")
    w = w.replace("ьą", "я́")
    w = w.replace("ьy", "і")

    w = w.replace("a", "а")
    w = w.replace("e", "е")
    w = w.replace("u", "оу")
    w = w.replace("o", "о")
    w = w.replace("ó", "о́")
    w = w.replace("ę", "у")
    w = w.replace("ą", "у́")
    w = w.replace("y", "и")

    # Handle riV => рjV ?
    # w = re.sub("ri(?=[aeiouyąę])", "rj", w)

    # Finally, let's use cyrillic consonants:
    for lat, cyr in alphabet.items():
        w = w.replace(lat, cyr)
    return w


# converts polish cyrillic to latin
def decode(w):
    # First, let's use latin consonants:
    for lat, cyr in alphabet.items():
        w = w.replace(cyr, lat)

    # De-cyrillicise the vowels:
    w = w.replace("іо́", "ьó")  # trigraph
    w = w.replace("іа", "ьa")
    w = w.replace("іо", "ьo")
    w = w.replace("я́", "ьą")  # digraphs have to go first
    w = w.replace("є", "ьe")
    w = w.replace("ю", "ьu")
    w = w.replace("я", "ьę")
    w = w.replace("і", "ьy")

    w = w.replace("оу", "u")
    w = w.replace("о́", "ó")
    w = w.replace("у́", "ą")  # digraphs have to go first
    w = w.replace("а", "a")
    w = w.replace("е", "e")
    w = w.replace("о", "o")
    w = w.replace("у", "ę")
    w = w.replace("и", "y")

    # Word-initial ь is j:
    w = re.sub(r"^ь", "j", w)

    # Re-insert implicit palatalisation:
    w = re.sub(r"(?<=[sz])(?=wь)", "ь", w)
    w = re.sub(r"(?<=s)(?=tь)", "ь", w)
    # w = re.sub(r"(?<=z)(?=dь)", "ь", w)

    # Polish prefers affricate representation of /tj dj/:
    w = w.replace("tь", "cь")
    w = w.replace("dь", "dzь")

    # Use Polish l vs ł, and rz:
    w = re.sub("l(?![ьӥ])", "ł", w)
    w = w.replace("lьy", "li")  # erroneously goes to ly otherwise
    w = w.replace("lь", "l")
    w = w.replace("rь", "ř")

    # When not followed by a vowel, use diacritic for soft consonants:
    w = re.sub(r"cь(?![aeoóuyąę])", "ć", w)
    w = re.sub(r"nь(?![aeoóuyąę])", "ń", w)
    w = re.sub(r"sь(?![aeoóuyąę])", "ś", w)
    w = re.sub(r"zь(?![aeoóuyąę])", "ź", w)

    # Bring back j intervocalically:
    w = re.sub(r"(?<=[aeoóuyąę])ь(?=[aeoóuyąę])", "j", w)

    # Re-establish ь -> i
    w = re.sub("ьy?", "i", w)
    w = re.sub("jy", "i", w)  # after a vowel!

    # Re-interpret non-palatalising i:
    w = w.replace("ӥ", "i")

    # Replace Czech letters with Polish digraphs
    w = w.replace("h", "ch")
    w = w.replace("ɣ", "h")
    w = w.replace("č", "cz")
    w = w.replace("š", "sz")
    w = w.replace("ž", "ż")  # just for letter consistency
    w = w.replace("ř", "rz")

    return w


def correct(w):
    return encode(decode(w)) == w


def convert(text):
    cyrillics = []
    tokens = text.split()
    for token in tokens:
        capd = token[0].upper() == token[0]
        token = token.lower()
        cyr = encode(token)
        if capd:
            cyr = cyr.title()
        cyrillics.append(cyr)
    return " ".join(cyrillics)


def revert(text):
    lacinka = []
    tokens = text.split()
    for token in tokens:
        capd = token[0].upper() == token[0]
        token = token.lower()
        cyr = decode(token)
        if capd:
            cyr = cyr.title()
        lacinka.append(cyr)
    return " ".join(lacinka)


def test():
    with open("dict.txt") as f:
        dictionary = f.read().split("\n")
        dictionary = [item for index, item
                      in enumerate(dictionary) if
                      # index % 50 == 0 and
                      "v" not in item
                      and "x" not in item
                      and "q" not in item
                      ]

    df = []
    for word in tqdm(dictionary):
        cyr = encode(word)
        lat = decode(cyr)
        df.append([word, cyr, lat, word == lat])
    df = pd.DataFrame(df, columns=["word", "cyr", "lat", "correct"])
    df.sort_values("correct").to_csv("conv.csv")

    print(f"""
    Correct: {len(df[df["correct"]])}
    Total: {len(df)}
    Correct percentage: {100*len(df[df["correct"]]) / len(df):.2f}%
    """)

if __name__ == "__main__":
    # test()
    a = convert("""Pójdź w loch zbić małżeńską gęś futryn!""")
    print(a)


