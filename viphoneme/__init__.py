#  (C1)(w)V(G|C2)+T

# symbol " ' " for undefine symbol and sign for english

"""
C1 = initial consonant onset
w = labiovelar on-glide /w/
V = vowel nucleus
G = off-glide coda (/j/ or /w/)
C2 = final consonant coda
T = tone.
"""

Cus_onsets = {
    "b": "b",
    "t": "t",
    "th": "tʰ",
    "đ": "d",
    "ch": "c",
    "kh": "x",
    "g": "ɣ",
    "l": "l",
    "m": "m",
    "n": "n",
    "ngh": "ŋ",
    "nh": "ɲ",
    "ng": "ŋ",
    "ph": "f",
    "v": "v",
    "x": "s",
    "d": "z",
    "h": "h",
    "p": "p",
    "qu": "kw",
    "gi": "j",
    "tr": "ʈ",
    "k": "k",
    "c": "k",
    "gh": "ɣ",
    "r": "ʐ",
    "s": "ʂ",
    "gi": "j",
}


Cus_nuclei = {
    "a": "a",
    "á": "a",
    "à": "a",
    "ả": "a",
    "ã": "a",
    "ạ": "a",
    "â": "ɤ̆",
    "ấ": "ɤ̆",
    "ầ": "ɤ̆",
    "ẩ": "ɤ̆",
    "ẫ": "ɤ̆",
    "ậ": "ɤ̆",
    "ă": "ă",
    "ắ": "ă",
    "ằ": "ă",
    "ẳ": "ă",
    "ẵ": "ă",
    "ặ": "ă",
    "e": "ɛ",
    "é": "ɛ",
    "è": "ɛ",
    "ẻ": "ɛ",
    "ẽ": "ɛ",
    "ẹ": "ɛ",
    "ê": "e",
    "ế": "e",
    "ề": "e",
    "ể": "e",
    "ễ": "e",
    "ệ": "e",
    "i": "i",
    "í": "i",
    "ì": "i",
    "ỉ": "i",
    "ĩ": "i",
    "ị": "i",
    "o": "ɔ",
    "ó": "ɔ",
    "ò": "ɔ",
    "ỏ": "ɔ",
    "õ": "ɔ",
    "ọ": "ɔ",
    "ô": "o",
    "ố": "o",
    "ồ": "o",
    "ổ": "o",
    "ỗ": "o",
    "ộ": "o",
    "ơ": "ɤ",
    "ớ": "ɤ",
    "ờ": "ɤ",
    "ở": "ɤ",
    "ỡ": "ɤ",
    "ợ": "ɤ",
    "u": "u",
    "ú": "u",
    "ù": "u",
    "ủ": "u",
    "ũ": "u",
    "ụ": "u",
    "ư": "ɯ",
    "ứ": "ɯ",
    "ừ": "ɯ",
    "ử": "ɯ",
    "ữ": "ɯ",
    "ự": "ɯ",
    "y": "i",
    "ý": "i",
    "ỳ": "i",
    "ỷ": "i",
    "ỹ": "i",
    "ỵ": "i",
    "eo": "eo",
    "éo": "eo",
    "èo": "eo",
    "ẻo": "eo",
    "ẽo": "eo",
    "ẹo": "eo",
    "êu": "ɛu",
    "ếu": "ɛu",
    "ều": "ɛu",
    "ểu": "ɛu",
    "ễu": "ɛu",
    "ệu": "ɛu",
    "ia": "iə",
    "ía": "iə",
    "ìa": "iə",
    "ỉa": "iə",
    "ĩa": "iə",
    "ịa": "iə",
    "ia": "iə",
    "iá": "iə",
    "ià": "iə",
    "iả": "iə",
    "iã": "iə",
    "iạ": "iə",
    "iê": "iə",
    "iế": "iə",
    "iề": "iə",
    "iể": "iə",
    "iễ": "iə",
    "iệ": "iə",
    "oo": "ɔ",
    "óo": "ɔ",
    "òo": "ɔ",
    "ỏo": "ɔ",
    "õo": "ɔ",
    "ọo": "ɔ",
    "oo": "ɔ",
    "oó": "ɔ",
    "oò": "ɔ",
    "oỏ": "ɔ",
    "oõ": "ɔ",
    "oọ": "ɔ",
    "ôô": "o",
    "ốô": "o",
    "ồô": "o",
    "ổô": "o",
    "ỗô": "o",
    "ộô": "o",
    "ôô": "o",
    "ôố": "o",
    "ôồ": "o",
    "ôổ": "o",
    "ôỗ": "o",
    "ôộ": "o",
    "ua": "uə",
    "úa": "uə",
    "ùa": "uə",
    "ủa": "uə",
    "ũa": "uə",
    "ụa": "uə",
    "uô": "uə",
    "uố": "uə",
    "uồ": "uə",
    "uổ": "uə",
    "uỗ": "uə",
    "uộ": "uə",
    "ưa": "ɯə",
    "ứa": "ɯə",
    "ừa": "ɯə",
    "ửa": "ɯə",
    "ữa": "ɯə",
    "ựa": "ɯə",
    "ươ": "ɯə",
    "ướ": "ɯə",
    "ườ": "ɯə",
    "ưở": "ɯə",
    "ưỡ": "ɯə",
    "ượ": "ɯə",
    "yê": "iɛ",
    "yế": "iɛ",
    "yề": "iɛ",
    "yể": "iɛ",
    "yễ": "iɛ",
    "yệ": "iɛ",
    "uơ": "uə",
    "uở": "uə",
    "uờ": "uə",
    "uở": "uə",
    "uỡ": "uə",
    "uợ": "uə",
}


