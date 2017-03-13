#-*- coding:utf-8 -*-
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

if __name__ == '__main__':
    p = PriorityQueue()
    bar = Item('bar')
    foo = Item('foo')
    kou = Item('kou')
    kng = Item('kng')
    p.push(kng,1)
    p.push(kou,3)
    p.push(bar,2)
    p.push(foo,2)
    print(p.pop())
    print(p.pop())
    print(p.pop())
    print(p.pop())