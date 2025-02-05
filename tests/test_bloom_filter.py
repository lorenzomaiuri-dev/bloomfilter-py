import pytest
from bloomfilter_lite import BloomFilter

@pytest.fixture
def bloom_filter():
    return BloomFilter(expected_items=1000, false_positive_rate=0.01)

def test_add_and_check(bloom_filter):
    bloom_filter.add("test")
    assert bloom_filter.check("test") is True

def test_false_negative(bloom_filter):
    assert bloom_filter.check("nonexistent") is False

def test_false_positive_rate():
    bf = BloomFilter(expected_items=10000, false_positive_rate=0.01)
    test_elements = [f"item{i}" for i in range(10000)]
    for item in test_elements:
        bf.add(item)
    
    false_positives = sum(1 for i in range(10000, 11000) if bf.check(f"item{i}"))
    actual_fp_rate = false_positives / 1000.0
    
    assert actual_fp_rate <= 0.02  # Allow some margin due to randomness

def test_edge_cases():
    bf = BloomFilter(expected_items=1, false_positive_rate=0.01)
    bf.add("")  # Empty string test
    assert bf.check("") is True

    with pytest.raises(TypeError):
        bf.add(None)  # Ensure NoneType input raises error
