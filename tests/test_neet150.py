import pytest

from neet150 import Solution

@pytest.fixture
def solution_object():
    return Solution()

def test_hasDuplicate(solution_object):
    assert solution_object.hasDuplicate([1,2,3,4]) == False
    assert solution_object.hasDuplicate([1,2,3,3]) == True

def test_isAnagram(solution_object):
    assert solution_object.isAnagram("racecar", "carrace") == True
    assert solution_object.isAnagram("jar", "jam") == False

def test_twoSum(solution_object):
    assert solution_object.twoSum([3,4,5,6], 7) == [0,1]
    assert solution_object.twoSum([4,5,6], 10) == [0,2]

def test_groupAnagrams(solution_object):
    assert solution_object.groupAnagrams(sorted(["act","pots","tops","cat","stop","hat"])) == sorted([["hat"],["act", "cat"],sorted(["stop", "pots", "tops"])])
    assert solution_object.groupAnagrams(["x"]) == [["x"]]
    assert solution_object.groupAnagrams([""]) == [[""]]
