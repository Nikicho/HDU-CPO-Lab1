import unittest
from hypothesis import given
import hypothesis.strategies as st
from immutable_node import *


class TestImmutableList(unittest.TestCase):
    def test_hash_Function(self):
        node1 = Node(10, None)
        node2 = Node(15, None)
        self.assertEqual(hash_Function(node1, 5), hash_Function(node2, 5))

    def test_insert_hash(self):
        buckets = [
            Node(0, None),
            Node(1, None),
            Node(2, None),
            Node(3, None),
            Node(4, None),
        ]
        node1 = Node(10, None)
        node2 = Node(15, None)
        self.assertEqual(insert_hash(node1, buckets), insert_hash(node2, buckets))

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
        buckets[0].next = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4
        hash_Function(node1, len(buckets))
        hash_Function(node2, len(buckets))
        hash_Function(node3, len(buckets))
        hash_Function(node4, len(buckets))
        self.assertEqual(remove_hash(node1, buckets), 1)

    def test_size(self):
        self.assertEqual(list_size(None), 0)
        self.assertEqual(list_size(cons('a', None)), 1)
        self.assertEqual(list_size(cons('a', cons('b', None))), 2)

    def test_cons(self):
        self.assertEqual(cons('a', None), Node('a', None))
        self.assertEqual(cons('a', cons('b', None)), Node('a', Node('b', None)))

    def test_append_node(self):
        n1=Node(1,Node(2,None))
        self.assertEqual(n1, append_node(Node(1, None), Node(2, None)))

    def test_remove(self):
        self.assertRaises(AssertionError, lambda: remove(None, 'a'))
        self.assertRaises(AssertionError, lambda: remove(cons('a', None), 'b'))
        self.assertEqual(remove(cons('a', cons('a', None)), 'a'), cons('a', None))
        self.assertEqual(remove(cons('a', cons('b', None)), 'a'), cons('b', None))
        self.assertEqual(remove(cons('a', cons('b', None)), 'b'), cons('a', None))

    def test_head(self):
        self.assertRaises(AssertionError, lambda: head(None))
        self.assertEqual(head(cons('a', None)), 'a')

    def test_tail(self):
        self.assertRaises(AssertionError, lambda: tail(None))
        self.assertEqual(tail(cons('a', None)), None)
        self.assertEqual(tail(cons('a', cons('b', None))), cons('b', None))


    def test_reverse(self):
        self.assertEqual(reverse(None), None)
        self.assertEqual(reverse(cons('a', None)), cons('a', None))
        self.assertEqual(reverse(cons('a', cons('b', None))), cons('b', cons('a', None)))


    def test_mconcat(self):
        self.assertEqual(mconcat(None, None), None)
        self.assertEqual(mconcat(cons('a', None), None), cons('a', None))
        self.assertEqual(mconcat(None, cons('a', None)), cons('a', None))
        self.assertEqual(mconcat(cons('a', None), cons('b', None)), cons('a', cons('b', None)))

    def test_to_list(self):
        self.assertEqual(to_list(None), [])
        self.assertEqual(to_list(cons('a', None)), ['a'])
        self.assertEqual(to_list(cons('a', cons('b', None))), ['a', 'b'])

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

    def test_from_hashmap(self):
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
            cur1.key=0
            cur1=cur1.next
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
        buckets1 = from_hashmap(buckets1, test_data)
        self.assertEqual(buckets1, buckets2)

    def test_hashmap_to_list(self):
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
        self.assertEqual(hasmap_to_list(from_hashmap(buckets1,test_data)), test_data)

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
            get_next = iterator(lst)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(x, tmp)
        self.assertEqual(to_list(lst), tmp)
        get_next = iterator(None)
        self.assertRaises(StopIteration, lambda: get_next())



if __name__ == '__main__':
    unittest.main()
