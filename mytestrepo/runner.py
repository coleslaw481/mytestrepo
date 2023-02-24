#! /usr/bin/env python

import logging


logger = logging.getLogger(__name__)


class MytestrepoRunner(object):
    """
    Class to run algorithm
    """
    def __init__(self, exitcode):
        """
        Constructor

        :param exitcode: value to return via :py:meth:`.MytestrepoRunner.run` method
        :type int:
        """
        self._exitcode = exitcode
        logger.debug('In constructor')

    def run(self):
        """
        Runs My Test Repo


        :return:
        """
        logger.debug('In run method')
        return self._exitcode
