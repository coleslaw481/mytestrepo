#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Integration Tests for `mytestrepo` package."""

import os

import unittest
from mytestrepo import mytestrepocmd

SKIP_REASON = 'MYTESTREPO_INTEGRATION_TEST ' \
              'environment variable not set, cannot run integration ' \
              'tests'

@unittest.skipUnless(os.getenv('MYTESTREPO_INTEGRATION_TEST') is not None, SKIP_REASON)
class TestIntegrationMytestrepo(unittest.TestCase):
    """Tests for `mytestrepo` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_something(self):
        """Tests parse arguments"""
        self.assertEqual(1, 1)