Cus_offglides = {
    "ai": "aj",
    "ái": "aj",
    "ài": "aj",
    "ải": "aj",
    "ãi": "aj",
    "ại": "aj",
    "ay": "ăj",
    "áy": "ăj",
    "ày": "ăj",
    "ảy": "ăj",
    "ãy": "ăj",
    "ạy": "ăj",
    "ao": "aw",
    "áo": "aw",
    "ào": "aw",
    "ảo": "aw",
    "ão": "aw",
    "ạo": "aw",
    "au": "ăw",
    "áu": "ăw",
    "àu": "ăw",
    "ảu": "ăw",
    "ãu": "ăw",
    "ạu": "ăw",
    "ây": "ɤ̆j",
    "ấy": "ɤ̆j",
    "ầy": "ɤ̆j",
    "ẩy": "ɤ̆j",
    "ẫy": "ɤ̆j",
    "ậy": "ɤ̆j",
    "âu": "ɤ̆w",
    "ấu": "ɤ̆w",
    "ầu": "ɤ̆w",
    "ẩu": "ɤ̆w",
    "ẫu": "ɤ̆w",
    "ậu": "ɤ̆w",
    "eo": "ew",
    "éo": "ew",
    "èo": "ew",
    "ẻo": "ew",
    "ẽo": "ew",
    "ẹo": "ew",
    "iu": "iw",
    "íu": "iw",
    "ìu": "iw",
    "ỉu": "iw",
    "ĩu": "iw",
    "ịu": "iw",
    "oi": "ɔj",
    "ói": "ɔj",
    "òi": "ɔj",
    "ỏi": "ɔj",
    "õi": "ɔj",
    "ọi": "ɔj",
    "ôi": "oj",
    "ối": "oj",
    "ồi": "oj",
    "ổi": "oj",
    "ỗi": "oj",
    "ội": "oj",
    "ui": "uj",
    "úi": "uj",
    "ùi": "uj",
    "ủi": "uj",
    "ũi": "uj",
    "ụi": "uj",
    # u'uy' : u'uj', u'úy' : u'uj', u'ùy' : u'uj', u'ủy' : u'uj', u'ũy' : u'uj', u'ụy' : u'uj',
    "uy": "ʷi",
    "úy": "uj",
    "ùy": "uj",
    "ủy": "uj",
    "ũy": "uj",
    "ụy": "uj",
    # thay để hạn chế trùng âm
    "uy": "ʷi",
    "uý": "ʷi",
    "uỳ": "ʷi",
    "uỷ": "ʷi",
    "uỹ": "ʷi",
    "uỵ": "ʷi",
    "ơi": "ɤj",
    "ới": "ɤj",
    "ời": "ɤj",
    "ởi": "ɤj",
    "ỡi": "ɤj",
    "ợi": "ɤj",
    "ưi": "ɯj",
    "ứi": "ɯj",
    "ừi": "ɯj",
    "ửi": "ɯj",
    "ữi": "ɯj",
    "ựi": "ɯj",
    "ưu": "ɯw",
    "ứu": "ɯw",
    "ừu": "ɯw",
    "ửu": "ɯw",
    "ữu": "ɯw",
    "ựu": "ɯw",
    "iêu": "iəw",
    "iếu": "iəw",
    "iều": "iəw",
    "iểu": "iəw",
    "iễu": "iəw",
    "iệu": "iəw",
    "yêu": "iəw",
    "yếu": "iəw",
    "yều": "iəw",
    "yểu": "iəw",
    "yễu": "iəw",
    "yệu": "iəw",
    "uôi": "uəj",
    "uối": "uəj",
    "uồi": "uəj",
    "uổi": "uəj",
    "uỗi": "uəj",
    "uội": "uəj",
    "ươi": "ɯəj",
    "ưới": "ɯəj",
    "ười": "ɯəj",
    "ưởi": "ɯəj",
    "ưỡi": "ɯəj",
    "ượi": "ɯəj",
    "ươu": "ɯəw",
    "ướu": "ɯəw",
    "ườu": "ɯəw",
    "ưởu": "ɯəw",
    "ưỡu": "ɯəw",
    "ượu": "ɯəw",
}
# Các âm vòng ở đây i chang không vòm: không có w ở trước		=> Try to add ʷ
Cus_onglides = {
    "oa": "ʷa",
    "oá": "ʷa",
    "oà": "ʷa",
    "oả": "ʷa",
    "oã": "ʷa",
    "oạ": "ʷa",
    "óa": "ʷa",
    "òa": "ʷa",
    "ỏa": "ʷa",
    "õa": "ʷa",
    "ọa": "ʷa",
    "oă": "ʷă",
    "oắ": "ʷă",
    "oằ": "ʷă",
    "oẳ": "ʷă",
    "oẵ": "ʷă",
    "oặ": "ʷă",
    "oe": "ʷɛ",
    "oé": "ʷɛ",
    "oè": "ʷɛ",
    "oẻ": "ʷɛ",
    "oẽ": "ʷɛ",
    "oẹ": "ʷɛ",
    "oe": "ʷɛ",
    "óe": "ʷɛ",
    "òe": "ʷɛ",
    "ỏe": "ʷɛ",
    "õe": "ʷɛ",
    "ọe": "ʷɛ",
    "ua": "ʷa",
    "uá": "ʷa",
    "uà": "ʷa",
    "uả": "ʷa",
    "uã": "ʷa",
    "uạ": "ʷa",
    "uă": "ʷă",
    "uắ": "ʷă",
    "uằ": "ʷă",
    "uẳ": "ʷă",
    "uẵ": "ʷă",
    "uặ": "ʷă",
    "uâ": "ʷɤ̆",
    "uấ": "ʷɤ̆",
    "uầ": "ʷɤ̆",
    "uẩ": "ʷɤ̆",
    "uẫ": "ʷɤ̆",
    "uậ": "ʷɤ̆",
    "ue": "ʷɛ",
    "ué": "ʷɛ",
    "uè": "ʷɛ",
    "uẻ": "ʷɛ",
    "uẽ": "ʷɛ",
    "uẹ": "ʷɛ",
    "uê": "ʷe",
    "uế": "ʷe",
    "uề": "ʷe",
    "uể": "ʷe",
    "uễ": "ʷe",
    "uệ": "ʷe",
    "uơ": "ʷɤ",
    "uớ": "ʷɤ",
    "uờ": "ʷɤ",
    "uở": "ʷɤ",
    "uỡ": "ʷɤ",
    "uợ": "ʷɤ",
    "uy": "ʷi",
    "uý": "ʷi",
    "uỳ": "ʷi",
    "uỷ": "ʷi",
    "uỹ": "ʷi",
    "uỵ": "ʷi",
    "uya": "ʷiə",
    "uyá": "ʷiə",
    "uyà": "ʷiə",
    "uyả": "ʷiə",
    "uyã": "ʷiə",
    "uyạ": "ʷiə",
    "uyê": "ʷiə",
    "uyế": "ʷiə",
    "uyề": "ʷiə",
    "uyể": "ʷiə",
    "uyễ": "ʷiə",
    "uyệ": "ʷiə",
    "uyu": "ʷiu",
    "uyú": "ʷiu",
    "uyù": "ʷiu",
    "uyủ": "ʷiu",
    "uyũ": "ʷiu",
    "uyụ": "ʷiu",
    "uyu": "ʷiu",
    "uýu": "ʷiu",
    "uỳu": "ʷiu",
    "uỷu": "ʷiu",
    "uỹu": "ʷiu",
    "uỵu": "ʷiu",
    "oen": "ʷen",
    "oén": "ʷen",
    "oèn": "ʷen",
    "oẻn": "ʷen",
    "oẽn": "ʷen",
    "oẹn": "ʷen",
    "oet": "ʷet",
    "oét": "ʷet",
    "oèt": "ʷet",
    "oẻt": "ʷet",
    "oẽt": "ʷet",
    "oẹt": "ʷet",
}

