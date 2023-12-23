from icecream import ic

strings = [
    "",
    "Krankheit: ",
    "Krankheit: Starker Husten",
]

for string in strings:
    new_string = string.replace("Krankheit: ", "")
    ic(new_string)
