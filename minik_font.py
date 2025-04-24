from font import Column, Character, zero_width_joiner, Font

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
        Column("xxxx  "),
        Column("   x  "),
        Column("  xxxx"),
        Column("   x  "),
    ),
    '$': Character( # this, too, is 4, but different
        Column("  xx  "),
        Column(" x x  "),
        Column("xxxxxx"),
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
    'B': Character(
        Column("xxxxxx"),
        Column("x x  x"),
        Column(" x xx "),
    ),
    'C': Character(
        Column(" xxxx "),
        Column("x    x"),
        Column(" x  x "),
    ),
    'D': Character(
        Column("xxxxxx"),
        Column("x    x"),
        Column(" xxxx "),
    ),
    'E': Character(
        Column("xxxxxx"),
        Column("x x  x"),
        Column("x x  x"),
    ),
    'F': Character(
        Column("xxxxxx"),
        Column("x x   "),
        Column("x x   "),
    ),
    'G': Character(
        Column(" xxxx "),
        Column("x    x"),
        Column("x  x x"),
        Column(" x xx ")
    ),
    'H': Character(
        Column("xxxxxx"),
        Column("  x   "),
        Column("xxxxxx"),
    ),
    'I': Character(
        Column("x    x"),
        Column("xxxxxx"),
        Column("x    x"),
    ),
    'J': Character(
        Column("x   x "),
        Column("x    x"),
        Column("xxxxx "),
    ),
    'K': Character(
        Column("xxxxxx"),
        Column("  x   "),
        Column(" x x  "),
        Column("x   xx"),
    ),
    'L': Character(
        Column("xxxxxx"),
        Column("     x"),
        Column("     x"),
    ),
    'M': Character(
        Column("xxxxxx"),
        Column(" x    "),
        Column("  x   "),
        Column(" x    "),
        Column("xxxxxx"),
    ),
    'N': Character(
        Column("xxxxxx"),
        Column("  x   "),
        Column("   x  "),
        Column("xxxxxx"),
    ),
    'O': Character(
        Column(" xxxx "),
        Column("x    x"),
        Column(" xxxx "),
    ),
    'P': Character(
        Column("xxxxxx"),
        Column("x x   "),
        Column(" x    "),
    ),
    'Q': Character(
        Column(" xxxx "),
        Column("x    x"),
        Column("x  x x"),
        Column("x   xx"),
        Column(" xxxxx"),
    ),
    'R': Character(
        Column("xxxxxx"),
        Column("x xx  "),
        Column("x x x "),
        Column(" x   x"),
    ),
    'S': Character(
        Column(" x  x "),
        Column("x x  x"),
        Column("x  x x"),
        Column(" x  x "),
    ),
    'T': Character(
        Column("x     "),
        Column("xxxxxx"),
        Column("x     "),
    ),
    'U': Character(
        Column("xxxxx "),
        Column("     x"),
        Column("     x"),
        Column("xxxxx "),
    ),
    'V': Character(
        Column("xxxxx "),
        Column("     x"),
        Column("xxxxx "),
    ),
    'W': Character(
        Column("xxxxxx"),
        Column("    x "),
        Column("   x  "),
        Column("    x "),
        Column("xxxxxx"),
    ),
    'X': Character(
        Column("x    x"),
        Column(" x  x "),
        Column("  xx  "),
        Column(" x  x "),
        Column("x    x"),
    ),
    'Y': Character(
        Column("xx    "),
        Column("  xxxx"),
        Column("xx    "),
    ),
    'Z': Character(
        Column("x   xx"),
        Column("x  x x"),
        Column("x x  x"),
        Column("xx   x"),
    ),

    # lowercase letters
    'a': Character(
        Column(""),
        Column(""),
        Column(""),
    ),
    'b': Character(
        Column("xxxxxx"),
        Column("   x x"),
        Column("    x "),
    ),

    # special characters
    ':': Character(
        Column(" x  x "),
    ),
    zero_width_joiner: Character(
        Column("      "),
    ),
    ' ': Character(
        Column("      "), 
        Column("      ")
    ),
})

for name, character in minik_font.characters.items():
    if name not in [zero_width_joiner, ' ']:
        print(name)
        print(character)
    print()

minik_font.display("16:13")