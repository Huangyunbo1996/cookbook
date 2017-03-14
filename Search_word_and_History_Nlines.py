#-*- coding:utf-8 -*-
from collections import deque


class LinesHistory:
    
    def __init__(self,lines,nlines=3):
        self._lines = lines
        self.history = deque(maxlen=nlines)
    
    def __iter__(self):
        for nline,line in enumerate(self._lines,start=1):
            self.history.append((nline,line))
            yield line


if __name__ == '__main__':
    with open('...\test.txt','r') as f:
        history = LinesHistory(f)
        for line in history:
            if 'python' in line:
                for nnline,lline in history.history:
                    print('%d:%s'%(nnline,lline))