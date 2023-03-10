#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `mytestrepo` package."""

import os
import tempfile
import shutil

import unittest
from mytestrepo import mytestrepocmd


class TestMytestrepo(unittest.TestCase):
    """Tests for `mytestrepo` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_parse_arguments(self):
        """Tests parse arguments"""
        res = mytestrepocmd._parse_arguments('hi', [])

        self.assertEqual(res.verbose, 0)
        self.assertEqual(res.exitcode, 0)
        self.assertEqual(res.logconf, None)

        someargs = ['-vv', '--logconf', 'hi', '--exitcode', '3']
        res = mytestrepocmd._parse_arguments('hi', someargs)

        self.assertEqual(res.verbose, 2)
        self.assertEqual(res.logconf, 'hi')
        self.assertEqual(res.exitcode, 3)

    def test_setup_logging(self):
        """ Tests logging setup"""
        try:
            mytestrepocmd._setup_logging(None)
            self.fail('Expected AttributeError')
        except AttributeError:
            pass

        # args.logconf is None
        res = mytestrepocmd._parse_arguments('hi', [])
        mytestrepocmd._setup_logging(res)

        # args.logconf set to a file
        try:
            temp_dir = tempfile.mkdtemp()

            logfile = os.path.join(temp_dir, 'log.conf')
            with open(logfile, 'w') as f:
                f.write("""[loggers]
keys=root

[handlers]
keys=stream_handler

[formatters]
keys=formatter

[logger_root]
level=DEBUG
handlers=stream_handler

[handler_stream_handler]
class=StreamHandler
level=DEBUG
formatter=formatter
args=(sys.stderr,)

[formatter_formatter]
format=%(asctime)s %(name)-12s %(levelname)-8s %(message)s""")

            res = mytestrepocmd._parse_arguments('hi', ['--logconf',
                                                                       logfile])
            mytestrepocmd._setup_logging(res)

        finally:
            shutil.rmtree(temp_dir)

    def test_main(self):
        """Tests main function"""

        # try where loading config is successful
        try:
            temp_dir = tempfile.mkdtemp()
            res = mytestrepocmd.main(['myprog.py'])
            self.assertEqual(res, 0)
        finally:
            shutil.rmtree(temp_dir)