Cus_onoffglides = {
    "oe": "ɛj",
    "oé": "ɛj",
    "oè": "ɛj",
    "oẻ": "ɛj",
    "oẽ": "ɛj",
    "oẹ": "ɛj",
    "oai": "aj",
    "oái": "aj",
    "oài": "aj",
    "oải": "aj",
    "oãi": "aj",
    "oại": "aj",
    "oay": "ăj",
    "oáy": "ăj",
    "oày": "ăj",
    "oảy": "ăj",
    "oãy": "ăj",
    "oạy": "ăj",
    "oao": "aw",
    "oáo": "aw",
    "oào": "aw",
    "oảo": "aw",
    "oão": "aw",
    "oạo": "aw",
    "oeo": "ew",
    "oéo": "ew",
    "oèo": "ew",
    "oẻo": "ew",
    "oẽo": "ew",
    "oẹo": "ew",
    "oeo": "ew",
    "óeo": "ew",
    "òeo": "ew",
    "ỏeo": "ew",
    "õeo": "ew",
    "ọeo": "ew",
    "ueo": "ew",
    "uéo": "ew",
    "uèo": "ew",
    "uẻo": "ew",
    "uẽo": "ew",
    "uẹo": "ew",
    "uai": "aj",
    "uái": "aj",
    "uài": "aj",
    "uải": "aj",
    "uãi": "aj",
    "uại": "aj",
    "uay": "ăj",
    "uáy": "ăj",
    "uày": "ăj",
    "uảy": "ăj",
    "uãy": "ăj",
    "uạy": "ăj",
    "uây": "ɤ̆j",
    "uấy": "ɤ̆j",
    "uầy": "ɤ̆j",
    "uẩy": "ɤ̆j",
    "uẫy": "ɤ̆j",
    "uậy": "ɤ̆j",
}

