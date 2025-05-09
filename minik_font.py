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
        Column(" x  xx"),
        Column(" x x x"),
        Column("  xxxx"),
    ),
    'b': Character(
        Column("xxxxxx"),
        Column("   x x"),
        Column("    x "),
    ),
    'c': Character(
        Column("  xxx "),
        Column(" x   x"),
        Column("  x x "),
    ),
    'd': Character(
        Column("    x "),
        Column("   x x"),
        Column("xxxxxx"),
    ),
    'e': Character(
        Column("  xxx "),
        Column(" x x x"),
        Column("  x  x"),
    ),
    'f': Character(
        Column("  x   "),
        Column("xxxxxx"),
        Column("x x   "),
    ),
    'g': Character(
        Column("  x  x"),
        Column(" x x x"),
        Column("  xxx "),
    ),
    'h': Character(
        Column("xxxxxx"),
        Column("   x  "),
        Column("   xxx"),
    ),
    'i': Character(
        Column(" x xxx"),
    ),
    'j': Character(
        Column("     x"),
        Column(" x xxx"),
    ),
    'k': Character(
        Column("xxxxxx"),
        Column("    x "),
        Column("   x x"),
    ),
    'l': Character(
        Column("xxxxx "),
        Column("     x"),
        Column("    x "),
    ),
    'm': Character(
        Column("  xxxx"),
        Column("   x  "),
        Column("  x   "),
        Column("   x  "),
        Column("  x   "),
        Column("   xxx"),
    ),
    'n': Character(
        Column("  xxxx"),
        Column("   x  "),
        Column("  x   "),
        Column("   xxx")
    ),
    'o': Character(
        Column("   xx "),
        Column("  x  x"),
        Column("   xx "),
    ),
    'p': Character(
        Column(" xxxxx"),
        Column(" x x  "),
        Column("  x   "),
    ),
    'q': Character(
        Column("  x   "),
        Column(" x x  "),
        Column(" xxxxx"),
    ),
    'r': Character(
        Column("  xxxx"),
        Column("   x  "),
        Column("  x   "),
    ),
    's': Character( # this is a cursive s... trust me, it is
        Column("  x x "),
        Column(" x   x"),
        Column("  x  x"),
        Column("   xx "),
    ),     
    't': Character(
        Column(" x    "),
        Column("xxxxxx"),
        Column(" x   x"),
    ),
    'u': Character(
        Column(" xxxx "),
        Column("     x"),
        Column("     x"),
        Column(" xxxx "),
    ),
    'v': Character(
        Column(" xxxx "),
        Column("     x"),
        Column(" xxxx "),
    ),
    'w': Character(
        Column(" xxxx "),
        Column("     x"),
        Column("    x "),
        Column("     x"),
        Column(" xxxx "),
    ),
    'x': Character(
        Column(" x   x"),
        Column("  x x "),
        Column("   x  "),
        Column("  x x "),
        Column(" x   x"),
    ),
    'y': Character(
        Column(" xx   "),
        Column("   xxx"),
        Column(" xx   "),
    ),
    'z': Character(
        Column(" x  xx"),
        Column(" x x x"),
        Column(" xx  x"),
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

#minik_font.display("16:29")