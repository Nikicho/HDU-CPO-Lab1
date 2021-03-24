# CPO-lab1
Computational Process Organization lab1 
## title: hash-map

## group name and list of group members
- LemonVodka 
- Zhou Xinyu 
  
  - ID: s202320087
  - Email : 18126152648@163.com
  
- Shi Wenhao
 
  - ID: s202320086
  - Email: swh524457@163.com

## laboratory work number: 4

### variant description
Hash-map (collision resolution: separate chaining)
*You can use the built-in list for storing buckets and a bucket itself
*You need to check that your implementation correctly works with None value.



## synopsis 

Work by Zhou Xinyu :

1. Design and develop a mutable version
2. realize the hash-map by using the mutable version
3. This implementation of hash map, it is designed as a list, in which each element of the list is a linked list. Each element in the hash map has a flag that takes you to a specific linked list. Here you can access the first element of the list. The chain method is used to solve the conflict.

   

Work by Shi Wenhao:

1. Design and develop a immutable version

2. realize the hash-map by using the immutable version

3. The hash-map that is designed to be  n linked-lists(it is not the real one,it just makes up by the immutable node).



##  descriptions of  modules

### immutable
###### in the module immutable_test.py , we test the all method in  immutable_node.py.
###### The realized methods in the immutable_node.py:

```
#hash number
def hash_Function(node, length):

# add an element
def add_hash(node, buckets):

# remove
def remove_hash(node, buckets):

# get length
def list_size(list):

# add a new node to the head of liked_list
def list_add(head, nextNode):

# add a new node to the nextNode of liked_list
def append_node(lst,nod):

#  delete a node of the list
def remove(node, x):

# get the val of the node
def head(node):

# get the nxt node
def nextNode(node):

# reverse the linked_list
def reverse(node, acc=None):

def empty():

#concat node1 and node2
def mconcat(node1, node2):

# linked_list to list[]
def to_list(node):

# hasmap to list[]
def hasmap_to_list(buket):

#list[] to the linked_list
def from_list(lst):

# Built-in list to hashmap
def to_hashmap(bukets, testdata):

```


### mutable
###### in the module mutable_test.py , we test the all method in  mutable.py.
###### The realized methods in the mutable.py:
```

class Node(object):
    def __init__(self, value=None, next=None):

    def __repr__(self):

class LinkedList(object):
    def __init__(self, head=None):

    # 1. add
    def add_to_tail(self, node):

    def add_to_head(self, node):

    def _last_node(self):

    # 2. remove
    def remove(self, value):

    # 3. size
    def size(self):

    # 4. conversion
    def linkedlist_to_list(self):

    def linkedlist_from_list(self, lst):

    # 7. map
    def hash_map(self, f):

    # 8. reduce
    def hash_reduce(self, f, initState):
	
    # 10. iterator
    def __iter__(self):

    def __next__(self):
    def __len__(self):
    def __str__(self):
    def __repr__(self):
    
class Hashmap(object):
    def __init__(self, length=5):

    def hashFunction(self, value):


    # 1. add
    def addEle(self, node):

    # 2. remove
    def remove(self, value):

    # 4. conversion
    def hashmap_to_list(self):

    def hashmap_from_list(self, list):

    # 5. ﬁnd
    def value_find_node(self, value):

    # 6. ﬁlter
    def filter_flag(self, flag):

    # 9. mempty and mconcat
    def mempty(self):

    def mconcat(self, node1,node2):

    def __repr__(self):
```
	

## conclusion 

An immutable object is an object whose state cannot be modified after it is created.In the hash table to add, delete, search and other operations, the performance is very high
