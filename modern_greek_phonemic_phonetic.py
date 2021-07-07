import re

voiced_consonants_and_vowels = "β|γ|δ|ζ|λ|ν|ρ|ντ|μπ|ϊ|ει|η|υ|υι|οι|ε|αι|α|ο|ω|ου|ΐ|ή|ύ|υί|οί|έ|αί|ά|ό|ώ|ού"
vowels = "ϊ|ει|η|υ|υι|οι|ε|αι|α|ο|ω|ου|ΐ|ή|ύ|υί|οί|έ|αί|ά|ό|ώ|ού"

ita_vowel_stressed = "ΐ|ί|εί|ή|ύ|υί|οί"
ita_vowel_unstressed = "ϊ|ι|ει|η|υ|υι|οι"

epsilon_vowel_stressed = "έ|αί"
epsilon_vowel_unstressed = "ε|αι"

alpha_vowel_stressed = "ά"
alpha_vowel_unstressed = "α"

omicron_vowel_stressed = "ό|ώ"
omicron_vowel_unstressed = "ο|ω"

ou_vowel_stressed = "ού"
ou_vowel_unstressed = "ου"


greek_ipa_vowels = "i|e|a|o|u|e̞|o̞|í|é|á|ó|ú|é̞|ó̞"
greek_ipa_vowels_stressed = "í|é|á|ó|ú|é̞|ó̞"
greek_ipa_vowels_unstressed = "i|e|a|o|u|e̞|o̞"
greek_ipa_front_vowels = "i|e|í|é"


greek_ipa_consonants = "ɣ|g|v|ð|k|c|p|b|t|x|f|θ|m|n|l|r|s|s̠|z|z̠|ɟ|ʝ|ɲ|ŋ|ɱ|ç|ʎ"
greek_ipa_voiced_consonants = "ɣ|v|b|ð|d|m|n|l|r|z"
greek_ipa_unvoiced_consonants = "k|p|t|x|f|θ|s"

greek_ipa_stop_consonants = "g|k|b|p|d|t"
greek_ipa_velar_consonants = "g|ɣ|k|x"
greek_ipa_velar_stop_consonants = "g|k"
greek_ipa_velar_fricative_consonants = "ɣ|x"
greek_ipa_palatal_fricative_consonants = "ç|j|ʝ"
greek_ipa_palatal_stop_consonants = "c|ɟ"


pattern1 = f"({greek_ipa_vowels_unstressed})({greek_ipa_consonants})({greek_ipa_consonants})({greek_ipa_vowels_stressed})"
new_pattern1 = r"\1\2ˈ\3\4"

pattern2 = f"({greek_ipa_vowels_unstressed})({greek_ipa_consonants})({greek_ipa_vowels_stressed})"
new_pattern2 = r"\1ˈ\2\3"

pattern3 = f"(\s{greek_ipa_consonants})({greek_ipa_consonants})({greek_ipa_vowels_stressed})"
new_pattern3 = r"ˈ\1\2\3"

pattern4 = f"^({greek_ipa_consonants})({greek_ipa_consonants})({greek_ipa_vowels_stressed})"
new_pattern4 = r"ˈ\1\2\3"

pattern5 = f"({greek_ipa_vowels_unstressed})({greek_ipa_vowels_stressed})"
new_pattern5 = r"\1ˈ\2"

pattern6 = f"^({greek_ipa_consonants})({greek_ipa_vowels_stressed})"
new_pattern6 = r"ˈ\1\2"

pattern7 = f"^({greek_ipa_vowels_stressed})"
new_pattern7 = r"ˈ\1"

pattern8 = f"(\s)({greek_ipa_vowels_stressed})"
new_pattern8 = r"\1ˈ\2"

pattern9 = f"({greek_ipa_vowels_unstressed})"
new_pattern9 = r"\1"



pattern11 = "í"
new_pattern11 = "i"

pattern12 = "é̞"
new_pattern12 = "e̞"

pattern13 = "á"
new_pattern13 = "a"

pattern14 = "ó̞"
new_pattern14 = "o̞"

pattern15 = "ú"
new_pattern15 = "u"

