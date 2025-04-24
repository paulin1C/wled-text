from font import Column, Character

characters = {
    'a': Character(
        Column("x x x "),
        Column(" x x x")
    ),
    'b': Character(
        Column("xxxxxx")
    )
}

for name, character in characters.items():
    print(name)
    print(character)