Cus_codas = {
    "p": "p",
    "t": "t",
    "c": "k",
    "m": "m",
    "n": "n",
    "ng": "ŋ",
    "nh": "ɲ",
    "ch": "tʃ",
}

Cus_tones_p = {
    "á": 5,
    "à": 2,
    "ả": 4,
    "ã": 3,
    "ạ": 6,
    "ấ": 5,
    "ầ": 2,
    "ẩ": 4,
    "ẫ": 3,
    "ậ": 6,
    "ắ": 5,
    "ằ": 2,
    "ẳ": 4,
    "ẵ": 3,
    "ặ": 6,
    "é": 5,
    "è": 2,
    "ẻ": 4,
    "ẽ": 3,
    "ẹ": 6,
    "ế": 5,
    "ề": 2,
    "ể": 4,
    "ễ": 3,
    "ệ": 6,
    "í": 5,
    "ì": 2,
    "ỉ": 4,
    "ĩ": 3,
    "ị": 6,
    "ó": 5,
    "ò": 2,
    "ỏ": 4,
    "õ": 3,
    "ọ": 6,
    "ố": 5,
    "ồ": 2,
    "ổ": 4,
    "ỗ": 3,
    "ộ": 6,
    "ớ": 5,
    "ờ": 2,
    "ở": 4,
    "ỡ": 3,
    "ợ": 6,
    "ú": 5,
    "ù": 2,
    "ủ": 4,
    "ũ": 3,
    "ụ": 6,
    "ứ": 5,
    "ừ": 2,
    "ử": 4,
    "ữ": 3,
    "ự": 6,
    "ý": 5,
    "ỳ": 2,
    "ỷ": 4,
    "ỹ": 3,
    "ỵ": 6,
}

Cus_gi = {"gi": "zi", "gí": "zi", "gì": "zi", "gì": "zi", "gĩ": "zi", "gị": "zi"}

Cus_qu = {
    "quy": "kwi",
    "qúy": "kwi",
    "qùy": "kwi",
    "qủy": "kwi",
    "qũy": "kwi",
    "qụy": "kwi",
}


################################################3
import sys, codecs, re
from io import StringIO
from optparse import OptionParser
from string import punctuation
from vinorm import TTSnorm
# import prosodic as p


