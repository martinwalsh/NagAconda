"""
Test basic command-line handling of the Plugin class.
"""

import sys
from nose import with_setup
from NagAconda import Plugin
from test import PlugTest
from optparse import OptionError

class TestOptions(PlugTest):
    """
    Test optparse integration with the Plugin class.

    Since our class did not actually extend OptionParser or Option, there's
    a chance something we did damaged the environment. This class ensures
    basic functionality still exists.
    """

    def test_required(self):
        """
        Test that required options are actually required.

        """
        # fixup testrunner output
        _stderr = sys.stderr
        sys.stderr = sys.stdout

        self.plugin.add_option("t", "test", "Test required parameter",
            required=True)

        try:
            self.plugin.start()
        except SystemExit, e:
            assert e.code == 2
        else:
            assert False
        finally:
            sys.stderr = _stderr

    def test_parameter(self):
        """
        Test that a specified parameter actually reaches our option list.

        """
        self.plugin.add_option("t", "test", "Test required parameter",
            required=True)
        sys.argv.extend(['-t', 'this.is.a.test'])
        self.plugin.start()

        assert self.plugin.options.test == 'this.is.a.test'

