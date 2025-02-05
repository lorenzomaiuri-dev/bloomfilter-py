[![Stargazers][stars-shield]][stars-url]
[![License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# Bloom Filter in Python

## Table of Contents

- [Introduction](#introduction)
- [Theory](#theory)
- [Installation](#installation)
- [Usage](#usage)
- [Benchmark](#benchmark)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## Introduction

A **Bloom Filter** is a space-efficient probabilistic data structure that is used to test whether an element is a member of a set. It allows false positives but never false negatives. This makes it ideal for applications where memory efficiency is crucial, such as caching, networking, and databases.

This implementation is optimized for configurability and performance, allowing users to specify the expected number of elements and the desired false positive probability.

## Theory

A Bloom Filter consists of a **bit array** of size `m` and uses `k` different hash functions. When an element is inserted, all `k` hash functions generate indices in the bit array, and the corresponding bits are set to 1.

To check if an element is present:

- Compute its `k` hash values.
- If all bits at those positions are 1, the element **may be present** (with a certain probability of false positives).
- If at least one bit is 0, the element is **definitely not present**.

### Mathematical Formulas

- **Optimal bit array size:**
  \[
  m = - \frac{n \log p}{(\log 2)^2}
  \]
  where `n` is the number of expected elements and `p` is the false positive rate.

- **Optimal number of hash functions:**
  \[
  k = \frac{m}{n} \log 2
  \]

## Installation

To install the Bloom Filter package, run:

```sh
pip install bloomfilter-lite
```

### Installation from source

1. Clone this repository:

   ```bash
    git clone https://github.com/lorenzomaiuri-dev/bloomfilter-py.git
    cd bloomfilter-py
2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv

    source venv/bin/activate  # On Linux/Mac
    venv\Scripts\activate  # On Windows
3. Install the dependencies

    ```bash
    pip install -r requirements.txt

## Usage

### Basic Example

```python
from bloomfilter_lite import BloomFilter

# Create a Bloom Filter for 1000 expected elements with a 1% false positive rate
bf = BloomFilter(expected_items=1000, false_positive_rate=0.01)

# Add elements
bf.add("hello")
bf.add("world")

# Check for membership
print(bf.check("hello"))  # True (probably)
print(bf.check("python")) # False (definitely not present)
```

## Benchmark

Performance testing for different dataset sizes:

| Elements | False Positive Rate | Memory (bits) | Time per Insert (ms) | Time per Lookup (ms) |
|----------|---------------------|--------------|--------------------|--------------------|
| 1,000    | 1%                  | ~9.6 KB      | 0.01               | 0.008              |
| 10,000   | 1%                  | ~96 KB       | 0.015              | 0.010              |
| 100,000  | 1%                  | ~960 KB      | 0.020              | 0.012              |

### Reproducing Benchmarks

To verify the benchmarks, run the following script:

```sh
python benchmarks/run_benchmark.py
```

This script tests insertions and lookups for varying dataset sizes and prints the execution time and memory usage.

## Running Tests

To run the unit tests using `pytest`:

```sh
pytest tests/
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch (git checkout -b feature/your-feature)
3. Commit your changes (git commit -am 'Add new feature')
4. Push the branch (git push origin feature/your-feature)
5. Open a Pull Request

Please ensure all pull requests pass the existing tests and include new tests for any added functionality

## License

This project is licensed under the MIT License. See the LICENSE file for more details

<!-- LINKS & IMAGES -->
[stars-shield]: https://img.shields.io/github/stars/lorenzomaiuri-dev/bloomfilter-py?style=social
[stars-url]: https://github.com/lorenzomaiuri-dev/bloomfilter-py/stargazers
[license-shield]: https://img.shields.io/badge/License-MIT-yellow.svg
[license-url]: https://opensource.org/licenses/MIT
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin&logoColor=white
[linkedin-url]: https://www.linkedin.com/in/maiurilorenzo