def trans(word, dialect, glottal, pham, cao, palatals):
    # Custom
    onsets, nuclei, codas, onglides, offglides, onoffglides, qu, gi = (
        Cus_onsets,
        Cus_nuclei,
        Cus_codas,
        Cus_onglides,
        Cus_offglides,
        Cus_onoffglides,
        Cus_qu,
        Cus_gi,
    )

    if pham or cao:
        # Custom
        tones_p = Cus_tones_p

        tones = tones_p

    ons = ""
    nuc = ""
    cod = ""
    ton = 0
    oOffset = 0
    cOffset = 0
    l = len(word)

    if l > 0:
        if word[0:3] in onsets:  # if onset is 'ngh'
            ons = onsets[word[0:3]]
            oOffset = 3
        elif word[0:2] in onsets:  # if onset is 'nh', 'gh', 'kʷ' etc
            ons = onsets[word[0:2]]
            oOffset = 2
        elif word[0] in onsets:  # if single onset
            ons = onsets[word[0]]
            oOffset = 1

        if word[l - 2 : l] in codas:  # if two-character coda
            cod = codas[word[l - 2 : l]]
            cOffset = 2
        elif word[l - 1] in codas:  # if one-character coda
            cod = codas[word[l - 1]]
            cOffset = 1

        # if word[0:2] == u'gi' and cod and len(word) == 3:  # if you just have 'gi' and a coda...
        if (
            word[0:2] in gi and cod and len(word) == 3
        ):  # if you just have 'gi' and a coda...
            nucl = "i"
            ons = "z"
        else:
            nucl = word[oOffset : l - cOffset]

        if nucl in nuclei:
            if oOffset == 0:
                if glottal == 1:
                    if word[0] not in onsets:  # if there isn't an onset....
                        ons = "ʔ" + nuclei[nucl]  # add a glottal stop
                    else:  # otherwise...
                        nuc = nuclei[nucl]  # there's your nucleus
                else:
                    nuc = nuclei[nucl]  # there's your nucleus
            else:  # otherwise...
                nuc = nuclei[nucl]  # there's your nucleus

        elif nucl in onglides and ons != "kw":  # if there is an onglide...
            nuc = onglides[nucl]  # modify the nuc accordingly
            if ons:  # if there is an onset...
                ons = ons + "w"  # labialize it, but...
            else:  # if there is no onset...
                ons = "w"  # add a labiovelar onset

        elif nucl in onglides and ons == "kw":
            nuc = onglides[nucl]

        elif nucl in onoffglides:
            cod = onoffglides[nucl][-1]
            nuc = onoffglides[nucl][0:-1]
            if ons != "kw":
                if ons:
                    ons = ons + "w"
                else:
                    ons = "w"
        elif nucl in offglides:
            cod = offglides[nucl][-1]
            nuc = offglides[nucl][:-1]

        elif word in gi:  # if word == 'gi', 'gì',...
            ons = gi[word][0]
            nuc = gi[word][1]

        elif word in qu:  # if word == 'quy', 'qúy',...
            ons = qu[word][:-1]
            nuc = qu[word][-1]

        else:
            # Something is non-Viet
            return (None, None, None, None)

        # Velar Fronting (Northern dialect)
        if dialect == "n":
            if nuc == "a":
                if cod == "k" and cOffset == 2:
                    nuc = "ɛ"
                if cod == "ɲ" and nuc == "a":
                    nuc = "ɛ"

            # Final palatals (Northern dialect)
            if nuc not in ["i", "e", "ɛ"]:
                if cod == "ɲ":
                    cod = "ɲ"  # u'ŋ'
            elif palatals != 1 and nuc in ["i", "e", "ɛ"]:
                if cod == "ɲ":
                    cod = "ɲ"  # u'ŋ'
            if palatals == 1:
                if cod == "k" and nuc in ["i", "e", "ɛ"]:
                    cod = "c"

        # Velar Fronting (Southern and Central dialects)
        else:
            if nuc in ["i", "e"]:
                if cod == "k":
                    cod = "t"
                if cod == "ŋ":
                    cod = "n"

            # There is also this reverse fronting, see Thompson 1965:94 ff.
            elif nuc in ["iə", "ɯə", "uə", "u", "ɯ", "ɤ", "o", "ɔ", "ă", "ɤ̆"]:
                if cod == "t":
                    cod = "k"
                if cod == "n":
                    cod = "ŋ"

        # Monophthongization (Southern dialects: Thompson 1965: 86; Hoàng 1985: 181)
        if dialect == "s":
            if cod in ["m", "p"]:
                if nuc == "iə":
                    nuc = "i"
                if nuc == "uə":
                    nuc = "u"
                if nuc == "ɯə":
                    nuc = "ɯ"

        # Tones
        # Modified 20 Sep 2008 to fix aberrant 33 error
        tonelist = [tones[word[i]] for i in range(0, l) if word[i] in tones]
        if tonelist:
            ton = str(tonelist[len(tonelist) - 1])
        else:
            if not (pham or cao):
                if dialect == "c":
                    ton = str("35")
                else:
                    ton = str("33")
            else:
                ton = str("1")

        # Modifications for closed syllables
        if cOffset != 0:
            # Obstruent-final nang tones are modal voice
            if (
                (dialect == "n" or dialect == "s")
                and ton == "21g"
                and cod in ["p", "t", "k"]
            ):
                # if ton == u'21\u02C0' and cod in ['p', 't', 'k']: # fixed 8 Nov 2016
                ton = "21"

            # Modification for sắc in closed syllables (Northern and Central only)
            if (
                (dialect == "n" and ton == "24") or (dialect == "c" and ton == "13")
            ) and cod in ["p", "t", "k"]:
                ton = "45"

            # Modification for 8-tone system
            if cao == 1:
                if ton == "5" and cod in ["p", "t", "k"]:
                    ton = "5b"
                if ton == "6" and cod in ["p", "t", "k"]:
                    ton = "6b"

            # labialized allophony (added 17.09.08)
            if nuc in ["u", "o", "ɔ"]:
                if cod == "ŋ":
                    cod = "ŋ͡m"
                if cod == "k":
                    cod = "k͡p"

        return (ons, nuc, cod, ton)


def convert(word, dialect, glottal, pham, cao, palatals, delimit):
    """Convert a single orthographic string to IPA."""

    ons = ""
    nuc = ""
    cod = ""
    ton = 0
    seq = ""

    try:
        (ons, nuc, cod, ton) = trans(word, dialect, glottal, pham, cao, palatals)
        if None in (ons, nuc, cod, ton):
            seq = "[" + word + "]"
        else:
            seq = delimit + delimit.join(filter(None, (ons, nuc, cod, ton))) + delimit
    except TypeError:
        pass

    return seq


########################333
from vinorm import *
from underthesea import word_tokenize
import eng_to_ipa

