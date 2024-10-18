import pytest

from neet150 import Solution

@pytest.fixture
def solution_object():
    return Solution()

def test_hasDuplicate(solution_object):
    assert solution_object.hasDuplicate([1,2,3,4]) == False
    assert solution_object.hasDuplicate([1,2,3,3]) == True