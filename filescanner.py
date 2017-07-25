#!/usr/bin/env python3
import sys
import os
from os.path import join, getsize, splitext
from fileinfo import FileInfo
from handler import DefaultHandler

class FileScanner:
    """"""
    def __init__(self, start, handler=DefaultHandler):
        self.start = start
        self.handler = handler

    def files_in(self, interested):
        for root, dirs, files in os.walk(self.start):
            for name in files:
                if self.is_interested(name, interested):
                    finfo = FileInfo(root, name)
                    self.handler.handle(finfo)

    def _file_is_format(self, name, fmt):
        a = splitext(name)
        if len(a) > 1:
            return a[-1][1:].lower() == fmt.lower()
        else:
            return False

    def is_interested(self, name, interested):
        for fmt in interested:
            if self._file_is_format(name, fmt):
                return True
        return False
        

def main():
    d = ['/Users/zhouyan/Documents/Technology/C++', '/Users/zhouyan/Documents/Technology/C']
    for path in d:
        fscanner = FileScanner(path)
        fscanner.files_in(['pdf'])

if __name__ == '__main__':
    main()

