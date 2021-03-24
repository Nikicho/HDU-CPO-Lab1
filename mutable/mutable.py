#Author: Zhou Xinyu
class Node(object):
    def __init__(self, value=None, next=None):
        self.flag = None
        self.value = value
        self.next = next

    def __repr__(self):
        if self.flag != None:
            return "Node flag: %s value: %s" % (self.flag, self.value)
        else:
            return "Node flag: %s value: %s" % (self.flag, self.value)


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.cur = None

    # 1. add
    def add_to_tail(self, node):
        self.cur = self.head
        if self.head is None:
            self.head = node
            return self.head
        else:
            while self.cur.next != None:
                self.cur = self.cur.next
            self.cur.next = node
        return self.cur

    def add_to_head(self, node):
        self.cur = self.head
        if self.head is None:
            self.head = node
            return self.head
        else:
            self.head = node
            self.head.next = self.cur
        return self.head

    def _last_node(self):
        assert self.head is not None
        self.cur = self.head
        while self.cur is not None:
            self.cur = self.cur.next
        return self.cur

    # 2. remove
    def remove(self, value):
        pre = None
        self.cur = self.head
        if self.cur is None:
            return 'Linked List is empty, value of: %s is not here' % value
        else:
            while self.cur != None:
                if self.cur.value == value:
                    if len(self) is 1:
                        pre = None
                        self.cur = None
                        self.head = None
                    else:
                        pre.next = self.cur.next
                        self.cur = None
                    return 'Node with the value: %s was removed from the LinkedList' % value
                else:
                    pre = self.cur
                    self.cur = self.cur.next
        return 'Node is not in LinkedList'

    # 3. size
    def size(self):
        length = 1
        if self.head is None:
            return length
        else:
            length = 1
            self.cur = self.head
            while self.cur.next != None:
                self.cur = self.cur.next
                length = length + 1
            return length

    # 4. conversion
    def linkedlist_to_list(self):
        list = []
        cur = self.head
        if cur is not None and cur.value != 'head':
            list.append([None, 'head'])
        while cur is not None:
            list.append([cur.flag, cur.value])

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
            node.flag = d[0]
            cur.next = node
            cur = cur.next
        self.head = root

    # 7. map
    def hash_map(self, f):
        self.cur = self.head
        while self.cur is not None:
            self.cur.value = f(self.cur.value)
            self.cur = self.cur.next

    # 8. reduce
    def hash_reduce(self, f, initState):
        state = initState
        cur = self.head
        while cur is not None:
            if cur.value is 'head':
                cur = cur.next
            else:
                state = f(state, cur.value)
                cur = cur.next

        return state

    # 10. iterator
    def __iter__(self):
        return LinkedList(self.head)

    def __next__(self):
        if self.head is None:
            raise StopIteration
        tmp = self.head.value
        self.head = self.head.next
        return tmp

    def __len__(self):
        return self.size()

    def __str__(self):
        return 'LinkedList: %s nodes' % self.size()

    def __repr__(self):
        nodes = []
        node = self.head
        while not node is None:
            nodes.append(repr(node))
            node = node.next
        return 'LinkedList: Nodes: %r' % nodes

    
class Hashmap(object):
    def __init__(self, length=5):
        listBuckets = []
        for i in range(length):
            head = Node(None, None)
            head.flag = i
            listBuckets.append(LinkedList(head))
        self.buckets = listBuckets
        # 3. size
        self.length = length

    def hashFunction(self, value):
        flag = value % self.length
        return flag

    # 1. add
    def addEle(self, node):
        flag = self.hashFunction(node.value)
        node.flag = flag
        pushOutput = self.buckets[flag].add_to_tail(node)
        return pushOutput

    # 2. remove
    def remove(self, value):
        flag = self.hashFunction(value)
        removedOutput = self.buckets[flag].remove(value)
        return removedOutput

    # 4. conversion
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
            flag = lst[0][0]
            self.buckets[flag] = linked

    # 5. ﬁnd
    def value_find_node(self, value):
        flag = value % self.length
        linked = self.buckets[flag]
        cur = linked.head
        ans = None
        while cur is not None:
            if cur.value == value:
                ans = cur
                cur = cur.next
            else:
                cur = cur.next
        return ans

    # 6. ﬁlter
    def filter_flag(self, flag):
        return self.buckets[flag]

    # 9. mempty and mconcat
    def mempty(self):
        ReBuckets  = []
        for i in range(self.length):
            head = Node(None, None)
            head.flag = i
            ReBuckets.append(LinkedList(head))
        self.buckets = ReBuckets

        return self.buckets

    def mconcat(self, node1,node2):
        if node1 is not None:
            flag1 = node1.value % self.length
            node1.flag = flag1
            self.buckets[flag1].add_to_tail(node1)
        if node2 is not None:
            flag2 = node2.value % self.length
            node2.flag = flag2
            self.buckets[flag2].add_to_tail(node2)

        return self.buckets

    def __repr__(self):
        return 'Hashmap %s' % self.buckets
