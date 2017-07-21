#!/usr/bin/env python3
import sys
from os.path import join, splitext

class FileInfo:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.fullpath = join(parent, name)
        self.ftype = self._file_type(name)
        
    def _file_type(self, name):
        a = splitext(name)
        if len(a) > 1:
            return a[-1][1:].lower()
        else:
            return None
        
    def __str__(self):
        return "-".join([self.name, self.fullpath])
        


