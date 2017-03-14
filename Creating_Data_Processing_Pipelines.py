#-*- coding:utf-8 -*-
import bz2,gzip
import os
import fnmatch
import re

def gen_find(filepat,top):
    for dirpath, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist,filepat):
            yield os.path.join(dirpath,name)

def gen_opnener(filenames):
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename,'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename,'rt')
        else:
            f = open(filename,'rt')
        yield f
        f.close()

def gen_concatenate(iterators):
    for t in iterators:
        yield from t

def gen_grep(pattern,lines):
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line