syms = [
    "ɯəj",
    "ɤ̆j",
    "ʷiə",
    "ɤ̆w",
    "ɯəw",
    "ʷet",
    "iəw",
    "uəj",
    "ʷen",
    "tʰw",
    "ʷɤ̆",
    "ʷiu",
    "kwi",
    "ŋ͡m",
    "k͡p",
    "cw",
    "jw",
    "uə",
    "eə",
    "bw",
    "oj",
    "ʷi",
    "vw",
    "ăw",
    "ʈw",
    "ʂw",
    "aʊ",
    "fw",
    "ɛu",
    "tʰ",
    "tʃ",
    "ɔɪ",
    "xw",
    "ʷɤ",
    "ɤ̆",
    "ŋw",
    "ʊə",
    "zi",
    "ʷă",
    "dw",
    "eɪ",
    "aɪ",
    "ew",
    "iə",
    "ɣw",
    "zw",
    "ɯj",
    "ʷɛ",
    "ɯw",
    "ɤj",
    "ɔ:",
    "əʊ",
    "ʷa",
    "mw",
    "ɑ:",
    "hw",
    "ɔj",
    "uj",
    "lw",
    "ɪə",
    "ăj",
    "u:",
    "aw",
    "ɛj",
    "iw",
    "aj",
    "ɜ:",
    "kw",
    "nw",
    "t∫",
    "ɲw",
    "eo",
    "sw",
    "tw",
    "ʐw",
    "iɛ",
    "ʷe",
    "i:",
    "ɯə",
    "dʒ",
    "ɲ",
    "θ",
    "ʌ",
    "l",
    "w",
    "1",
    "ɪ",
    "ɯ",
    "d",
    "∫",
    "p",
    "ə",
    "u",
    "o",
    "3",
    "ɣ",
    "!",
    "ð",
    "ʧ",
    "6",
    "ʒ",
    "ʐ",
    "z",
    "v",
    "g",
    "ă",
    "_",
    "æ",
    "ɤ",
    "2",
    "ʤ",
    "i",
    ".",
    "ɒ",
    "b",
    "h",
    "n",
    "ʂ",
    "ɔ",
    "ɛ",
    "k",
    "m",
    "5",
    " ",
    "c",
    "j",
    "x",
    "ʈ",
    ",",
    "4",
    "ʊ",
    "s",
    "ŋ",
    "a",
    "ʃ",
    "?",
    "r",
    ":",
    "η",
    "f",
    ";",
    "e",
    "t",
    "'",
]


def normEng(eng, delemit):
    return eng
    # x= p.Text(eng)
    # x.parse()
    # PAR = str(x.bestParses()[0]).split("|")
    # SYL = x.syllables()
    # if len(PAR) != len(SYL):
    #     print("check dif len: ", eng)
    #     result="/"+"/".join(list(eng))
    #     return result
    # result = ""
    # for i,syl in enumerate(SYL):
    #     syllable = str(syl).replace("'","").replace("ː","").replace("ɑ","a")
    #     if PAR[i].lower().upper() == PAR[i]:
    #         result+=syllable+"'5"+" "
    #     else:
    #         result+=syllable+"'1"+" "
    # result=result.rstrip(" ")
    # if delemit !="":
    #     takemore=""
    #     for r in result:
    #         if r in syms:
    #             takemore+=delemit+r
    #     result=takemore
    # return result


def Parsing(listParse, text, delimit):
    undefine_symbol = "'"
    if listParse == "default":
        listParse = [
            "ɯəj",
            "ɤ̆j",
            "ʷiə",
            "ɤ̆w",
            "ɯəw",
            "ʷet",
            "iəw",
            "uəj",
            "ʷen",
            "tʰw",
            "ʷɤ̆",
            "ʷiu",
            "kwi",
            "ŋ͡m",
            "k͡p",
            "cw",
            "jw",
            "uə",
            "eə",
            "bw",
            "oj",
            "ʷi",
            "vw",
            "ăw",
            "ʈw",
            "ʂw",
            "aʊ",
            "fw",
            "ɛu",
            "tʰ",
            "tʃ",
            "ɔɪ",
            "xw",
            "ʷɤ",
            "ɤ̆",
            "ŋw",
            "ʊə",
            "zi",
            "ʷă",
            "dw",
            "eɪ",
            "aɪ",
            "ew",
            "iə",
            "ɣw",
            "zw",
            "ɯj",
            "ʷɛ",
            "ɯw",
            "ɤj",
            "ɔ:",
            "əʊ",
            "ʷa",
            "mw",
            "ɑ:",
            "hw",
            "ɔj",
            "uj",
            "lw",
            "ɪə",
            "ăj",
            "u:",
            "aw",
            "ɛj",
            "iw",
            "aj",
            "ɜ:",
            "kw",
            "nw",
            "t∫",
            "ɲw",
            "eo",
            "sw",
            "tw",
            "ʐw",
            "iɛ",
            "ʷe",
            "i:",
            "ɯə",
            "dʒ",
            "ɲ",
            "θ",
            "ʌ",
            "l",
            "w",
            "1",
            "ɪ",
            "ɯ",
            "d",
            "∫",
            "p",
            "ə",
            "u",
            "o",
            "3",
            "ɣ",
            "!",
            "ð",
            "ʧ",
            "6",
            "ʒ",
            "ʐ",
            "z",
            "v",
            "g",
            "ă",
            "_",
            "æ",
            "ɤ",
            "2",
            "ʤ",
            "i",
            ".",
            "ɒ",
            "b",
            "h",
            "n",
            "ʂ",
            "ɔ",
            "ɛ",
            "k",
            "m",
            "5",
            " ",
            "c",
            "j",
            "x",
            "ʈ",
            ",",
            "4",
            "ʊ",
            "s",
            "ŋ",
            "a",
            "ʃ",
            "?",
            "r",
            ":",
            "η",
            "f",
            ";",
            "e",
            "t",
            "'",
        ]
    listParse.sort(reverse=True, key=len)
    output = ""
    skip = 0
    for ic, char in enumerate(text):
        ##print(char,skip)
        check = 0
        if skip > 0:
            skip = skip - 1
            continue
        for l in listParse:
            if len(l) <= len(text[ic:]) and l == text[ic : ic + len(l)]:
                output += delimit + l
                check = 1
                skip = len(l) - 1
                break
        if check == 0:
            # Case symbol not in list
            if str(char) in ["ˈ", "ˌ", "*"]:
                continue
            # print("this is not in symbol :"+ char+":")
            output += delimit + undefine_symbol
    return output.rstrip() + delimit


