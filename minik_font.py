from font import Column, Character, zero_width_joiner, Font

minik_font = Font({
    'A': Character(
        Column(" xxxxx"),
        Column("x  x  "),
        Column(" xxxxx"),
    ),
    'b': Character(
        Column("xxxxxx"),
        Column("   x x"),
        Column("    x "),
    ),
    zero_width_joiner: Character(Column("      "), Column("      ")),
    ' ': Character(Column("      "), Column("      ")),
})

for name, character in minik_font.characters.items():
    if name not in [zero_width_joiner, ' ']:
        print(name)
        print(character)
    print()

minik_font.print("Ab Abbbbb")