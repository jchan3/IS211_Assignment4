#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for Joe Chan: search_compare.py."""


import time
import random


def sequential_search(a_list, item):
    """Conducts a sequential search of a list for a specific item.

    Args:
        a_list(list): The list being searched.
        item(string): The item to search for.

    Returns:
        tuple: found (A boolean variable) and end-start (The value of end value
        subtracted to start value.
    """
    start = time.time()

    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1

    end = time.time()
    return (found, end-start)


def ordered_sequential_search(a_list, item):
    """Conducts an ordered sequential search of a list for a specific item.

    Args:
        a_list(list): The list being searched.
        item(string): The item to search for.

    Returns:
        tuple: found (A boolean variable) and end-start (The value of end value
        subtracted to start value.
    """
    start = time.time()

    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1

    end = time.time()
    return (found, end-start)


def binary_search_iterative(a_list, item):
    """Conducts a binary search of a list for a specific item.

    Args:
        a_list(list): The list being searched.
        item(string): The item to search for.

    Returns:
        tuple: found (A boolean variable) and end-start (The value of end value
        subtracted to start value.
    """
    start = time.time()

    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end = time.time()
    return (found, end-start)


def binary_search_recursive(a_list, item):
    """Conducts a recursive binary search of a list for a specific item.

    Args:
        a_list(list): The list being searched.
        item(string): The item to search for.

    Returns:
        found: A boolean variable.
    """
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item)
        else:
            return binary_search_recursive(a_list[midpoint+1:], item)


if __name__ == "__main__":
    ss_list = []
    oss_list = []
    bsi_list = []
    bsr_list = []
    a = []
    b = []
    c = []

    for j in xrange(100):
        templist = []
        for i in xrange(500):
            temp = random.randint(1, 100)
            templist.append(temp)

        templist.sort()
        ss_list.append(sequential_search(templist, -1))
        oss_list.append(ordered_sequential_search(templist, -1))
        bsi_list.append(binary_search_iterative(templist, -1))
        start = time.time()
        tvalue = (binary_search_recursive(templist, -1))
        end = time.time()
        bsr_list.append(end-start)

    for k in xrange(100):
        a.append(ss_list[k][1])
        b.append(oss_list[k][1])
        c.append(bsi_list[k][1])

    ss_avg = sum(a) / 100
    oss_avg = sum(b) / 100
    bsi_avg = sum(c) / 100
    bsr_avg = sum(bsr_list) / 100

    print "Results of lists of size 500: "
    print "Sequential Search took %10.7f seconds to run on average" % ss_avg
    print ("Ordered Sequential Search took %10.7f seconds to run on average" %
           oss_avg)
    print ("Binary Search Iterative took %10.7f seconds to run on average" %
           bsi_avg)
    print ("Binary Search Recursive took %10.7f seconds to run on average" %
           bsr_avg)

    ss_list = []
    oss_list = []
    bsi_list = []
    bsr_list = []
    a = []
    b = []
    c = []

    for j in xrange(100):
        templist = []
        for i in xrange(1000):
            temp = random.randint(1, 100)
            templist.append(temp)

        templist.sort()
        ss_list.append(sequential_search(templist, -1))
        oss_list.append(ordered_sequential_search(templist, -1))
        bsi_list.append(binary_search_iterative(templist, -1))
        start = time.time()
        tvalue = (binary_search_recursive(templist, -1))
        end = time.time()
        bsr_list.append(end-start)

    for k in xrange(100):
        a.append(ss_list[k][1])
        b.append(oss_list[k][1])
        c.append(bsi_list[k][1])

    ss_avg = sum(a) / 100
    oss_avg = sum(b) / 100
    bsi_avg = sum(c) / 100
    bsr_avg = sum(bsr_list) / 100

    print "Results of lists of size 1,000: "
    print "Sequential Search took %10.7f seconds to run on average" % ss_avg
    print ("Ordered Sequential Search took %10.7f seconds to run on average" %
           oss_avg)
    print ("Binary Search Iterative took %10.7f seconds to run on average" %
           bsi_avg)
    print ("Binary Search Recursive took %10.7f seconds to run on average" %
           bsr_avg)

    ss_list = []
    oss_list = []
    bsi_list = []
    bsr_list = []
    a = []
    b = []
    c = []

    for j in xrange(100):
        templist = []
        for i in xrange(10000):
            temp = random.randint(1, 100)
            templist.append(temp)

        templist.sort()
        ss_list.append(sequential_search(templist, -1))
        oss_list.append(ordered_sequential_search(templist, -1))
        bsi_list.append(binary_search_iterative(templist, -1))
        start = time.time()
        tvalue = (binary_search_recursive(templist, -1))
        end = time.time()
        bsr_list.append(end-start)

    for k in xrange(100):
        a.append(ss_list[k][1])
        b.append(oss_list[k][1])
        c.append(bsi_list[k][1])

    ss_avg = sum(a) / 100
    oss_avg = sum(b) / 100
    bsi_avg = sum(c) / 100
    bsr_avg = sum(bsr_list) / 100

    print "Results of lists of size 10,000: "
    print "Sequential Search took %10.7f seconds to run on average" % ss_avg
    print ("Ordered Sequential Search took %10.7f seconds to run on average" %
           oss_avg)
    print ("Binary Search Iterative took %10.7f seconds to run on average" %
           bsi_avg)
    print ("Binary Search Recursive took %10.7f seconds to run on average" %
           bsr_avg)
