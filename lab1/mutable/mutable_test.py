import unittest
from hypothesis import given
import hypothesis.strategies as st
from mutable import *


class TestCaseNode(unittest.TestCase):

    def setUp(self):
        self.node = Node(7, None)

    def tearDown(self):
        self.node = None
        del self.node


class TestNodeMethods(TestCaseNode):
    def test_init(self):
        self.assertEqual(self.node.data, 7)
        self.assertEqual(self.node.key, None)
        self.assertEqual(self.node.next, None)

    def test_repr(self):
        reprString = repr(self.node)
        self.assertEqual(reprString, "<Node key: None data: 7>")
        self.node.key = 45
        reprString = repr(self.node)
        self.assertEqual(reprString, "<Node key: 45 data: 7>")


class TestCaseMuLinkedList(unittest.TestCase):
    def setUp(self):
        self.linkedlist = LinkedList()

    def tearDown(self):
        del self.linkedlist


class TestLinkedListMethods(TestCaseMuLinkedList):
    def test_init(self):
        self.assertEqual(self.linkedlist.head, None)

    def test_size(self):
        self.assertEqual(len(self.linkedlist), 1)

        for i in range(20):
            node = Node(i, None)
            self.linkedlist.add_to_tail(node)
        self.assertEqual(len(self.linkedlist), 20)

    def test_add_to_tail(self):
        node = Node(3, None)
        output = self.linkedlist.add_to_tail(node)
        self.assertEqual(repr(output), "<Node key: None data: 3>")
        for i in range(7):
            node = Node(i, None)
            output = self.linkedlist.add_to_tail(node)
        self.assertEqual(repr(output), "<Node key: None data: 5>")

    def test_add_to_head(self):
        node = Node(3, None)
        output = self.linkedlist.add_to_head(node)
        self.assertEqual(repr(output), "<Node key: None data: 3>")
        for i in range(7):
            node = Node(i, None)
            output = self.linkedlist.add_to_head(node)
        self.assertEqual(repr(output), "<Node key: None data: 6>")

    def test_remove(self):
        node = Node(10, None)
        outputEmpty = self.linkedlist.remove(node.data)
        self.assertEqual(outputEmpty, "Linked List is empty, value of: 10 is not here")
        for i in range(10):
            node = Node(i, None)
            self.linkedlist.add_to_head(node)
        outputNotHere = self.linkedlist.remove(11)
        self.assertEqual(outputNotHere, 'Node is not in LinkedList')
        outputRemove = self.linkedlist.remove(5)
        self.assertEqual(outputRemove, 'Node with the value: 5 was removed from the LinkedList')

    def test_str(self):
        output = str(self.linkedlist)
        self.assertEqual(output, '<LinkedList: 1 nodes>')

    def test_repr(self):
        output = repr(self.linkedlist)
        self.assertEqual(output, 'LinkedList: Nodes: []')

    def test_linkedlist_to_list(self):
        self.assertEqual(LinkedList().linkedlist_to_list(), [])
        self.assertEqual(LinkedList(Node('a', None)).linkedlist_to_list(), [[None, 'head'], [None, 'a']])
        self.assertEqual(LinkedList(Node('a', Node('b', None))).linkedlist_to_list(), [[None, 'head'], [None, 'a'], [None, 'b']])

    def test_linkedlist_from_list(self):
        test_data = [
            [],
            [[None, 'a']],
            [[None, 'a'], [None, 'b']]
        ]
        lst = LinkedList()
        lst.linkedlist_from_list(test_data[0])
        self.assertEqual(lst.linkedlist_to_list(), [])
        lst1 = LinkedList()
        lst1.linkedlist_from_list(test_data[1])
        self.assertEqual(lst1.linkedlist_to_list(), [[None, 'head'], [None, 'a']])
        lst2 = LinkedList()
        lst2.linkedlist_from_list(test_data[2])
        self.assertEqual(lst2.linkedlist_to_list(), [[None, 'head'], [None, 'a'], [None, 'b']])

    def test_map(self):
        lst = LinkedList()
        lst.hash_map(str)
        self.assertEqual(lst.linkedlist_to_list(), [])
        lst = LinkedList()
        lst.linkedlist_from_list([[1, 1], [2, 2], [3, 3]])
        lst.hash_map(str)
        self.assertEqual(lst.linkedlist_to_list(), [[None, 'head'], [1, '1'], [2, '2'], [3, '3']])

    def test_reduce(self):
        lst = LinkedList()
        self.assertEqual(lst.hash_reduce(lambda st, e: st + e, 0), 0)
        lst = LinkedList()
        lst.linkedlist_from_list([[1, 1], [2, 2], [3, 3]])
        self.assertEqual(lst.hash_reduce(lambda st, e: st + e, 0), 6)

    @given(k=st.integers(), v=st.integers())
    def linkedlist_to_list(self, k, v):
        list = [[k, v]]
        lst = LinkedList()
        lst.linkedlist_from_list(list)
        b = lst.linkedlist_to_list()
        list = [[None, 'head'], [k, v]]
        self.assertEqual(list, b)

    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        lst = LinkedList()
        list = []
        for i in a:
            list.append([None, i])
        lst.linkedlist_from_list(list)
        self.assertEqual(lst.size() - 1, len(list))

    def test_iter(self):
        x = [[1, 1], [2, 2], [3, 3]]
        lst = LinkedList()
        lst.linkedlist_from_list(x)
        tmp = []
        cur = lst.head

        while cur is not None:
            tmp.append([cur.key, cur.data])

            cur = cur.next

        self.assertEqual(lst.linkedlist_to_list(), tmp)