greek_patterns_case_and_stress = [

##making_everything_lowercase_START###

    [re.compile("Β"), "β"],
    [re.compile("Γ"), "γ"],
    [re.compile("Δ"), "δ"],
    [re.compile("Ζ"), "ζ"],
    [re.compile("Θ"), "θ"],
    [re.compile("Κ"), "κ"],
    [re.compile("Λ"), "λ"],
    [re.compile("Μ"), "μ"],
    [re.compile("Ν"), "ν"],
    [re.compile("Ξ"), "ξ"],
    [re.compile("Π"), "π"],
    [re.compile("Ρ"), "ρ"],
    [re.compile("Σ"), "σ"],
    [re.compile("Τ"), "τ"],
    [re.compile("Φ"), "φ"],
    [re.compile("Χ"), "χ"],
    [re.compile("Ψ"), "ψ"],

    [re.compile("Ϊ"), "ϊ"],
    [re.compile("Ι"), "ι"],
    [re.compile("Ί"), "ί"],
    [re.compile("Ἴ"), "ί"],
    [re.compile("Ἵ"), "ί"],
    [re.compile("Ἲ"), "ί"],
    [re.compile("Ἳ"), "ί"],
    [re.compile("Ἶ"), "ί"],
    [re.compile("Ἷ"), "ί"],
    [re.compile("Ὶ"), "ί"],
    [re.compile("Ἰ"), "ί"],
    [re.compile("Ἱ"), "ί"],

    [re.compile("Υ"), "υ"],
    [re.compile("῎Υ"), "ύ"],
    [re.compile("Ὕ"), "ύ"],
    [re.compile("῍Υ"), "ύ"],
    [re.compile("Ὓ"), "ύ"],
    [re.compile("῏Υ"), "ύ"],
    [re.compile("Ὗ"), "ύ"],
    [re.compile("῀Υ"), "ύ"],
    [re.compile("Ὺ"), "ύ"],

    [re.compile("᾽Υ"), "υ"],
    [re.compile("Ὑ"), "υ"],

    [re.compile("Η"), "η"],
    [re.compile("Ἤ"), "ή"],
    [re.compile("Ἥ"), "ή"],
    [re.compile("Ἢ"), "ή"],
    [re.compile("Ἣ"), "ή"],
    [re.compile("Ἦ"), "ή"],
    [re.compile("Ἧ"), "ή"],
    [re.compile("῀Η"), "ή"],
    [re.compile("Ὴ"), "ή"],

    [re.compile("῀ιΗ"), "ή"],
    [re.compile("´ͅΗ"), "ή"],
    [re.compile("ῌ"), "η"],

    [re.compile("Ἡ"), "η"],
    [re.compile("Ἠ"), "η"],

    [re.compile("Ε"), "ε"],
    [re.compile("Ἔ"), "έ"],
    [re.compile("Ἕ"), "έ"],
    [re.compile("Ἒ"), "έ"],
    [re.compile("Ἓ"), "έ"],
    [re.compile("Ὲ"), "έ"],

    [re.compile("Ἐ"), "ε"],
    [re.compile("Ἑ"), "ε"],


    [re.compile("Α"), "α"],
    [re.compile("Ἄ"), "ά"],
    [re.compile("Ἅ"), "ά"],
    [re.compile("Ἂ"), "ά"],
    [re.compile("Ἃ"), "ά"],
    [re.compile("Ἆ"), "ά"],
    [re.compile("Ἇ"), "ά"],
    [re.compile("῀Α"), "ά"],
    [re.compile("Ὰ"), "ά"],

    [re.compile("῀ιΑ"), "ά"],
    [re.compile("´ͅΑ"), "ά"],
    [re.compile("ᾼ"), "α"],

    [re.compile("Ἀ"), "α"],
    [re.compile("Ἁ"), "α"],

    [re.compile("Ο"), "ο"],
    [re.compile("Ὄ"), "ό"],
    [re.compile("Ὅ"), "ό"],
    [re.compile("Ὂ"), "ό"],
    [re.compile("Ὃ"), "ό"],
    [re.compile("Ὸ"), "ό"],

    [re.compile("Ὀ"), "ο"],
    [re.compile("Ὁ"), "ο"],

    [re.compile("Ω"), "ω"],
    [re.compile("Ὤ"), "ώ"],
    [re.compile("Ὥ"), "ώ"],
    [re.compile("Ὤ"), "ώ"],
    [re.compile("Ὣ"), "ώ"],
    [re.compile("Ὦ"), "ώ"],
    [re.compile("Ὧ"), "ώ"],
    [re.compile("῀Ω"), "ώ"],
    [re.compile("Ὼ"), "ώ"],

    [re.compile("῀ιΩ"), "ώ"],
    [re.compile("´ͅΩ"), "ώ"],
    [re.compile("ῼ"), "ω"],

    [re.compile("Ὠ"), "ω"],
    [re.compile("Ὡ"), "ω"],


#making_everything_lowercase_END

#regularise_accents_to_modern_stress_START#

    [re.compile("οἴ"), "οί"],
    [re.compile("οἵ"), "οί"],
    [re.compile("οἲ"), "οί"],
    [re.compile("οἳ"), "οί"],
    [re.compile("οἶ"), "οί"],
    [re.compile("οἷ"), "οί"],
    [re.compile("οῖ"), "οί"],
    [re.compile("οὶ"), "οί"],

    [re.compile("οἱ"), "οι"],
    [re.compile("οἰ"), "οι"],

    [re.compile("εἴ"), "εί"],
    [re.compile("εἵ"), "εί"],
    [re.compile("εἲ"), "εί"],
    [re.compile("εἳ"), "εί"],
    [re.compile("εἶ"), "εί"],
    [re.compile("εἷ"), "εί"],
    [re.compile("εῖ"), "εί"],
    [re.compile("εὶ"), "εί"],

    [re.compile("εἱ"), "ει"],
    [re.compile("εἰ"), "ει"],

    [re.compile("αἴ"), "αί"],
    [re.compile("αἵ"), "αί"],
    [re.compile("αἲ"), "αί"],
    [re.compile("αἳ"), "αί"],
    [re.compile("αἶ"), "αί"],
    [re.compile("αἷ"), "αί"],
    [re.compile("αῖ"), "αί"],
    [re.compile("αὶ"), "αί"],

    [re.compile("αἱ"), "αι"],
    [re.compile("αἰ"), "αι"],

    [re.compile("υἴ"), "υί"],
    [re.compile("υἵ"), "υί"],
    [re.compile("υἲ"), "υί"],
    [re.compile("υἳ"), "υί"],
    [re.compile("υἶ"), "υί"],
    [re.compile("υἷ"), "υί"],
    [re.compile("υῖ"), "υί"],
    [re.compile("υὶ"), "υί"],

    [re.compile("υἱ"), "υι"],
    [re.compile("υἰ"), "υι"],

    [re.compile("οὔ"), "ού"],
    [re.compile("οὕ"), "ού"],
    [re.compile("οὒ"), "ού"],
    [re.compile("οὓ"), "ού"],
    [re.compile("οὖ"), "ού"],
    [re.compile("οὗ"), "ού"],
    [re.compile("οῦ"), "ού"],
    [re.compile("οὺ"), "ού"],

    [re.compile("οὑ"), "ου"],
    [re.compile("οὐ"), "ου"],

    [re.compile("αὔ"), "αύ"],
    [re.compile("αὕ"), "αύ"],
    [re.compile("αὒ"), "αύ"],
    [re.compile("αὓ"), "αύ"],
    [re.compile("αὖ"), "αύ"],
    [re.compile("αὗ"), "αύ"],
    [re.compile("αῦ"), "αύ"],
    [re.compile("αὺ"), "αύ"],

    [re.compile("αὑ"), "αυ"],
    [re.compile("αὐ"), "αυ"],

    [re.compile("εὔ"), "εύ"],
    [re.compile("εὕ"), "εύ"],
    [re.compile("εὒ"), "εύ"],
    [re.compile("εὓ"), "εύ"],
    [re.compile("εὖ"), "εύ"],
    [re.compile("εὗ"), "εύ"],
    [re.compile("εῦ"), "εύ"],
    [re.compile("εὺ"), "εύ"],

    [re.compile("εὑ"), "ευ"],
    [re.compile("εὐ"), "ευ"],

    [re.compile("ἴ"), "ί"],
    [re.compile("ἵ"), "ί"],
    [re.compile("ἲ"), "ί"],
    [re.compile("ἳ"), "ί"],
    [re.compile("ἶ"), "ί"],
    [re.compile("ἷ"), "ί"],
    [re.compile("ῖ"), "ί"],
    [re.compile("ὶ"), "ί"],

    [re.compile("ἰ"), "ι"],
    [re.compile("ἱ"), "ι"],

    [re.compile("ὔ"), "ύ"],
    [re.compile("ὕ"), "ύ"],
    [re.compile("ὒ"), "ύ"],
    [re.compile("ὓ"), "ύ"],
    [re.compile("ὖ"), "ύ"],
    [re.compile("ὗ"), "ύ"],
    [re.compile("ῦ"), "ύ"],
    [re.compile("ὺ"), "ύ"],

    [re.compile("ὐ"), "υ"],
    [re.compile("ὑ"), "υ"],

    [re.compile("ἤ"), "ή"],
    [re.compile("ἥ"), "ή"],
    [re.compile("ἢ"), "ή"],
    [re.compile("ἣ"), "ή"],
    [re.compile("ἦ"), "ή"],
    [re.compile("ἧ"), "ή"],
    [re.compile("ῆ"), "ή"],
    [re.compile("ὴ"), "ή"],

    [re.compile("ῇ"), "ή"],
    [re.compile("ῄ"), "ή"],
    [re.compile("ῃ"), "η"],

    [re.compile("ἡ"), "η"],
    [re.compile("ἠ"), "η"],

    [re.compile("ἔ"), "έ"],
    [re.compile("ἕ"), "έ"],
    [re.compile("ἒ"), "έ"],
    [re.compile("ἓ"), "έ"],
    [re.compile("ὲ"), "έ"],

    [re.compile("ἐ"), "ε"],
    [re.compile("ἑ"), "ε"],

    [re.compile("ἄ"), "ά"],
    [re.compile("ἅ"), "ά"],
    [re.compile("ἂ"), "ά"],
    [re.compile("ἃ"), "ά"],
    [re.compile("ἆ"), "ά"],
    [re.compile("ἇ"), "ά"],
    [re.compile("ᾶ"), "ά"],
    [re.compile("ὰ"), "ά"],

    [re.compile("ᾷ"), "ά"],
    [re.compile("ᾴ"), "ά"],
    [re.compile("ᾳ"), "α"],

    [re.compile("ἀ"), "α"],
    [re.compile("ἁ"), "α"],

    [re.compile("ὄ"), "ό"],
    [re.compile("ὅ"), "ό"],
    [re.compile("ὂ"), "ό"],
    [re.compile("ὃ"), "ό"],
    [re.compile("ὸ"), "ό"],

    [re.compile("ὀ"), "ο"],
    [re.compile("ὁ"), "ο"],

    [re.compile("ὤ"), "ώ"],
    [re.compile("ὥ"), "ώ"],
    [re.compile("ὢ"), "ώ"],
    [re.compile("ὣ"), "ώ"],
    [re.compile("ὦ"), "ώ"],
    [re.compile("ὧ"), "ώ"],
    [re.compile("ῶ"), "ώ"],
    [re.compile("ὼ"), "ώ"],

    [re.compile("ῷ"), "ώ"],
    [re.compile("ῴ"), "ώ"],
    [re.compile("ῳ"), "ω"],

    [re.compile("ὠ"), "ω"],
    [re.compile("ὡ"), "ω"],

###regularise_accents_to_modern_stress_END###


]

