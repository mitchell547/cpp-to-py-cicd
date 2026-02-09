from mymodule.main import my_sum, my_sum_py
import pytest
import timeit

def test_empty_arr():
    res = my_sum([])
    assert res == 0, "Sum of empty array should be 0"
    
def test_all_zeros():
    res = my_sum([0,0,0,0,0,0,0,0])
    assert res == 0, "Sum of all zero elements should be 0"
    
def test_single_elem():
    res = my_sum([5])
    assert res == 5, "Wrong answer"
    
def test_ten_elems():
    res = my_sum([1,2,3,4,5,6,7,8,9,10])
    assert res == 55, "Wrong answer"
    
def test_thousand_elems():
    arr = [1] * 1000
    res = my_sum(arr)
    assert res == 1000, "Wrong answer"
    
def test_negative_elems():
    res = my_sum([-1, -2, -3])
    assert res == -6, "Wrong answer"

def test_opposite_elems():
    res = my_sum([-9999, 9999])
    assert res == 0, "Wrong answer"
    
def test_wrong_datatype():
    with pytest.raises(TypeError):
        res = my_sum(['a'])
    
def test_performance():
    arr_len = 1000
    print("cpp func:", timeit.timeit('my_sum(arr)', setup=f'arr = [1] * {arr_len};', globals=globals(), number=1000))
    print("py func:", timeit.timeit('my_sum_py(arr)', setup=f'arr = [1] * {arr_len};', globals=globals(), number=1000))