class TestCaseHashMap(unittest.TestCase):
    def setUp(self):
        self.hashmap = Hashmap()

    def tearDown(self):
        del self.hashmap


class TestHashmapMethods(TestCaseHashMap):

    def test_init(self):
        self.assertEqual(self.hashmap.length, 5)
        del self.hashmap
        self.hashmap = Hashmap(5)
        self.assertEqual(self.hashmap.length, 5)
        self.assertEqual(self.hashmap.buckets[3].head.key, 3)

    def test_hashFunction(self):
        key = self.hashmap.hashFunction(1079)
        self.assertEqual(key, 4)

    def test_insert(self):
        node = Node(576, None)
        insertOutput = self.hashmap.insert(node)
        self.assertEqual(repr(insertOutput.next), '<Node key: 1 data: 576>')

    def test_remove(self):
        removeEmpty = self.hashmap.remove(5)
        self.assertEqual(removeEmpty, "Node is not in LinkedList")
        for i in range(5):
            node = Node(i, None)
            self.hashmap.insert(node)
        outputNotHere = self.hashmap.remove(505)
        self.assertEqual(outputNotHere, 'Node is not in LinkedList')
        outputRemove = self.hashmap.remove(4)
        self.assertEqual(outputRemove, 'Node with the value: 4 was removed from the LinkedList')
        node = Node(205, None)
        self.hashmap.insert(node)
        node = Node(305, None)
        self.hashmap.insert(node)
        outputRemove = self.hashmap.remove(305)
        self.assertEqual(outputRemove, 'Node with the value: 305 was removed from the LinkedList')

    def test_hashmap_to_list(self):
        self.assertEqual(Hashmap().hashmap_to_list(), [[[0, None]], [[1, None]], [[2, None]], [[3, None]], [[4, None]]])

    def test_hashmap_from_list(self):
        test_data = [[[0, 5], [0, 10]],
                     [[1, 6], [1, 11]],
                     [[2, 7], [2, 12]],
                     [[3, 8], [3, 13]],
                     [[4, 9], [4, 14]]]

        hashmap = Hashmap()
        hashmap.hashmap_from_list(test_data)
        self.assertEqual(repr(hashmap),
                         "<Hashmap [LinkedList: Nodes: ['<Node key: None data: head>', '<Node key: 0 data: 5>', '<Node key: 0 data: 10>'],"
                         " LinkedList: Nodes: ['<Node key: None data: head>', '<Node key: 1 data: 6>', '<Node key: 1 data: 11>'], "
                         "LinkedList: Nodes: ['<Node key: None data: head>', '<Node key: 2 data: 7>', '<Node key: 2 data: 12>'], "
                         "LinkedList: Nodes: ['<Node key: None data: head>', '<Node key: 3 data: 8>', '<Node key: 3 data: 13>'], "
                         "LinkedList: Nodes: ['<Node key: None data: head>', '<Node key: 4 data: 9>', '<Node key: 4 data: 14>']]>")

    def test_hashmap_from_list_to_list_equality(self):
        test_data = [[[0, 5], [0, 10]],
                     [[1, 6], [1, 11]],
                     [[2, 7], [2, 12]],
                     [[3, 8], [3, 13]],
                     [[4, 9], [4, 14]]]

        hashmap = Hashmap()
        hashmap.hashmap_from_list(test_data)
        self.assertEqual(hashmap.hashmap_to_list(), test_data)

    def test_data_find_node(self):
        test_data = [[[0, 5], [0, 10]],
                     [[1, 6], [1, 11]],
                     [[2, 7], [2, 12]],
                     [[3, 8], [3, 13]],
                     [[4, 9], [4, 14]]]

        hashmap = Hashmap()
        hashmap.hashmap_from_list(test_data)
        node = hashmap.data_find_node(10)
        self.assertEqual(repr(node), '<Node key: 0 data: 10>')

    def test_filter_key(self):
        test_data = [[[0, 5], [0, 10]],
                     [[1, 6], [1, 11]],
                     [[2, 7], [2, 12]],
                     [[3, 8], [3, 13]],
                     [[4, 9], [4, 14]]]

        hashmap = Hashmap()
        hashmap.hashmap_from_list(test_data)
        linked = hashmap.filter_key(0)
        self.assertEqual(repr(linked),
                         "LinkedList: Nodes: ['<Node key: None data: head>', '<Node key: 0 data: 5>', '<Node key: 0 data: 10>']")

    def test_mempty(self):
        self.assertEqual(repr(Hashmap().mempty()),
                         "[LinkedList: Nodes: ['<Node key: 0 data: None>'], "
                        "LinkedList: Nodes: ['<Node key: 1 data: None>'], "
                        "LinkedList: Nodes: ['<Node key: 2 data: None>'], "
                        "LinkedList: Nodes: ['<Node key: 3 data: None>'], "
                        "LinkedList: Nodes: ['<Node key: 4 data: None>']]")

    def test_mconcat(self):
        node1 = Node(5, None)
        node2 = Node(10,None)
        self.assertEqual(repr(Hashmap().mconcat(node1,node2)),
                         "[LinkedList: Nodes: ['<Node key: 0 data: None>', '<Node key: 0 data: 5>', '<Node key: 0 data: 10>'], "
                         "LinkedList: Nodes: ['<Node key: 1 data: None>'], "
                         "LinkedList: Nodes: ['<Node key: 2 data: None>'], "
                         "LinkedList: Nodes: ['<Node key: 3 data: None>'], "
                         "LinkedList: Nodes: ['<Node key: 4 data: None>']]")

    @given(l1=st.integers(), l2=st.integers(),l3=st.integers())
    def test_monoid_identity(self, l1,l2,l3):
        hashmap = Hashmap()
        hashmap2 = Hashmap()

        hashmap2.insert(Node(l1,None))
        self.assertEqual(repr(hashmap.mconcat(Node(l1,None),None)), repr(hashmap2.buckets))
        hashmap.remove(l1)
        self.assertEqual(repr(hashmap.mconcat(None,Node(l1,None))), repr(hashmap2.buckets))
        hashmap.remove(l1)

        hashmap2.insert(Node(l2,None))
        hashmap2.insert(Node(l3, None))
        hashmap.mconcat(Node(l1,None),Node(l2,None))
        hashmap.mconcat(Node(l3, None),None)
        self.assertEqual(repr(hashmap.buckets), repr(hashmap2.buckets))

        hashmap3 = Hashmap()
        hashmap3.mconcat(Node(l1,None),None)
        hashmap3.mconcat(Node(l2,None),Node(l3,None))

        self.assertEqual(repr(hashmap3.buckets), repr(hashmap2.buckets))

if __name__ == '__main__':
    unittest.main()