greek_patterns_phonemic = [



    [re.compile("γγ"), "nk"],
    [re.compile("γξ"), "nks"],
    [re.compile("γχ"), "nx"],
    [re.compile("γι"), "i"],

    [re.compile(f"(?<=^συ)μπ"), "np"],
    [re.compile(f"(?<=^ε)μπ"), "np"],
    [re.compile(f"(?<= συ)μπ"), "np"],
    [re.compile(f"(?<= ε)μπ"), "np"],


    [re.compile(f"(?<=[{vowels}])μπ"), "mp"],
    [re.compile("μπ"), "b"],

    [re.compile(f"(?<=[{vowels}])ντ"), "nt"],
    [re.compile("ντ"), "d"],

    [re.compile(f"(?<=[{vowels}])γκ"), "nk"],
    [re.compile("γκ"), "g"],

    [re.compile("β(?=['β'])"), ""],
    [re.compile("δ(?=['δ'])"), ""],
    [re.compile("χ(?=['χ'])"), ""],
    [re.compile("φ(?=['φ'])"), ""],
    [re.compile("θ(?=['θ'])"), ""],
    [re.compile("κ(?=['κ'])"), ""],
    [re.compile("π(?=['π'])"), ""],
    [re.compile("τ(?=['τ'])"), ""],
    [re.compile("μ(?=['μ'])"), ""],
    [re.compile("ν(?=['ν'])"), ""],
    [re.compile("λ(?=['λ'])"), ""],
    [re.compile("ρ(?=['ρ'])"), ""],
    [re.compile("σ(?=['σ'])"), ""],
    [re.compile("ζ(?=['ζ'])"), ""],

    [re.compile("γ"), "ɣ"],
    [re.compile("β"), "v"],
    [re.compile("δ"), "ð"],

    [re.compile("χ"), "x"],
    [re.compile("φ"), "f"],
    [re.compile("θ"), "θ"],

    [re.compile("κ"), "k"],
    [re.compile("π"), "p"],
    [re.compile("τ"), "t"],

    [re.compile("μ"), "m"],
    [re.compile("ν"), "n"],

    [re.compile("λ"), "l"],
    [re.compile("ρ"), "r"],

    [re.compile("σ"), "s"],
    [re.compile("ς"), "s"],
    [re.compile("ζ"), "z"],

    [re.compile("ξ"), "ks"],
    [re.compile("ψ"), "ps"],


# consonants above this line ----

    [re.compile(f"ηύ(?={voiced_consonants_and_vowels})"), "ív"],
    [re.compile(f"ηυ(?={voiced_consonants_and_vowels})"), "iv"],
    [re.compile("ηύ"), "íf"],
    [re.compile("ηυ"), "if"],

    [re.compile(f"εύ(?={voiced_consonants_and_vowels})"), "é̞v"],
    [re.compile(f"ευ(?={voiced_consonants_and_vowels})"), "e̞v"],
    [re.compile("εύ"), "é̞f"],
    [re.compile("ευ"), "e̞f"],

    [re.compile(f"αύ(?={voiced_consonants_and_vowels}])"), "áv"],
    [re.compile(f"αυ(?={voiced_consonants_and_vowels})"), "av"],
    [re.compile("αύ"), "áf"],
    [re.compile("αυ"), "af"],


# diphthongs above this line ----

    [re.compile("εί"), "í"],
    [re.compile("ει"), "i"],

    [re.compile("υί"), "í"],
    [re.compile("υι"), "i"],

    [re.compile("οί"), "í"],
    [re.compile("οι"), "i"],

    [re.compile("αί"), "é"],
    [re.compile("αι"), "e"],

    [re.compile("ού"), "ú"],
    [re.compile("ου"), "u"],

    [re.compile("ΐ"), "í"],
    [re.compile("ϊ"), "i"],

    [re.compile("ί"), "í"],
    [re.compile("ι"), "i"],

    [re.compile("ή"), "í"],
    [re.compile("η"), "i"],

    [re.compile("ύ"), "í"],
    [re.compile("υ"), "i"],

    [re.compile("έ"), "é"],
    [re.compile("ε"), "e"],

    [re.compile("ά"), "á"],
    [re.compile("α"), "a"],

    [re.compile("ό"), "ó"],
    [re.compile("ο"), "o"],

    [re.compile("ώ"), "ó"],
    [re.compile("ω"), "o"],


# vowels above this line ----





]

