#!/usr/bin/env python3
import sys
from os.path import join

class FileInfo:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.fullpath = join(parent, name)

    def __str__(self):
        return "-".join([self.name, self.fullpath])
        


