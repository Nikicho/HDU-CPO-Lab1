"""
@author: Shi Wenhao
"""
import unittest
from hypothesis import given
import hypothesis.strategies as st
from immutable_node import *


class TestImmutableList(unittest.TestCase):
    def test_hash_Function(self):
        node1 = Node(10, None)
        node2 = Node(15, None)
        self.assertEqual(hash_Function(node1, 5), hash_Function(node2, 5))

    def test_add_hash(self):
        buckets = [
            Node(0, None),
            Node(1, None),
            Node(2, None),
            Node(3, None),
            Node(4, None),
        ]
        node1 = Node(10, None)
        node2 = Node(15, None)
        self.assertEqual(add_hash(node1, buckets), add_hash(node2, buckets))

    def test_remove_hash(self):
        buckets = [
            Node(0, None),
            Node(1, None),
            Node(2, None),
            Node(3, None),
            Node(4, None),
        ]
        node1 = Node(20, None)
        node2 = Node(5, None)
        node3 = Node(10, None)
        node4 = Node(15, None)
        buckets[0].nxt = node1
        node1.nxt = node2
        node2.nxt = node3
        node3.nxt = node4
        hash_Function(node1, len(buckets))
        hash_Function(node2, len(buckets))
        hash_Function(node3, len(buckets))
        hash_Function(node4, len(buckets))
        self.assertEqual(remove_hash(node1, buckets), 1)

    def test_size(self):
        self.assertEqual(list_size(None), 0)
        self.assertEqual(list_size(list_add('a', None)), 1)
        self.assertEqual(list_size(list_add('a', list_add('b', None))), 2)

    def test_list_add(self):
        self.assertEqual(list_add('a', None), Node('a', None))
        self.assertEqual(list_add('a', list_add('b', None)), Node('a', Node('b', None)))

    def test_append_node(self):
        n1=Node(1,Node(2,None))
        self.assertEqual(n1, append_node(Node(1, None), Node(2, None)))

    def test_remove(self):
        self.assertRaises(AssertionError, lambda: remove(None, 'a'))
        self.assertRaises(AssertionError, lambda: remove(list_add('a', None), 'b'))
        self.assertEqual(remove(list_add('a', list_add('a', None)), 'a'), list_add('a', None))
        self.assertEqual(remove(list_add('a', list_add('b', None)), 'a'), list_add('b', None))
        self.assertEqual(remove(list_add('a', list_add('b', None)), 'b'), list_add('a', None))

    def test_head(self):
        self.assertRaises(AssertionError, lambda: head(None))
        self.assertEqual(head(list_add('a', None)), 'a')

    def test_nextNode(self):
        self.assertRaises(AssertionError, lambda: nextNode(None))
        self.assertEqual(nextNode(list_add('a', None)), None)
        self.assertEqual(nextNode(list_add('a', list_add('b', None))), list_add('b', None))


    def test_reverse(self):
        self.assertEqual(reverse(None), None)
        self.assertEqual(reverse(list_add('a', None)), list_add('a', None))
        self.assertEqual(reverse(list_add('a', list_add('b', None))), list_add('b', list_add('a', None)))


    def test_mconcat(self):
        self.assertEqual(mconcat(None, None), None)
        self.assertEqual(mconcat(list_add('a', None), None), list_add('a', None))
        self.assertEqual(mconcat(None, list_add('a', None)), list_add('a', None))
        self.assertEqual(mconcat(list_add('a', None), list_add('b', None)), list_add('a', list_add('b', None)))

    def test_to_list(self):
        self.assertEqual(to_list(None), [])
        self.assertEqual(to_list(list_add('a', None)), ['a'])
        self.assertEqual(to_list(list_add('a', list_add('b', None))), ['a', 'b'])

    def test_from_list(self):
        test_data = [[3, 6, 9],
                     [4, 7, 10],
                     [5, 8, 11]]
        n0 = Node(3, Node(6, Node(9, None)))
        n1 = Node(4, Node(7, Node(10, None)))
        n2 = Node(5, Node(8, Node(11, None)))
        self.assertEqual(n0,from_list(test_data[0]))
        self.assertEqual(n1,from_list(test_data[1]))
        self.assertEqual(n2,from_list(test_data[2]))

    def test_to_hashmap(self):
        test_data= [[3, 6, 9],
                    [4, 7, 10],
                    [5, 8, 11]]
        buckets1 = [
            Node(0, None),
            Node(1, None),
            Node(2, None),
        ]
        n1 = Node(3, Node(6, Node(9, None)))
        cur1 = n1
        while cur1 is not None:
            cur1.flag=0
            cur1=cur1.nxt
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
        buckets1 = to_hashmap(buckets1, test_data)
        self.assertEqual(buckets1, buckets2)

    def test_hashmap_to_list(self):
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
        test_data = [[3, 6, 9],
                     [4, 7, 10],
                     [5, 8, 11]]
        self.assertEqual(hasmap_to_list(buckets2),test_data)

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self,a):
        lst = from_list(a)
        b = to_list(lst)
        self.assertEqual(a, b)

    def test_from_hashmap_to_list_equality(self):
        test_data = [[3, 6, 9],
                     [4, 7, 10],
                     [5, 8, 11]]
        buckets1 = [
            Node(0, None),
            Node(1, None),
            Node(2, None),
        ]
        self.assertEqual(hasmap_to_list(to_hashmap(buckets1,test_data)), test_data)

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst):
        a = from_list(lst)
        b=[1, 2, 3]
        list=from_list(b)
        n1=Node(1,None)
        n2=Node(2,None)
        n3=Node(3,None)
        self.assertEqual(mconcat(empty(), a), a)
        self.assertEqual(mconcat(a, empty()), a)
        self.assertEqual(mconcat(mconcat(n1, n2), n3), list)
        self.assertEqual(mconcat(n1, mconcat(n2, n3)), list)

    def test_iter(self):
        x = [1, 2, 3]
        lst = from_list(x)
        tmp = []
        try:
            get_nxt = iterator(lst)
            while True:
                tmp.append(get_nxt())
        except StopIteration:
            pass
        self.assertEqual(x, tmp)
        self.assertEqual(to_list(lst), tmp)
        get_nxt = iterator(None)
        self.assertRaises(StopIteration, lambda: get_nxt())



if __name__ == '__main__':
    unittest.main()
