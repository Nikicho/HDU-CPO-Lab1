# define hashmap
'''
1. define listBuckets of hashmap
2. hash mapping function
3. insert a node
4. delete a node
'''


# give the inserting node a key
def hash_Function(node, length):
    if(node == None):
        return 0
    key = node.value % length
    node.key = key
    return key

# insert the node into the head of hasmap
def insert_hash(node, buckets):
    key = hash_Function(node, len(buckets))
    node.key = key
    return  append_node(buckets[key], node)

# remove hashnode
def remove_hash(node, buckets):
    key = hash_Function(node, len(buckets))
    remove_node = remove(buckets[key], node.value)
    if remove_node:
        return 1
    else:
        return 0

# get the length of list and the item of list is node
def list_size(list):
    if list is None:
        return 0
    else:
        return 1 + list_size(list.next)

# add a new node to the head of liked_list
def cons(head, tail):
    return Node(head, tail)

# add a new node to the hail of liked_list
def append_node(lst,nod):
    if lst==None:
        lst=nod
        return  lst
    else:
        cur= lst
        cur1 =lst.next
        while cur1 is not None:
            cur=cur1
            cur1=cur.next
        cur.next=nod
        return lst


#  delete the value of element of the list
def remove(node, element):
    assert node is not None, "element should be in list"
    if node.value == element:
        return node.next
    else:
        return cons(node.value, remove(node.next, element))


# get the value of the node
def head(node):
    assert type(node) is Node
    return node.value


# get the next node
def tail(node):
    assert type(node) is Node
    return node.next


# reverse the linked_list
def reverse(node, acc=None):
    if node is None:
        return acc
    return reverse(tail(node), Node(head(node), acc))

# return a empty object
def empty():
    return None

#concat node1 and node2
def mconcat(node1, node2):
    if node1 is None:
        return node2
    tmp = reverse(node1)
    res = node2
    while tmp is not None:
        res = cons(tmp.value, res)
        tmp = tmp.next
    return res

# change the linked_list to list[]
def to_list(node):
    res = []
    cur = node
    while cur is not None:
        res.append(cur.value)
        cur = cur.next
    return res

# change hasmap to list[]
def hasmap_to_list(buket):
    res=[]
    for s in buket:
        cur = s.next
        lst = to_list(cur)
        res.append(lst)
    return res

# change list[] to the linked_list
def from_list(lst):
    res = None
    for e in lst:
        res = append_node(res, Node(e,None))
    return res

# change the Built-in list to hashmap
def from_hashmap(bukets, testdata):
    for s in testdata:
        for t in s:
            insert_hash(Node(t,None), bukets)
    return bukets


def iterator(lst):
    cur = lst
    def foo():
        nonlocal cur
        if cur is None: raise StopIteration
        tmp = cur.value
        cur = cur.next
        return tmp
    return foo


class Node(object):
    def __init__(self, value, next):
        """node constructor"""
        self.key = None
        self.value = value
        self.next = next

    def __repr__(self):
        if self.key != None:
            return "<Node key: %d data: %d>" % (self.key, self.value)
        else:
            return "<Node key: %s data: %d>" % (self.key, self.value)

    def __str__(self):
        """for str() implementation"""
        if type(self.next) is Node:
            return "{} : {}".format(self.value, self.next)
        return str(self.value)

    def __eq__(self, other):
        """for write assertion, we should be abel for check list equality (list are equal, if all elements are equal)."""
        if other is None:
            return False
        if self.value != other.value:
            return False
        return self.next == other.next


if __name__ == '__main__':
    n1 = Node(0, None)
    n2 = Node(2, None)
    n1 = Node(3, Node(6, Node(9, None)))
    cur1 = n1
    while cur1 is not None:
        cur1.key = 0
        cur1 = cur1.next
    n2 = Node(4, Node(7, Node(10, None)))
    cur2 = n2
    while cur2 is not None:
        cur2.key = 1
        cur2 = cur2.next
    n3 = Node(5, Node(8, Node(11, None)))
    cur3 = n3
    while cur3 is not None:
        cur3.key = 3
        cur3 = cur3.next
    buckets2 = [
        Node(0, n1),
        Node(1, n2),
        Node(2, n3),
    ]
    res=hasmap_to_list(buckets2)
    print(res)





