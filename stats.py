def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        
    return file_contents

def get_num_words(text):
    return len(text.split())


# You could use a for loop to generate a set of all possible characters
# then a for loop on the set to generate the empty dictionary.
# Or you could use the same for loop below where on a first pass
# you set all the found characters as key with a value of 0 instead of +=1.
"""
num_char_dict = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "0": 0,
    " ": 0,
    "\n": 0,
    ",": 0,
    ".": 0,
    ";": 0,
    ":": 0,
    "!": 0,
    "?": 0,
    "'": 0,
    '"': 0,
    "`": 0,
    "‘": 0,
    "’": 0,
    "“": 0,
    "”": 0,
    "(": 0,
    ")": 0,
    "[": 0,
    "]": 0,
    "{": 0,
    "}": 0,
    "-": 0,
    "_": 0,
    "—": 0,
    "#": 0,
    "&": 0,
    "*": 0,
    "%": 0,
    "$": 0,
    "/": 0,
    "æ": 0,
    "â": 0,
    "ë": 0,
    "ê": 0,
    "ô": 0,
    "™": 0,
    "•": 0
}
"""
 
def get_num_char(text):
    num_char_dict = {}
    for character in text:
        num_char_dict[f"{character.lower()}"] = 0

    for character in text:
        num_char_dict[f"{character.lower()}"] += 1

    sorted_num_char_dict = dict(sorted(num_char_dict.items()))
        
    return sorted_num_char_dict


#print(get_num_char(get_book_text("books/frankenstein.txt")))
#get_num_char("alLorA")
