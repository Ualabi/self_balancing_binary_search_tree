self_balancing_binary_search_tree
---------------------------------
A Python implementation of a self balancing binary search tree (AVL Tree). Useful to practice, study and see how the SBBTs works.

Introduction
============

A **self-balancing binary search tree** is a data structure, a kind advanced one I would say, that optimizes the times for insertion, deletion and serching. Even though there a few types of SBBSTs (2–3 tree, AA tree, AVL tree, B-tree, Red–black tree, ...), in this library I decided to implement the AVL Tree because I consider it as the easiest one.

It has *O(N)* space in memory and its respectives times and functions are:

=============== ===================== =====================
Time complexity Function in the class Action             
=============== ===================== =====================
*O(1)*          SBBT.getSize()        Size of the tree   
*O(logN)*       SBBT.search(x)        Search value
*O(logN)*       SBBT.insert(x)        Insert value
*O(logN)*       SBBT.delete(x)        Delete value
*O(logN)*       SBBT.getMinVal()      Minimum value
*O(logN)*       SBBT.getMaxVal()      Maximum value
*O(K+logN)*     SBBT.kthsmallest(k)   Kth Minimum value
*O(K+logN)*     SBBT.kthlargest(k)    Kth Maximum value
*O(N)*          SBBT.getHeight()      Height of the tree
=============== ===================== =====================

I made the library **self_balancing_binary_search_tree** (sorry for the long name) with the intention that you can use it easily for your own projects, learning or coding competitions (in which case I would suggest to compile your program with Pypy instead of Python3 and download the code directly from my Github and modify it as your necessities).

Requirements
============

- Python 2.7+ or 3.4+

Installation
============

To install a stable version from PyPi_:

.. code-block:: bash

    ~$ pip install self_balancing_binary_search_tree

Or download the init.py file directly from my GitHub_ and worh with it.
    
.. _PyPi: https://pypi.python.org/pypi/self_balancing_binary_search_tree
.. _GitHub: https://github.com/Ualabi/self_balancing_binary_search_tree

The library works with the tree nodes defined as:

.. code-block:: python

    class TreeNode():
        def __init__ (self, val):
            self.val = val
            self.place = 0  # helps in the print process
            self.height = 1 # mandatory in the AVL Trees
            self.left = None
            self.right = None

Getting Started
===============

To start working with the library, you will only need 2 lines more:

.. code-block:: python

    >>> from self_balancing_binary_search_tree import SBBST
    >>> MT = SBBST()
    
And that will be enough to start working with it. Take the following script as example

.. code-block:: python
    
    from self_balancing_binary_search_tree import SBBST
    MT = SBBST()
    nums = [128, 131, 4, 134, 135, 10, 1, 3, 140, 14, 142, 145, 146, 147, 149] # random numbers
    for num in nums:
        MT.insert(num)
    print(BT)
    print("Number of elements:",BT.getSize())
    print("Height:",BT.Height())
    print("Min val:",BT.getMinVal())
    print("Max val:",BT.getMaxVal())
    print("Pre Order:",BT.inOrder())
    print("In Order:",BT.preOrder()
    print("Post Order:",BT.postOrder())

This would be the output you will see in the terminal:

.. code-block:: txt

        ____128_________
       /                \
      _4             ___140___
     /  \           /         \
     1  10        134         145___
      \   \      /   \       /      \
      3   14   131   135   142      147
                                   /   \
                                 146   149
    
    Number of elements: 15
    Height: 5
    Min val: 1
    Max val: 149
    Pre Order: [1, 3, 4, 10, 14, 128, 131, 134, 135, 140, 142, 145, 146, 147, 149]
    In Order: [128, 4, 1, 3, 10, 14, 140, 134, 131, 135, 145, 142, 147, 146, 149]
    Post Order: [3, 1, 14, 10, 4, 131, 135, 134, 142, 146, 149, 147, 145, 140, 128]
    
Additionally, I add a second class in case you want to use it along practice coding in platforms such as LeetCode_ or Interbiewbit_. At the beginning I had troubles to visualize what was happening in the Tree, such as the DFSs, swaps or insertions, so thats why I worked on in this library as sketch and then improved as it is today. 

.. _LeetCode: https://leetcode.com/p
.. _Interviewbit: https://www.interviewbit.com/courses/programming/

.. code-block:: python

    >>> from binarytree import TreeNode
    >>> head = Node(1)
    >>> head.left = Node(1)
    >>> head.right = Node(3)
    >>> head.left.right = Node(4)
    >>> head.right.left = Node(5)
    >>> head.right.right = Node(6)
    >>> print(head)
     _1_
    /   \
    2   3
     \ / \
     4 5 6
    

Inspect tree properties:


`List representations`_ are also supported:

.. _List representations: https://en.wikipedia.org/wiki/Binary_tree#Arrays

.. code-block:: python

    >>> from binarytree import build
    >>>
    >>> # Build a tree from list representation
    >>> values = [7, 3, 2, 6, 9, None, 1, 5, 8]
    >>> root = build(values)
    >>> print(root)
    #
    #            __7
    #           /   \
    #        __3     2
    #       /   \     \
    #      6     9     1
    #     / \
    #    5   8
    #
    >>> # Convert the tree back to list representation
    >>> root.values
    [7, 3, 2, 6, 9, None, 1, 5, 8]

Check out the documentation_ for more details!

.. _documentation: http://binarytree.readthedocs.io/en/latest/index.html

Contributing
============

Please have a look at this page_ before submitting a pull request. Thanks!

.. _page: http://binarytree.readthedocs.io/en/latest/contributing.html
