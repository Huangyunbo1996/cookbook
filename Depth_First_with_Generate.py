#-*- coding:utf-8 -*-

class Node:
    def __init__(self,node):
        self._node = node
        self._children = []

    def add_child(self,node):
        self._children.append(node)

    def __repr__(self):
        return '<Node:{!r}>'.format(self._node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


if __name__ == '__main__':
    root = Node(1)
    child1 = Node(4)
    child2 = Node(3)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(9))
    child2.add_child(Node(6))
    child2.add_child(Node(5))
    
    for c in root.depth_first():
        print(c)
        #Output:
               #<Node:1>
               #<Node:4>
               #<Node:9>
               #<Node:3>
               #<Node:6>
               #<Node:5>