"""
@author: Shi Wenhao
"""
#hash number
def hash_Function(node, length):
    if(node == None):
        return 0
    flag = node.val % length
    node.flag = flag
    return flag

# add an element
def add_hash(node, buckets):
    flag = hash_Function(node, len(buckets))
    node.flag = flag
    return  append_node(buckets[flag], node)

# remove
def remove_hash(node, buckets):
    flag = hash_Function(node, len(buckets))
    remove_node = remove(buckets[flag], node.val)
    if remove_node:
        return 1
    else:
        return 0

# get length
def list_size(list):
    if list is None:
        return 0
    else:
        return 1 + list_size(list.nxt)

# add a new node to the head of liked_list
def list_add(head, nextNode):
    return Node(head, nextNode)

# add a new node to the nextNode of liked_list
def append_node(lst,nod):
    if lst==None:
        lst=nod
        return  lst
    else:
        cur= lst
        cur1 =lst.nxt
        while cur1 is not None:
            cur=cur1
            cur1=cur.nxt
        cur.nxt=nod
        return lst


#  delete a node of the list
def remove(node, x):
    assert node is not None, "x should be in list"
    if node.val == x:
        return node.nxt
    else:
        return list_add(node.val, remove(node.nxt, x))


# get the val of the node
def head(node):
    assert type(node) is Node
    return node.val


# get the nxt node
def nextNode(node):
    assert type(node) is Node
    return node.nxt


# reverse the linked_list
def reverse(node, acc=None):
    if node is None:
        return acc
    return reverse(nextNode(node), Node(head(node), acc))

def empty():
    return None

#concat node1 and node2
def mconcat(node1, node2):
    if node1 is None:
        return node2
    tmp = reverse(node1)
    res = node2
    while tmp is not None:
        res = list_add(tmp.val, res)
        tmp = tmp.nxt
    return res

# linked_list to list[]
def to_list(node):
    res = []
    cur = node
    while cur is not None:
        res.append(cur.val)
        cur = cur.nxt
    return res

# hasmap to list[]
def hasmap_to_list(buket):
    res=[]
    for s in buket:
        cur = s.nxt
        lst = to_list(cur)
        res.append(lst)
    return res

#list[] to the linked_list
def from_list(lst):
    res = None
    for e in lst:
        res = append_node(res, Node(e,None))
    return res

# Built-in list to hashmap
def to_hashmap(bukets, testdata):
    for s in testdata:
        for t in s:
            add_hash(Node(t,None), bukets)
    return bukets


def iterator(lst):
    cur = lst
    def foo():
        nonlocal cur
        if cur is None: raise StopIteration
        tmp = cur.val
        cur = cur.nxt
        return tmp
    return foo


class Node(object):
    def __init__(self, val, nxt):
        """node list_addtructor"""
        self.flag = None
        self.val = val
        self.nxt = nxt

    def __repr__(self):
        if self.flag != None:
            return "flag:%d;data:%d" % (self.flag, self.val)
        else:
            return "flag:%s;data:%d" % (self.flag, self.val)

    def __str__(self):
        if type(self.nxt) is Node:
            return "{} : {}".format(self.val, self.nxt)
        return str(self.val)

    def __eq__(self, other):
        if other is None:
            return False
        if self.val != other.val:
            return False
        return self.nxt == other.nxt


if __name__ == '__main__':
    n1 = Node(0, None)
    n2 = Node(2, None)
    n1 = Node(3, Node(6, Node(9, None)))
    cur1 = n1
    while cur1 is not None:
        cur1.flag = 0
        cur1 = cur1.nxt
    n2 = Node(4, Node(7, Node(10, None)))
    cur2 = n2
    while cur2 is not None:
        cur2.flag = 1
        cur2 = cur2.nxt
    n3 = Node(5, Node(8, Node(11, None)))
    cur3 = n3
    while cur3 is not None:
        cur3.flag = 3
        cur3 = cur3.nxt
    buckets2 = [
        Node(0, n1),
        Node(1, n2),
        Node(2, n3),
    ]
    res=hasmap_to_list(buckets2)
    print(res)





