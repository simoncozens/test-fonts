from fontParts.world import *
f = OpenFont("Fallback Plus Source.ufo")
from youseedee import ucd_data

# First generate glyphs in all positions
hexes = "0123456789ABCDEF"

for h in hexes:
   g = f.layers[0].newGlyph("_two_"+h)
   g.appendComponent("_one_"+h, offset=(300,0))

   g = f.layers[0].newGlyph("_three_"+h)
   g.appendComponent("_one_"+h, offset=(0,-250))

   g = f.layers[0].newGlyph("_four_"+h)
   g.appendComponent("_one_"+h, offset=(300,-250))

   g = f.layers[0].newGlyph("_five_"+h)
   g.appendComponent("_one_"+h, offset=(0,-500))

   g = f.layers[0].newGlyph("_six_"+h)
   g.appendComponent("_one_"+h, offset=(300,-500))

# Generate spare glyphs for substitutions etc.
for l in "0123456789":
  for r in "0123456789":
    g = f.layers[0].newGlyph("glyph"+l+r)
    g.appendComponent("_spare")
    g.appendComponent("_one_"+l)
    g.appendComponent("_two_"+r)
    g.width = 600

# Now generate U+xx glyphs
for l in hexes:
  for r in hexes:
    g = f.layers[0].newGlyph("_uplus"+l+r)
    g.appendComponent("_uplus")
    g.appendComponent("_one_"+l)
    g.appendComponent("_two_"+r)

# Now generate U+xxxx real glyphs

for one in hexes:
  for two in hexes:
    print("Generating %s%sXX" % (one,two))
    for three in hexes:
      for four in hexes:
        codepoint = int(one+two+three+four,16)
        if not "Name" in ucd_data(codepoint): continue
        if codepoint == 0x20: continue
        g = f.layers[0].newGlyph("uni"+one+two+three+four)
        g.unicode = codepoint
        g.appendComponent("_uplus"+one+two)
        g.appendComponent("_three_"+three)
        g.appendComponent("_four_"+four)
        g.width = 600

f.save("Fallback Plus.ufo")
