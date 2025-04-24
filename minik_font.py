from font import Column, Character, zero_width_joiner, Font

"""
example character to copy-paste:
'': Character(
        Column(""),
        Column(""),
        Column(""),
        Column(""),
    ),
"""

minik_font = Font({
    
    # numbers
    '0': Character(
        Column(" xxxx "),
        Column("x    x"),
        Column("x    x"),
        Column(" xxxx "),
    ),
    '1': Character(
        Column("  x   "),
        Column(" x   x"),
        Column("xxxxxx"),
        Column("     x"),
    ),
    '2': Character(
        Column(" x  xx"),
        Column("x  x x"),
        Column("x  x x"),
        Column(" xx  x"),
    ),
    '3': Character(
        Column(" x  x "),
        Column("x    x"),
        Column("x x  x"),
        Column(" x xx "),
    ),
    '4': Character(
        Column("  xx  "),
        Column(" x x  "),
        Column("xxxxxx"),
        Column("   x  "),
    ),
    '$': Character( # this, too, is 4, but different. haven't decided which one I like more yet
        Column("xxxx  "),
        Column("   x  "),
        Column("  xxxx"),
        Column("   x  "),
    ),
    '5': Character(
        Column("xxx x "),
        Column("x x  x"),
        Column("x x  x"),
        Column("x  xx "),
    ),
    '6': Character(
        Column(" xxxx "),
        Column("x x  x"),
        Column("x x  x"),
        Column("   xx "),
    ),
    '7': Character(
        Column("x     "),
        Column("x  xxx"),
        Column("x x   "),
        Column("xx    "),
    ),
    '8': Character(
        Column(" x xx "),
        Column("x x  x"),
        Column("x x  x"),
        Column(" x xx "),
    ),
    '9': Character(
        Column(" xx   "),
        Column("x  x x"),
        Column("x  x x"),
        Column(" xxxx "),
    ),

    # uppercase letters
    'A': Character(
        Column(" xxxxx"),
        Column("x  x  "),
        Column(" xxxxx"),
    ),

    # lowercase letters
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

#minik_font.print("Ab Abbbbb")