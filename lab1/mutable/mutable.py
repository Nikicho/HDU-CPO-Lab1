class Node(object):
    def __init__(self, data=None, next=None):
        self.key = None
        self.data = data
        self.next = next

    def __repr__(self):
        if self.key != None:
            return "<Node key: %s data: %s>" % (self.key, self.data)
        else:
            return "<Node key: %s data: %s>" % (self.key, self.data)


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.current = None

    # 1. add a new element
    def add_to_tail(self, node):
        self.current = self.head
        if self.head is None:
            self.head = node
            return self.head
        else:
            while self.current.next != None:
                self.current = self.current.next
            self.current.next = node
        return self.current

    def add_to_head(self, node):
        self.current = self.head
        if self.head is None:
            self.head = node
            return self.head
        else:
            self.head = node
            self.head.next = self.current
        return self.head

    def _last_node(self):
        assert self.head is not None
        self.current = self.head
        while self.current is not None:
            self.current = self.current.next
        return self.current

    # 2. remove an element
    def remove(self, value):
        previous = None
        self.current = self.head
        if self.current is None:
            return 'Linked List is empty, value of: %s is not here' % value
        else:
            while self.current != None:
                if self.current.data == value:
                    if len(self) is 1:
                        previous = None
                        self.current = None
                        self.head = None
                    else:
                        previous.next = self.current.next
                        self.current = None
                    return 'Node with the value: %s was removed from the LinkedList' % value
                else:
                    previous = self.current
                    self.current = self.current.next
        return 'Node is not in LinkedList'

    # 3. size
    def size(self):
        length = 1
        if self.head is None:
            return length
        else:
            length = 1
            self.current = self.head
            while self.current.next != None:
                self.current = self.current.next
                length = length + 1
            return length

    # 4. conversion from and to python lists
    def linkedlist_to_list(self):
        list = []
        cur = self.head
        if cur is not None and cur.data != 'head':
            list.append([None, 'head'])
        while cur is not None:
            list.append([cur.key, cur.data])

            cur = cur.next
        return list

    def linkedlist_from_list(self, lst):
        if len(lst) == 0:
            self.head = None
            return
        root = Node('head', None)
        cur = root
        for d in lst:
            node = Node(d[1], None)
            node.key = d[0]
            cur.next = node
            cur = cur.next
        self.head = root

    # 7. map structure by speciﬁc function
    def hash_map(self, f):
        self.current = self.head
        while self.current is not None:
            self.current.data = f(self.current.data)
            self.current = self.current.next

    # 8. reduce – process structure elements to build a return value by speciﬁc functions
    def hash_reduce(self, f, initial_state):
        state = initial_state
        cur = self.head
        while cur is not None:
            if cur.data is 'head':
                cur = cur.next
            else:
                state = f(state, cur.data)
                cur = cur.next

        return state

    # 10. iterator
    def __iter__(self):
        return LinkedList(self.head)

    def __next__(self):
        if self.head is None:
            raise StopIteration
        tmp = self.head.data
        self.head = self.head.next
        return tmp

    def __len__(self):
        return self.size()

    def __str__(self):
        return '<LinkedList: %s nodes>' % self.size()

    def __repr__(self):
        nodes = []
        node = self.head
        while not node is None:
            nodes.append(repr(node))
            node = node.next
        return 'LinkedList: Nodes: %r' % nodes


# A Hashmap that uses LinkedLists to handle collisions (chaining)
class Hashmap(object):
    def __init__(self, length=5):
        listBuckets = []
        for i in range(length):
            head = Node(None, None)
            head.key = i
            listBuckets.append(LinkedList(head))
        self.buckets = listBuckets
        # 3. size
        self.length = length

    def hashFunction(self, data):
        key = data % self.length
        return key

    # 1. add a new element
    def insert(self, node):
        key = self.hashFunction(node.data)
        node.key = key
        pushOutput = self.buckets[key].add_to_tail(node)
        return pushOutput

    # 2. remove an element
    def remove(self, data):
        key = self.hashFunction(data)
        removedOutput = self.buckets[key].remove(data)
        return removedOutput

    # 4. conversion from and to python lists
    def hashmap_to_list(self):
        list = []
        for i in range(self.length):
            linked = self.buckets[i]
            res = linked.linkedlist_to_list()
            del res[0]
            list.append(res)
        return list

    def hashmap_from_list(self, list):

        for lst in list:
            linked = LinkedList()
            linked.linkedlist_from_list(lst)
            key = lst[0][0]
            self.buckets[key] = linked

    # 5. ﬁnd element by speciﬁc predicate
    def data_find_node(self, data):
        key = data % self.length
        linked = self.buckets[key]
        cur = linked.head
        ans = None
        while cur is not None:
            if cur.data == data:
                ans = cur
                cur = cur.next
            else:
                cur = cur.next
        return ans

    # 6. ﬁlter data structure by speciﬁc predicate
    def filter_key(self, key):
        return self.buckets[key]

    # 9. mempty and mconcat
    def mempty(self):
        ReBuckets  = []
        for i in range(self.length):
            head = Node(None, None)
            head.key = i
            ReBuckets.append(LinkedList(head))
        self.buckets = ReBuckets

        return self.buckets

    def mconcat(self, node1,node2):
        if node1 is not None:
            key1 = node1.data % self.length
            node1.key = key1
            self.buckets[key1].add_to_tail(node1)
        if node2 is not None:
            key2 = node2.data % self.length
            node2.key = key2
            self.buckets[key2].add_to_tail(node2)

        return self.buckets

    def __repr__(self):
        return '<Hashmap %s>' % self.buckets
