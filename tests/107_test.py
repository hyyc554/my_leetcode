# -*- coding: utf-8 -*-
"""
@Time    : 2020/5/15 21:25
@Author  : Yancy
@Email   : hyc554@gmail.com
@File    : 107_test.py

"""
import pytest
from tree.leetcode107


def test_max():
    values = (2, 3, 1, 4, 6)

    val = utils.algo.max(values)
    assert val == 6