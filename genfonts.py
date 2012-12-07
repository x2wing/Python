#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   genfonts.py
#
#   Copyright (c) 2012, Nikita Volchenkov <nikitavolchenkov@gmail.com>
#   All rights reserved.
#
#   Redistribution and use in source and binary forms, with or without
#   modification, are permitted provided that the following conditions are met:
#
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#   AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#   IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#   ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
#   LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#   CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#   SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#   INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#   CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#   ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#   POSSIBILITY OF SUCH DAMAGE.


# Python 3 compatibility imports
from __future__ import print_function

import sys
import os
import argparse
import fontforge


# Error exit codes
(EX_INTERRUPT, EX_GENFAIL) = range(1, 3)
# Output filetype
(FT_OTF, FT_TTF, FT_CAD) = range(3)


def generate_font(sfdfile, type=FT_OTF, outdir=None):
    font = fontforge.open(sfdfile)
    if outdir is None:
        fontprefix = os.path.splitext(sfdfile)[0]
    else:
        fontprefix = os.path.join(outdir,
                os.path.basename(os.path.splitext(sfdfile)[0]))


    if type == FT_TTF:
        font.familyname = font.familyname + " TT"
        splitname = font.fullname.split()
        splitname.insert(-1, "TT")
        font.fullname = " ".join(splitname)
        splitname = font.fontname.split("-")
        splitname.insert(-1, "TT-")
        font.fontname = "".join(splitname)
        try:
            font.generate(fontprefix+".ttf", flags=("opentype", "old-kern",
                    "PfEd-colors", "PfEd-lookups"))
        except EnvironmentError, e:
            print("!!! %s" % e, file=sys.stderr)
            sys.exit(EX_GENFAIL)
    elif type == FT_CAD:
        font.familyname = font.familyname + " DS"
        splitname = font.fullname.split()
        splitname.insert(-1, "DS")
        font.fullname = " ".join(splitname)
        splitname = font.fontname.split("-")
        splitname.insert(-1, "DS-")
        font.fontname = "".join(splitname)
        # Copy reference to DIAMETER_SIGN into LATIN_SMALL_LETTER_O_WITH_STROKE
        font.selection.select(0x2300)
        font.copyReference()
        font.selection.select(0x00d8)
        font.paste()
        font.selection.select(0x00f8)
        font.paste()
        # Output file name
        outfile = os.path.dirname(fontprefix) + font.fontname + ".ttf"
        try:
            font.generate(outfile, flags=("opentype", "old-kern",
                    "PfEd-colors", "PfEd-lookups"))
        except EnvironmentError, e:
            print("!!! %s" % e, file=sys.stderr)
            sys.exit(EX_GENFAIL)
    else:
        try:
            font.generate(fontprefix+".otf", flags=("opentype", "PfEd-colors",
                    "PfEd-lookups"))
        except EnvironmentError, e:
            print("!!! %s" % e, file=sys.stderr)
            sys.exit(EX_GENFAIL)

    font.close()


def main():
    parser = argparse.ArgumentParser(description="Generate OpenType or "
            "TrueType font files from FontForge sources")
    parser.add_argument("file", nargs="+", help="One or more FontForge files "
            "to generate from")
    parser.add_argument("-o", "--opentype", dest="type", action="store_const",
            const=FT_OTF, help="Generate OpenType fonts. This is the default "
            "action")
    parser.add_argument("-t", "--truetype", dest="type", action="store_const",
            const=FT_TTF, help="Generate TrueType fonts")
    parser.add_argument("-c", "--cad", dest="type", action="store_const",
            const=FT_CAD, help="Generate TrueType fonts with special "
            "behaviour for CAD programs like DraftSight or BricsCAD")
    parser.add_argument("-d", "--output-dir", help="Place generated font files "
            "into specified dir")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s "
            "0.3")
    args = parser.parse_args()

    for i in args.file:
        generate_font(i, args.type, args.output_dir)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(EX_INTERRUPT)

