#Author: Zhou Xinyu
import unittest
from hypothesis import given
import hypothesis.strategies as st
from mutable import *
import pytest

class TestHashmapMethods(unittest.TestCase):

    def test_init(self):
        hashmap = HashMap()
        self.assertEqual(hashmap.length, 5)

    def test_hashFunction(self):
        hashmap = HashMap()
        hash_value = hashmap.hashFunction(77)
        self.assertEqual(hash_value, 2)
    #1.
    def test_add(self):
        hashmap = HashMap()
        self.assertEqual(hashmap.hashmap_to_list(), [])
        hashmap.add(46, 244)
        self.assertEqual(hashmap.get(46), 244)
    #2.      
    def test_remove(self):
        hashmap = HashMap()
        hashmap.add(1,2)
        self.assertEqual(hashmap.get(1), 2)
        
        hashmap.remove(2)
        self.assertEqual(hashmap.hashmap_to_dict(), {})
        with pytest.raises(Exception):
            hashmap.remove(6)
        
    def test_get(self):
        hashmap = HashMap()
        hashmap.add(1, 2)
        self.assertEqual(hashmap.get(1), 2)
    #3.
    def test_get_size(self):
        hashmap = HashMap()
        self.assertEqual(hashmap.get_size(), 0)
        dict = {1: 1, 2: 2, 3: 3}
        hashmap.hashmap_from_dict(dict)
        self.assertEqual(hashmap.get_size(), 3)
        hashmap.add(2, 10)
        self.assertEqual(hashmap.get_size(), 3)
    #4. conversion  
    def test_hashmap_from_dict(self):
        hashmap = HashMap()
        dict = {1: 1, 2: 2, 3: 3}
        hashmap.hashmap_from_dict(dict)
        self.assertEqual(hashmap.get_size(), 3)
        dict1 = {5:10, 22:4}
        hashmap.hashmap_from_dict(dict1)
        self.assertEqual(hashmap.get_size(), 5)
    #4. conversion 
    def test_hashmap_from_list(self):
        hashmap = HashMap()
        test_data = [1, 2, 3, 4]
        hashmap.hashmap_from_list(test_data)
        self.assertEqual(hashmap.get_size(), 4)
    #4. conversion    
    def test_hashmap_to_dict(self):
        hashmap = HashMap()
        hashmap.add(1, 2)
        hashmap.add(2, 3)
        self.assertEqual(hashmap.hashmap_to_dict(), {1: 2, 2: 3})
    #4. conversion    
    def test_hashmap_to_list(self):
        hashmap = HashMap()
        dict = {1: 2, 2: 3, 3: 4}
        hashmap.hashmap_from_dict(dict)
        self.assertEqual(hashmap.hashmap_to_list(), [2, 3, 4])
    # 5. ﬁnd: return the even value list
    def test_find_even(self):
        hashmap = HashMap()
        hashmap.hashmap_from_list([45.21, 2, 70.0, 7.0])
        self.assertEqual(hashmap.find_even(), [2, 70.0])
    # 6. ﬁlter: return the values' list except even value
    def test_filter_even(self):
        hashmap = HashMap()
        hashmap.hashmap_from_list([45.21, 2 ,4, 7.0])
        self.assertEqual(hashmap.filter_even(), [45.21, 7.0])
    # 7.map(func): test square
    def test_map(self):
        dict1 = {1: 3, 4: 10}
        hashmap = HashMap()
        hashmap.hashmap_from_dict(dict1)
        self.assertEqual(hashmap.map(lambda x: x*x), [9,100])
    # 8.reduce:test multiplicative
    def test_reduce(self):
        hashmap = HashMap()
        self.assertEqual(hashmap.reduce(lambda a,b: a*b), 1)
        dict1 = {2: 18, 4: 18}
        hashmap.hashmap_from_dict(dict1)
        self.assertEqual(hashmap.reduce(lambda a,b: a*b), 324)
    #10.iteration
    def test_iter(self):
        x = {1, 2, 3, 4}
        hashmap = HashMap()
        hashmap.hashmap_from_list(x)
        tmp = {}
        for e in hashmap:
            tmp[e.key] = e.value
        self.assertEqual(hashmap.hashmap_to_dict(), tmp)
        i = iter(hashmap)
        self.assertEqual(next(i).value, 1)
    #Add property-based tests for from_list and to_list, all monoid properties (Associativity, Identity element) 
    @given(a=st.lists(st.integers()), b=st.lists(st.integers()), c=st.lists(st.integers()))
    def test_monoid_associativity(self, a, b, c):
        hashmap = HashMap()
        hash_a = HashMap()
        hash_b = HashMap()
        hash_c = HashMap()
        
        hash_a.hashmap_from_list(a)
        hash_b.hashmap_from_list(b)
        hash_c.hashmap_from_list(c)
        
        ab = hashmap.mconcat(hash_a, hash_b)
        abc1 = hashmap.mconcat(ab, hash_c)
        bc = hashmap.mconcat(hash_b, hash_c)
        abc2 = hashmap.mconcat(hash_a, bc)
        
        self.assertEqual(abc1, abc2)
        
    @given(st.lists(st.integers()))
    def test_monoid_identity(self, a):
        hash1 = HashMap()
        hash2 = HashMap()
        hash1.hashmap_from_list(a)
        # a+b = b+a
        self.assertEqual(hash1.mconcat(hash2.mempty(), hash1), hash1)
        self.assertEqual(hash1.mconcat(hash1, hash2.mempty()), hash1)
        
    @given(a =st.lists(st.integers()))
    def test_hashmap_from_list_to_list_equality(self, a):
        hashmap = HashMap()
        hashmap.hashmap_from_list(a)
        b = hashmap.hashmap_to_list()
        self.assertEqual(len(b), len(a))

if __name__ == '__main__':
    unittest.main()
