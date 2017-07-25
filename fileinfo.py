#!/usr/bin/env python3
import sys
import re
from os.path import join, splitext

class FileInfo:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.fullpath = join(parent, name)
        self.ftype = self._file_type(name)
        self.tags = self._get_tags()
        self.url = self._get_url()

    def _get_url(self):
        return re.sub('/Users/zhouyan', 'http://192.168.0.104:8088', self.fullpath)
        
    def _get_tags(self):
        return list(filter(lambda x: len(x) > 0, re.split('[_\-, \.]', self.name)))
        
    def _file_type(self, name):
        a = splitext(name)
        if len(a) > 1:
            return a[-1][1:].lower()
        else:
            return None
        
    def __str__(self):
        return "-".join([self.name, self.url])+" tags :"+" ".join(self.tags)
        