def T2IPA_split(text, delimit):
    sys.path.append("./Rules")  # make sure we can find the Rules files
    # Setup option
    glottal = 0
    pham = 0
    cao = 0
    palatals = 0
    tokenize = 0
    dialect = "n"  # "c""s"
    tone_type = 0
    if tone_type == 0:
        pham = 1
    else:
        cao = 1
    # Input text
    line = text
    if line == "\n":
        return ""
    else:
        compound = ""
        ortho = ""
        words = line.split()
        ## toss len==0 junk
        words = [word for word in words if len(word) > 0]
        ## hack to get rid of single hyphens or underscores
        words = [word for word in words if word != "-"]
        words = [word for word in words if word != "_"]
        for i in range(0, len(words)):
            word = words[i].strip()
            ortho += word
            word = word.strip(punctuation).lower()
            ## 29.03.16: check if tokenize is true
            ## if true, call this routine for each substring
            ## and re-concatenate
            if (tokenize and "-" in word) or (tokenize and "_" in word):
                substrings = re.split(r"(_|-)", word)
                values = substrings[::2]
                delimiters = substrings[1::2] + [""]
                ipa = [
                    convert(x, dialect, glottal, pham, cao, palatals, delimit).strip()
                    for x in values
                ]
                seq = "".join(v + d for v, d in zip(ipa, delimiters))
            else:
                seq = convert(
                    word, dialect, glottal, pham, cao, palatals, delimit
                ).strip()
            # concatenate
            if len(words) >= 2:
                ortho += " "
            if i < len(words) - 1:
                seq = seq + " "
            compound = compound + seq
        return compound


def T2IPA(text):
    sys.path.append("./Rules")  # make sure we can find the Rules files
    # Setup option
    glottal = 0
    pham = 0
    cao = 0
    palatals = 0
    tokenize = 0
    delimit = ""
    dialect = "n"  # "c""s"
    tone_type = 0
    if tone_type == 0:
        pham = 1
    else:
        cao = 1
    # Input text
    line = text
    if line == "\n":
        return ""
    else:
        compound = ""
        ortho = ""
        words = line.split()
        ## toss len==0 junk
        words = [word for word in words if len(word) > 0]
        ## hack to get rid of single hyphens or underscores
        words = [word for word in words if word != "-"]
        words = [word for word in words if word != "_"]
        for i in range(0, len(words)):
            word = words[i].strip()
            ortho += word
            word = word.strip(punctuation).lower()
            ## 29.03.16: check if tokenize is true
            ## if true, call this routine for each substring
            ## and re-concatenate
            if (tokenize and "-" in word) or (tokenize and "_" in word):
                substrings = re.split(r"(_|-)", word)
                values = substrings[::2]
                delimiters = substrings[1::2] + [""]
                ipa = [
                    convert(x, dialect, glottal, pham, cao, palatals, delimit).strip()
                    for x in values
                ]
                seq = "".join(v + d for v, d in zip(ipa, delimiters))
            else:
                seq = convert(
                    word, dialect, glottal, pham, cao, palatals, delimit
                ).strip()
            # concatenate
            if len(words) >= 2:
                ortho += " "
            if i < len(words) - 1:
                seq = seq + " "
            compound = compound + seq
        return compound


EN = {
    "a": "ây",
    "ă": "á",
    "â": "ớ",
    "b": "bi",
    "c": "si",
    "d": "đi",
    "đ": "đê",
    "e": "i",
    "ê": "ê",
    "f": "ép",
    "g": "giy",
    "h": "ếch",
    "i": "ai",
    "j": "giây",
    "k": "cây",
    "l": "eo",
    "m": "em",
    "n": "en",
    "o": "âu",
    "ô": "ô",
    "ơ": "ơ",
    "p": "pi",
    "q": "kiu",
    "r": "a",
    "s": "ét",
    "t": "ti",
    "u": "diu",
    "ư": "ư",
    "v": "vi",
    "w": "đắp liu",
    "x": "ít",
    "y": "quai",
    "z": "giét",
}
import re


