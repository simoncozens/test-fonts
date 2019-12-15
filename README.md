OpenType Test Fonts
===================

The [OpenType specification](https://docs.microsoft.com/en-gb/typography/opentype/spec/) is amazing! It describes a huge range of things you can do inside OpenType fonts, and tells you everything you need to implement that functionality.

But sometimes you just want someone else to do it for you. If you're working on color font support, or vertical typesetting, or mathematics, or justification, you just want an example font you can poke about with, take apart, or try in your application.

That's what this repository is for.

## Fonts available

###  [`CFF-Outlines.otf`](https://github.com/simoncozens/test-fonts/blob/master/CFF-Outlines.otf)

This contains the glyphs `A` and `B` in PostScript ([CFF](https://docs.microsoft.com/en-gb/typography/opentype/spec/cff)) outlines. The glyphs handily tell you that they are CFF-based.

*If you see some gobbledegook below, go [here](https://simoncozens.github.io/test-fonts/) to see this site in its full glory.*

<style>
    .testfont { margin: 20px; padding:5px; border: 1px dotted black; background-color: #efefef; font-size:80px; }
    @font-face {
        font-family: "CFF Outlines";
        src: url(https://github.com/simoncozens/test-fonts/blob/master/CFF-Outlines.otf?raw=true);
    }
</style>

<div class="testfont" style="font-family:'CFF Outlines'">
A B
</div>

### [`TrueType-Outlines.ttf`](https://github.com/simoncozens/test-fonts/blob/master/TrueType-Outlines.ttf)

This contains the glyphs `A` and `B` in TrueType ([`glyf` table](https://docs.microsoft.com/en-gb/typography/opentype/spec/glyf)) outlines. The glyphs handily tell you that they are `glyf`-based.

<style>
    @font-face {
        font-family: "TrueType Outlines";
        src: url(https://github.com/simoncozens/test-fonts/blob/master/TrueType-Outlines.ttf?raw=true);
    }
</style>

<div class="testfont" style="font-family:'TrueType Outlines'">
A B
</div>

### [`CFF-and-TrueType-Together.otf`](https://github.com/simoncozens/test-fonts/blob/master/CFF-and-TrueType-Together.otf)

This contains the glyphs `A` and `B`, but with *both* `CFF` and `glyf` tables. The sfnt wrapper has an OpenType (`OTTO`) magic number.

<style>
    @font-face {
        font-family: "CFF and TrueType Together OTF";
        src: url(https://github.com/simoncozens/test-fonts/blob/master/CFF-and-TrueType-Together.otf?raw=true);
    }
</style>

<div class="testfont" style="font-family:'CFF and TrueType Together OTF'">
A B
</div>

### [`CFF-and-TrueType-Together.ttf`](https://github.com/simoncozens/test-fonts/blob/master/CFF-and-TrueType-Together.ttf)

This contains the glyphs `A` and `B`, but with *both* `CFF` and `glyf` tables. The sfnt wrapper has a TrueType (`\01\00\00\00`) magic number.

<style>
    @font-face {
        font-family: "CFF and TrueType Together TTF";
        src: url(https://github.com/simoncozens/test-fonts/blob/master/CFF-and-TrueType-Together.ttf?raw=true);
    }
</style>

<div class="testfont" style="font-family:'CFF and TrueType Together TTF'">
A B
</div>

### [`CFF-Outlines-and-COLR.otf`](https://github.com/simoncozens/test-fonts/blob/master/CFF-Outlines-and-COLR.otf)

This contains the glyphs `A` and `B`, with CFF outlines but also with color font ([`COLR`](https://docs.microsoft.com/en-gb/typography/opentype/spec/colr) / [`CPAL`](https://docs.microsoft.com/en-gb/typography/opentype/spec/cpal) table format). The color outlines handily tell you that they are COLR-based.

<style>
    @font-face {
        font-family: "CFF and COLR";
        src: url(https://github.com/simoncozens/test-fonts/blob/master/CFF-Outlines-and-COLR.otf?raw=true);
    }
</style>

<div class="testfont" style="font-family:'CFF and COLR'">
A B
</div>

### [`CFF-Outlines-and-SVG.otf`](https://github.com/simoncozens/test-fonts/blob/master/CFF-Outlines-and-SVG.otf)

This contains the glyphs `A` and `B`, with CFF outlines but also with [`SVG`](https://docs.microsoft.com/en-gb/typography/opentype/spec/svg) outlines. The color outlines handily tell you that they are SVG-based.

<style>
    @font-face {
        font-family: "CFF and SVG";
        src: url(https://github.com/simoncozens/test-fonts/blob/master/CFF-Outlines-and-SVG.otf?raw=true);
    }
</style>

<div class="testfont" style="font-family:'CFF and SVG'">
A B
</div>

### [`CFF-COLR-and-SVG.otf`](https://github.com/simoncozens/test-fonts/blob/master/CFF-COLR-and-SVG.otf)

This contains the glyphs `A` and `B`, with CFF outlines but also with [`SVG`](https://docs.microsoft.com/en-gb/typography/opentype/spec/svg) *and* [`COLR`](https://docs.microsoft.com/en-gb/typography/opentype/spec/colr) / [`CPAL`](https://docs.microsoft.com/en-gb/typography/opentype/spec/cpal) outlines. Which outlines will your rendering software show? Place your bets now!

<style>
    @font-face {
        font-family: "CFF COLR and SVG";
        src: url(https://github.com/simoncozens/test-fonts/blob/master/CFF-COLR-and-SVG.otf?raw=true);
    }
</style>

<div class="testfont" style="font-family:'CFF COLR and SVG'">
A B
</div>

### [`CFF-and-SBIX.otf`](https://github.com/simoncozens/test-fonts/blob/master/CFF-and-SBIX.otf)

This contains the glyphs `A` and `B` with CFF outlines, but also with [`sbix`](https://docs.microsoft.com/en-gb/typography/opentype/spec/sbix) ("Apple colour") bitmaps for the glyph "A". Four strikes (bitmap sizes) are provided: 512, 256, 128 and 64. Each bitmap describes its own size.

<style>
    @font-face {
        font-family: "CFF and SBIX";
        src: url(https://github.com/simoncozens/test-fonts/blob/master/CFF-and-SBIX.otf?raw=true);
    }
</style>

<div class="testfont" style="font-family:'CFF and SBIX'">
A B
</div>