greek_patterns_phonetic = [


    [re.compile("γγ"), "nk"],
    [re.compile("γξ"), "nks"],
    [re.compile("γχ"), "nx"],
    [re.compile("γι"), "i"],

    [re.compile(f"(?<=^συ)μπ"), "np"],
    [re.compile(f"(?<=^ε)μπ"), "np"],
    [re.compile(f"(?<=[{vowels}])μπ"), "mp"],
    [re.compile("μπ"), "b"],

    [re.compile(f"(?<=[{vowels}])ντ"), "nt"],
    [re.compile("ντ"), "d"],

    [re.compile(f"(?<=[{vowels}])γκ"), "nk"],
    [re.compile("γκ"), "g"],

    [re.compile("β(?=['β'])"), ""],
    [re.compile("δ(?=['δ'])"), ""],
    [re.compile("χ(?=['χ'])"), ""],
    [re.compile("φ(?=['φ'])"), ""],
    [re.compile("θ(?=['θ'])"), ""],
    [re.compile("κ(?=['κ'])"), ""],
    [re.compile("π(?=['π'])"), ""],
    [re.compile("τ(?=['τ'])"), ""],
    [re.compile("μ(?=['μ'])"), ""],
    [re.compile("ν(?=['ν'])"), ""],
    [re.compile("λ(?=['λ'])"), ""],
    [re.compile("ρ(?=['ρ'])"), ""],
    [re.compile("σ(?=['σ'])"), ""],
    [re.compile("ζ(?=['ζ'])"), ""],

    [re.compile("γ"), "ɣ"],
    [re.compile("β"), "v"],
    [re.compile("δ"), "ð"],

    [re.compile("χ"), "x"],
    [re.compile("φ"), "f"],
    [re.compile("θ"), "θ"],

    [re.compile("κ"), "k"],
    [re.compile("π"), "p"],
    [re.compile("τ"), "t"],

    [re.compile("μ"), "m"],
    [re.compile("ν"), "n"],

    [re.compile("λ"), "l"],
    [re.compile("ρ"), "r"],

    [re.compile("σ"), "s"],
    [re.compile("ς"), "s"],
    [re.compile("ζ"), "z"],

    [re.compile("ξ"), "ks"],
    [re.compile("ψ"), "ps"],


# PHONEMIC: consonants above this line ----

    [re.compile(f"ηύ(?={voiced_consonants_and_vowels})"), "ív"],
    [re.compile(f"ηυ(?={voiced_consonants_and_vowels})"), "iv"],
    [re.compile("ηύ"), "íf"],
    [re.compile("ηυ"), "if"],

    [re.compile(f"εύ(?={voiced_consonants_and_vowels})"), "év"],
    [re.compile(f"ευ(?={voiced_consonants_and_vowels})"), "ev"],
    [re.compile("εύ"), "éf"],
    [re.compile("ευ"), "ef"],

    [re.compile(f"αύ(?={voiced_consonants_and_vowels}])"), "áv"],
    [re.compile(f"αυ(?={voiced_consonants_and_vowels})"), "av"],
    [re.compile("αύ"), "áf"],
    [re.compile("αυ"), "af"],


# PHONEMIC: diphthongs above this line ----

    [re.compile("εί"), "í"],
    [re.compile("ει"), "i"],

    [re.compile("υί"), "í"],
    [re.compile("υι"), "i"],

    [re.compile("οί"), "í"],
    [re.compile("οι"), "i"],

    [re.compile("αί"), "é"],
    [re.compile("αι"), "e"],

    [re.compile("ού"), "ú"],
    [re.compile("ου"), "u"],

    [re.compile("ΐ"), "í"],
    [re.compile("ϊ"), "i"],

    [re.compile("ί"), "í"],
    [re.compile("ι"), "i"],

    [re.compile("ή"), "í"],
    [re.compile("η"), "i"],

    [re.compile("ύ"), "í"],
    [re.compile("υ"), "i"],

    [re.compile("έ"), "é"],
    [re.compile("ε"), "e"],

    [re.compile("ά"), "á"],
    [re.compile("α"), "a"],

    [re.compile("ό"), "ó"],
    [re.compile("ο"), "o"],

    [re.compile("ώ"), "ó"],
    [re.compile("ω"), "o"],


# PHONEMIC: vowels above this line ----





###############


    [re.compile(f"s(?={greek_ipa_voiced_consonants})"), "z"],

    [re.compile("(?<=m)p"), "b"],
    [re.compile("(?<=n)p"), "b"],

    [re.compile("(?<=m)t"), "d"],
    [re.compile("(?<=n)t"), "d"],

    [re.compile(f"ɣ(?={greek_ipa_front_vowels})"), "ʝ"],

    [re.compile(f"(?<=n)k(?={greek_ipa_front_vowels})"), "ɟ"],
    [re.compile(f"k(?={greek_ipa_front_vowels})"), "c"],
    [re.compile("(?<=n)k"), "g"],

    [re.compile(f"x(?={greek_ipa_front_vowels})"), "ç"],
    [re.compile(f"n(?={greek_ipa_velar_stop_consonants})"), "(ŋ)"],
    [re.compile(f"n(?={greek_ipa_velar_fricative_consonants})"), "ŋ"],
    [re.compile(f"n(?={greek_ipa_palatal_stop_consonants})"), "(ɲ)"],
    [re.compile(f"n(?={greek_ipa_palatal_fricative_consonants})"), "ɲ"],
    [re.compile("n(?=[bp])"), "(m)"],
    [re.compile(f"n(?={greek_ipa_stop_consonants})"), "(n)"],
    [re.compile(f"ni(?={greek_ipa_vowels})"), "ɲ"],

    [re.compile("m(?=[fv])"), "ɱ"],
    [re.compile("m(?=[bp])"), "(m)"],

    [re.compile(f"li(?={greek_ipa_vowels})"), "ʎ"],
            #some dialects have ʎ before /i/ generally:  [re.compile("l(?=['i','í'])"), "ʎ"],



# PHONETIC: consonants above this line ----

    [re.compile(f"(?<=[{greek_ipa_vowels}])u"), "w"],

    [re.compile(f"(?<=[{greek_ipa_vowels}])u"), "w"],

    [re.compile(f"(?<=[{greek_ipa_vowels}])i"), "j"],

    [re.compile(f"^i(?={greek_ipa_vowels})"), "ʝ"],
    [re.compile(f" i(?={greek_ipa_vowels})"), " ʝ"],
    [re.compile(f"(?<=m)i(?={greek_ipa_vowels})"), "ɲ"],
    [re.compile(f"(?<=[{greek_ipa_voiced_consonants}])i(?={greek_ipa_vowels})"), "ʝ"],
    [re.compile(f"(?<=[{greek_ipa_unvoiced_consonants}])i(?={greek_ipa_vowels})"), "ç"],


# PHONETIC: vowels above this line ----



    [re.compile("s"), "s̠"],
    [re.compile("z"), "z̠"],

    [re.compile("ó"), "ó̞"],
    [re.compile("o"), "o̞"],

    [re.compile("é"), "é̞"],
    [re.compile("e"), "e̞"],


# PHONETIC: final vowel-consonant phonetic conversion above this line ----




]



