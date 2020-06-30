#!/home/Nancy/anaconda3/bin/python

# ------------------------------------------------------------------------
# Change History
# May-June 2020 Nancy Schorr - reworked

from __future__ import print_function
import sys
import json
import datetime
from time import strftime, strptime
import re
from get_tapi import GetTapi
import get_tapi
import regex


class RemJunk:
    ## must use capital U for 8 chars, lowercase u for four
    def __init__(self):
        self.todays = datetime.datetime.now().strftime('%F%H%M%S')
        self.encode = 'utf-8'

    def strip_emoji(self, tline0):
        #re_emoji = re.compile(u'([\U000D000A])|([\U0000000D])|([\U0000000A])|([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
        #re_emoji = re.compile(u'([\U000D000A])|([\U0000000D])|([\U0000000A])|([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
        # https://stackoverflow.com/questions/26568722/remove-unicode-emoji-using-re-in-python

        rep1 = re.compile(r"\\r\\n", re.ASCII)   ## \\n working!!!!
        rep2 = re.compile(r"\\n", re.ASCII)   ## \\n working!!!!
        rep3 = re.compile(r"\\f", re.ASCII)   ## \\n working!!!!
        rep4 = re.compile(r"\\t", re.ASCII)   ## \\n working!!!!
        # rep5a = re.compile(r"\\", re.ASCII)   ## \\n working!!!!
        #rep6 = re.compile(u'([\U00000200-\U0001FFFF])|([\U00010000-\U0001ffFF]))')
        # rep6 = re.compile(u'([\u00AF-\uFFFF])')
        rep6 = re.compile(u'([\ud83d])')

        # rep6 = re.compile(u'([\U00010000-\U0001FFFF])')
        # \ud83d\udcaa
        tline1 = rep1.sub('', tline0)
        tline2 = rep2.sub('', tline1)
        tline3 = rep3.sub('', tline2)
        tline4 = rep4.sub('', tline3)
        # tline5a = rep5a.sub('$$$$$$$', tline4)
        tline6 = rep6.sub('', tline4)
        return tline6

    # "id_str": "1276498949654880256", "full_text": "\ud83d\udcaa
    # dirtyline = self.strip_emoji('"id_str": "1276498949654880256", "full_text": "\ud83d\udcaa"')


    def clean_json_file2(self, fname_read, fname_write):
        with open(fname_write, 'w+', encoding=self.encode) as write_file:
            with open(fname_read, 'r', encoding=self.encode) as read_file:
                emoji_line = read_file.readline()
                print("orig: \n" + emoji_line + ": END: \n\n")
                clean_line = self.strip_emoji(emoji_line)
                print("\nHERE: \n" + clean_line)
                write_file.writelines(clean_line)
        return 0

    def clean_json_file(self, fname_read, fname_write):
        with open(fname_write, 'w+', encoding=self.encode) as write_file:
            with open(fname_read, 'r', encoding=self.encode) as read_file:
                for tline in read_file:
                    print("old line: \n" + tline + ": END: \n\n")
                    clean_line = self.strip_emoji(tline)
                    print("\nCleaned: \n" + clean_line)
                    write_file.writelines(clean_line)

            print("\n\n" + fname_write)

        return 0

    def main(self, in_file, out_file):
        # results = self.clean_json_file(in_file, out_file)  # twitter api - tapi
        # print(results)
        dline = '"id_str": "1276498949654880256", "full_text": "\ud83d\udcaa"'
        rep1 = re.compile(r"\\r\\n", re.ASCII)
        cline = rep1.sub('', dline)

        print(cline)
        print()

if __name__ == '__main__':
    RemJunkObj = RemJunk()  # make the class object for nuls
    # infile = 'nulsjson/nulsRPSjun29parta.json'
    infile = 'intest.json'
    outfile = 'nulsRPSjun29partaclean.json'
    RemJunkObj.main(infile, outfile)

