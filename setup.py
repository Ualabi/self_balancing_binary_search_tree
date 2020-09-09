from setuptools import setup, find_packages

with open('./README.rst') as fp:
    long_description = fp.read()

setup(
    name = "sbbst",
    version = "0.1",
    author = "Joseandres Hinojoza",
    author_email = "jhinojoza@outlook.com",
    description = "A Python implementation of a self balancing binary search tree (AVL Tree). Useful to practice, study and see how a SBBST works.",
    long_description = long_description,
    long_description_content_type = "text/x-rst",
    url = "https://github.com/Ualabi/self_balancing_binary_search_tree",
    license = 'MIT',
    keywords = ['Self Balancing Binary Search Tree','Balanced Binary Search Tree','Binary Search Tree','Binary Tree','AVL Tree','SBBST','BBST','BST','Print Tree','sbbst'],
    packages = find_packages(),
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Education'
    ],
    install_requires = [''],
)
