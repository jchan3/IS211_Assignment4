#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for Joe Chan: sort_compare.py."""


import time
import random


def insertion_sort(a_list):
    """Sorts a list of numbers in ascending order using sublists.

    Args:
        a_list(list): The list being searched.

    Returns:
        None.
    """
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position-1] > current_value:
            a_list[position] = a_list[position-1]
            position = position - 1
        a_list[position] = current_value
    return


def shell_sort(a_list):
    """Sorts a list of numbers in ascending order using several sublists.

    Args:
        a_list(list): The list being searched.

    Returns:
        None.
    """
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    return


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value
    return


def python_sort(a_list):
    """Sorts a list of numbers in ascending order using the sort function.

    Args:
        a_list(list): The list being searched.

    Returns:
        None.
    """
    a_list.sort()
    return


if __name__ == "__main__":
    is_list = []
    ss_list = []
    ps_list = []

    for j in xrange(100):
        templist = []
        temp_copy = []
        temp_copy2 = []
        for k in xrange(500):
            temp = random.randint(1, 100)
            templist.append(temp)

        temp_copy = templist[:]
        temp_copy2 = templist[:]

        start = time.time()
        insertion_sort(templist)
        end = time.time()
        is_list.append(end-start)

        start = time.time()
        shell_sort(temp_copy)
        end = time.time()
        ss_list.append(end-start)

        start = time.time()
        python_sort(temp_copy2)
        end = time.time()
        ps_list.append(end-start)

    is_avg = sum(is_list) / 100
    ss_avg = sum(ss_list) / 100
    ps_avg = sum(ps_list) / 100

    print "Results of lists of size 500: "
    print "Insertion Sort took %10.7f seconds to run on average" % is_avg
    print "Shell Sort took %10.7f seconds to run on average" % ss_avg
    print "Python Sort took %10.7f seconds to run on average" % ps_avg

    is_list = []
    ss_list = []
    ps_list = []

    for j in xrange(100):
        templist = []
        temp_copy = []
        temp_copy2 = []
        for k in xrange(1000):
            temp = random.randint(1, 100)
            templist.append(temp)

        temp_copy = templist[:]
        temp_copy2 = templist[:]

        start = time.time()
        insertion_sort(templist)
        end = time.time()
        is_list.append(end-start)

        start = time.time()
        shell_sort(temp_copy)
        end = time.time()
        ss_list.append(end-start)

        start = time.time()
        python_sort(temp_copy2)
        end = time.time()
        ps_list.append(end-start)

    is_avg = sum(is_list) / 100
    ss_avg = sum(ss_list) / 100
    ps_avg = sum(ps_list) / 100

    print "Results of lists of size 1,000: "
    print "Insertion Sort took %10.7f seconds to run on average" % is_avg
    print "Shell Sort took %10.7f seconds to run on average" % ss_avg
    print "Python Sort took %10.7f seconds to run on average" % ps_avg

    is_list = []
    ss_list = []
    ps_list = []

    for j in xrange(100):
        templist = []
        temp_copy = []
        temp_copy2 = []
        for k in xrange(10000):
            temp = random.randint(1, 100)
            templist.append(temp)

        temp_copy = templist[:]
        temp_copy2 = templist[:]

        start = time.time()
        insertion_sort(templist)
        end = time.time()
        is_list.append(end-start)

        start = time.time()
        shell_sort(temp_copy)
        end = time.time()
        ss_list.append(end-start)

        start = time.time()
        python_sort(temp_copy2)
        end = time.time()
        ps_list.append(end-start)

    is_avg = sum(is_list) / 100
    ss_avg = sum(ss_list) / 100
    ps_avg = sum(ps_list) / 100

    print "Results of lists of size 10,000: "
    print "Insertion Sort took %10.7f seconds to run on average" % is_avg
    print "Shell Sort took %10.7f seconds to run on average" % ss_avg
    print "Python Sort took %10.7f seconds to run on average" % ps_avg
