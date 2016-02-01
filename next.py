#!/usr/bin/env python3
# encoding: utf-8

"""
I prefer to collect words in files called 01.txt, 02.txt, etc.
This little helper finds the filename with the largest number
in its name and increments it by one, then opens this new file
for editing.
"""

import os
import re

EDITOR = os.getenv('EDITOR')


def main():
    txts = [f for f in os.listdir(".") if re.search(r'^\d+\.txt$', f)]
    txts.sort(key=lambda fname: int(fname.split(".")[0]))
    try:
        fname = txts[-1]
        new_name = "{}.txt".format(int(fname.split(".")[0]) + 1)
    except IndexError:
        new_name = '01.txt'
    cmd = "{ed} {fname}".format(ed=EDITOR, fname=new_name)
#    print(cmd)
    os.system(cmd)
    print("# file name: {}".format(new_name))

##############################################################################

if __name__ == "__main__":
    main()
