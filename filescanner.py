#!/usr/bin/env python3
import sys
import os
from os.path import join, getsize, splitext
from fileinfo import FileInfo

class FileScanner:
    """"""
    def __init__(self, start, bps=True):
        self.start = start

    def files_in(self, interested):
        for root, dirs, files in os.walk(self.start):
            for name in files:
                if self.is_interested(name, interested):
                    finfo = FileInfo(root, name)
                    print(finfo)

    def _file_is_format(self, name, fmt):
        a = splitext(name)
        if len(a) > 1:
            return a[1][1:].lower() == fmt.lower()
        else:
            return False

    def is_interested(self, name, interested):
        for fmt in interested:
            if self._file_is_format(name, fmt):
                return True
        return False
        

def main():
    fscanner = FileScanner('/Users/zhouyan/Documents/Technology/C++')
    fscanner.files_in(['pdf'])

if __name__ == '__main__':
    main()

