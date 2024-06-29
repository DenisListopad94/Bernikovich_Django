from __future__ import absolute_import, unicode_literals

import sys
from unittest import TestCase, main, skipUnless
from celery import app as celery_app


__all__ = ('celery_app',)
try:
    from unittest.mock import patch, Mock
except ImportError:
    from mock import patch, Mock

from ..ansitowin32 import StreamWrapper
from ..initialise import init, just_fix_windows_console
from .utils import osname, replace_by

orig_stdout = sys.stdout
orig_stderr = sys.stderr


class InitTest(TestCase):

    @skipUnless(sys.stdout.isatty(), "sys.stdout is not a tty")
    def setUp(self):
        # sanity check
        self.assertNotWrapped()

    def tearDown(self):
        _wipe_internal_state_for_tests()
        sys.stdout = orig_stdout
        sys.stderr = orig_stderr