def vi2IPA_split(texts, delimit):
    content = []
    with open(imp.find_module("viphoneme")[1] + "/Popular.txt", encoding="utf-8") as f:
        content = f.read().splitlines()
    tess = texts.split(".")
    Results = ""
    for text in tess:
        # print("------------------------------------------------------")
        TN = TTSnorm(text)
        # TN=text
        # print("------------------------------------------------------")
        # print("Text normalize:              ",TN)
        TK = word_tokenize(TN)
        # print("Vietnamese Tokenize:         ",TK)

        for iuv, under_valid in enumerate(TK):
            token_under = under_valid.split(" ")
            checkinvalid = 0
            ##print(token_under)
            if len(token_under) > 1:
                for tok in token_under:
                    if tok not in content or "[" in T2IPA(tok):
                        checkinvalid = 1
            if checkinvalid == 1:
                TK = TK[:iuv] + TK[iuv + 1 :]
                for tok in reversed(token_under):
                    TK.insert(iuv, tok)

        IPA = ""

        for tk in TK:
            ipa = T2IPA_split(tk, delimit).replace(" ", "_")
            if ipa == "":
                IPA += delimit + tk + delimit + " "
            elif ipa[0] == "[" and ipa[-1] == "]":
                eng = eng_to_ipa.convert(tk)
                if eng[-1] == "*":
                    if tk.lower().upper() == tk:
                        ##print("ENGLISH",tk)
                        # Đọc tiếng anh từng chữ
                        letter2sound = ""
                        for char in tk:
                            CHAR = str(char).lower()
                            if CHAR in list(EN.keys()):
                                letter2sound += EN[CHAR] + " "
                            else:
                                letter2sound += char + " "
                        IPA += T2IPA_split(letter2sound, delimit) + " "
                    else:
                        # Giữ nguyên
                        # Future: test experiment" Nếu từ unknow có thể dùng eng_norm để chuyển qua thay thế chứ không cần giữ nguyên như này
                        IPA += Parsing("default", tk.lower(), delimit) + " "
                else:
                    # This use for version english not splited by syllable
                    # IPA+=Parsing("default",eng,delimit)+" "
                    # This version will split english to each syllable
                    IPA += normEng(tk, delimit) + delimit + " "

                # Check tu dien tieng anh Etrain bưc
                # Neu co Mapping
                # Neu khong, check co nguyen am
                # Neu co de nguyen
                # Neu khong danh van
                # print("                                    ..................Out of domain word: " ,ipa)
            else:
                IPA += ipa + " "
        IPA = re.sub(delimit + "+", delimit, IPA)
        IPA = re.sub(" +", " ", IPA)
        # print("IPA Vietnamese:             ",IPA)
        # print("------------------------------------------------------")
        Results += IPA.rstrip() + " " + delimit + "." + delimit + " "

    return Results.rstrip()


def vi2IPA(text):
    # Bỏ phần này để hoạt động với window
    TN = TTSnorm(text)
    # Chuẩn hóa lại, tuy nhiên phần xử lý ngày tháng năm phải fix lại bằng text
    # text = text.lower()

    TK = word_tokenize(TN)
    # print("Vietnamese Tokenize:         ",TK)

    # Trong trường hợp word_tokenize sai
    new_TK = []
    for word in TK:
        new_TK.extend(word.split())
    TK = new_TK

    IPA = ""
    for tk in TK:
        ipa = T2IPA(tk).replace(" ", "_")
        if ipa == "":
            IPA += tk + " "
        elif ipa[0] == "[" and ipa[-1] == "]":
            eng = eng_to_ipa.convert(tk)
            if eng[-1] == "*":
                if tk.lower().upper() == tk:
                    # Đọc tiếng anh từng chữ
                    letter2sound = ""
                    for char in tk:
                        CHAR = str(char).lower()
                        if CHAR in list(EN.keys()):
                            letter2sound += EN[CHAR] + " "
                        else:
                            letter2sound += char + " "
                    IPA += T2IPA_split(letter2sound, "") + " "
                else:
                    # Giữ nguyên
                    IPA += Parsing("default", tk, "") + " "
            else:
                IPA += eng + " "
            # Check tu dien tieng anh Etrain bưc
            # Neu co Mapping
            # Neu khong, check co nguyen am
            # Neu co de nguyen
            # Neu khong danh van
            # print("                                    ..................Out of domain word: " ,ipa)
        else:
            IPA += ipa + " "
    IPA = re.sub(" +", " ", IPA)
    # print("IPA Vietnamese:             ",IPA)
    # print("------------------------------------------------------")
    return IPA
