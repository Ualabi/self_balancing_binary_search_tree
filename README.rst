sbbst (Self Balancing Binary Search Tree)
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
*O(1)*          SBBT.getHeightTree()  Height of the tree
*O(logN)*       SBBT.search(x)        Search value
*O(logN)*       SBBT.insert(x)        Insert value
*O(logN)*       SBBT.delete(x)        Delete value
*O(logN)*       SBBT.getMinVal()      Minimum value
*O(logN)*       SBBT.getMaxVal()      Maximum value
*O(K+logN)*     SBBT.kthsmallest(k)   Kth Minimum value
*O(K+logN)*     SBBT.kthlargest(k)    Kth Maximum value
*O(N)*          str(SBBT)             Visualize the tree
=============== ===================== =====================

I made the library **sbbst** with the intention that you can use it easily for your own projects, learning or coding competitions (in which case I would suggest to compile your program with Pypy instead of Python3 and download the code directly from my Github and modify it as your necessities). I used this structure (with a few changes so it can work out with intervals instead of numbers) in the Facebook Hacker Cup 2020 and it was fast enough to pass the time complexity, though I would suggest to migrate to C++ (thing that I have not done properly yet [sept 2020]).

Requirements
============

- Python 2.7+ or 3.4+

Installation
============

To install a stable version from PyPi_:

.. code-block:: bash

    ~$ pip install self_balancing_binary_search_tree

Or download the *__init__.py* file directly from my GitHub_ and worh with it.
    
.. _PyPi: https://pypi.python.org/pypi/sbbst
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

To start working with the library, you will only need 2 lines:

.. code-block:: python

    >>> from sbbst import sbbst
    >>> MT = sbbst()
    
And that will be enough to start working with it. Take the following script as an example

.. code-block:: python
    
    from sbbst import sbbst
    ST = sbbst()
    nums = [128, 131, 4, 134, 135, 10, 1, 3, 140, 14, 142, 145, 146, 147, 149] # random numbers
    for num in nums:
        ST.insert(num)
    # It also works out: ST = sbbst(nums)
    print(ST)
    print("Number of elements:",ST.getSize())
    print("Height:",ST.getHeightTree())
    print("Min val:",ST.getMinVal())
    print("Max val:",ST.getMaxVal())
    print("3rd smallest val:",ST.kthsmallest(3))
    print("2nd largest val:",ST.kthlargest(2))
    print("Pre Order:",ST.inOrder())
    print("In Order:",ST.preOrder())
    print("Post Order:",ST.postOrder())
    ST.delete(128)
    ST.delete(140)
    print(ST)
    ST.insert(55)
    print(ST)
    print("Number of elements:",ST.getSize())
    

This would be the output you will see in the terminal:

::

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
    3rd smallest val: 4
    2nd lasrgets val: 145
    Pre Order: [1, 3, 4, 10, 14, 128, 131, 134, 135, 140, 142, 145, 146, 147, 149]
    In Order: [128, 4, 1, 3, 10, 14, 140, 134, 131, 135, 145, 142, 147, 146, 149]
    Post Order: [3, 1, 14, 10, 4, 131, 135, 134, 142, 146, 149, 147, 145, 140, 128]
    
        ________131______
       /                 \
      _4__            ___142
     /    \          /      \
     1    14       134      145
      \  /  \         \        \
      3 10  21        135      149
              \
              50
    
    
        __________131______
       /                   \
      _4__              ___142
     /    \            /      \
     1    14__       134      145
      \  /    \         \        \
      3 10    50        135      149
             /  \
            21  55
    
    Number of elements: 14


Additionally, I added 3 extra functios (the 3 of them works in *O(N)* time) in case you want to use it along you practice coding in platforms such as LeetCode_ or Interviewbit_. (At the beginning I had troubles to visualize what was happening in the Trees and the DFSs, swaps or insertions, so thats why I worked on in this library as sketch and then improved as it is today.) In those pages the *input* of the trees will be like:

::
    s = "1 2 3 -1 4 -1 5 -1 -1 6 -1 -1 -1"
    s = "1,2,3,null,4,null,5,null,null,6,null,null,null"
    s = [ 1, 2, 3, None, 4, None, 5, None, None, 6, None, None, None ]
    
.. _LeetCode: https://leetcode.com/
.. _Interviewbit: https://www.interviewbit.com/courses/programming/

Some functions you can use are the following:

.. code-block:: python

    from self_balancing_binary_search_tree import TreeNode
    from self_balancing_binary_search_tree import getTree
    from self_balancing_binary_search_tree import getStr
    from self_balancing_binary_search_tree import getList
    # Any of the following s works out
    # s = "1 2 3 -1 4 -1 5 -1 -1 6 -1 -1 -1"
    # s = "1 2 3 None 4 None 5 None None 6 None None None"
    # s = "1,2,3,null,4,null,5,null,null,6,null,null,null"
    s = [ 1, 2, 3, None, 4, None, 5, None, None, 6, None, None, None ]
    head = getTree(s)
    print(getStr(head))
    print("The list of the Tree is:",getList(head))
    
The output in the terminal will be the following:

::

      _1
     /  \
     2  3_
      \   \
      4   5
         /
         6

    The list of the Tree is: [1, 2, None, 4, None, None, 3, None, 5, 6, None, None, None]

Contributing
============

The best way to learn is to copy the code and edit it with your own necessities. You can also find other useful data structures in my GitHub https://github.com/Ualabi/Useful_Data_Structures.

If you want to contribute to this library, please take a look at this page_ before submitting a pull request. Thanks!

.. _page: http://binarytree.readthedocs.io/en/latest/contributing.html

Change Log
==========

- 0.1.3 (09/09/2020)
    - First release
