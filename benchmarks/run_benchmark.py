import time
from bloomfilter_lite import BloomFilter

def run_benchmark(num_elements, false_positive_rate):
    print(f"Running benchmark for {num_elements} elements with {false_positive_rate * 100}% false positive rate")
    bf = BloomFilter(expected_items=num_elements, false_positive_rate=false_positive_rate)
    
    # Measure insertion time
    start_time = time.time()
    for i in range(num_elements):
        bf.add(f"item{i}")
    insert_time = (time.time() - start_time) / num_elements * 1000  # Convert to ms
    
    # Measure lookup time
    start_time = time.time()
    for i in range(num_elements):
        bf.check(f"item{i}")
    lookup_time = (time.time() - start_time) / num_elements * 1000  # Convert to ms
    
    print(f"Time per insert: {insert_time:.6f} ms")
    print(f"Time per lookup: {lookup_time:.6f} ms")
    print("----------------------")

if __name__ == "__main__":
    test_cases = [
        (1000, 0.01),
        (10000, 0.01),
        (100000, 0.01)
    ]
    
    for num_elements, fp_rate in test_cases:
        run_benchmark(num_elements, fp_rate)
