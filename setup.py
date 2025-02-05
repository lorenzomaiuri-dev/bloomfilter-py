from setuptools import setup, find_packages

setup(
    name="bloomfilter-lite",
    version="1.0.0",
    author="Lorenzo maiuri",
    author_email="maiurilorenzo@gmail.com",
    description="A space-efficient probabilistic data structure for membership testing.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lorenzomaiuri-dev/bloomfilter-py",
    packages=find_packages(include=["bloom_filter.py"], where="src"),
    package_dir={"": "src"},
    include_package_data=False,
    install_requires=[
        "bitarray==3.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Information Analysis"
    ],
    python_requires='>=3.6',
    keywords="bloom filter, probabilistic data structures, python",
    project_urls={
        "Source": "https://github.com/lorenzomaiuri-dev/bloomfilter-py",
        "Bug Tracker": "https://github.com/lorenzomaiuri-dev/bloomfilter-py/issues"
    }
)
