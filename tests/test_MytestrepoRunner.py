#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `mytestrepo` package."""


import unittest
from mytestrepo.runner import MytestrepoRunner


class TestMytestreporunner(unittest.TestCase):
    """Tests for `mytestrepo` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_constructor(self):
        """Tests constructor"""
        myobj = MytestrepoRunner(0)

        self.assertIsNotNone(myobj)

    def test_run(self):
        """ Tests run()"""
        myobj = MytestrepoRunner(4)
        self.assertEqual(4, myobj.run())