def transcribed_case_and_stress(word):
    """Transcribe a Greek word"""
    for pattern, replace in greek_patterns_case_and_stress:
        word = pattern.sub(replace, word)
    return word

def transcribed_phonemic(word):
    """Transcribe a Greek word"""
    for pattern, replace in greek_patterns_phonemic:
        word = pattern.sub(replace, word)
    return word


def transcribed_phonetic(word):
    """Transcribe a Greek word"""
    for pattern, replace in greek_patterns_phonetic:
        word = pattern.sub(replace, word)
    return word

def convert_stress(word):
    if re.search(pattern1, word):
        return re.sub(pattern1, new_pattern1, word)
    elif re.search(pattern2, word):
        return re.sub(pattern2, new_pattern2, word)
    elif re.search(pattern3, word):
        return re.sub(pattern3, new_pattern3, word)
    elif re.search(pattern4, word):
        return re.sub(pattern4, new_pattern4, word)
    elif re.search(pattern5, word):
        return re.sub(pattern5, new_pattern5, word)
    elif re.search(pattern6, word):
        return re.sub(pattern6, new_pattern6, word)
    elif re.search(pattern7, word):
        return re.sub(pattern7, new_pattern7, word)
    elif re.search(pattern8, word):
        return re.sub(pattern8, new_pattern8, word)
    elif re.search(pattern9, word):
        return re.sub(pattern9, new_pattern9, word)
    else:
        return word

def remove_acute(word):
    if re.search(pattern11, word):
        return re.sub(pattern11, new_pattern11, word)
    elif re.search(pattern12, word):
        return re.sub(pattern12, new_pattern12, word)
    elif re.search(pattern13, word):
        return re.sub(pattern13, new_pattern13, word)
    elif re.search(pattern14, word):
        return re.sub(pattern14, new_pattern14, word)
    elif re.search(pattern15, word):
        return re.sub(pattern15, new_pattern15, word)
    else:
        return word

def def greek_split(word):
    return word.split()

for word in greek_split(word):

    xyz = remove_acute(convert_stress(transcribed_phonetic(word)))

def main(word):

    phonemic = transcribed_phonemic(transcribed_case_and_stress(word))
    #phonetic = xyz
    ##remove_acute(convert_stress(transcribed_phonetic(transcribed_case_and_stress(word))))

    return phonemic, phonetic
