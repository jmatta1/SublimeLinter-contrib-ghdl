#
# linter.py
# Linter for SublimeLinter, a code checking framework for Sublime Text
#
# Written by Bruno JJE
# Copyright (c) 2015 Bruno JJE
#
# Modified for
# SublimeLinter defaults/selector usage
# (c) 2019 David Goncalves
#
# License: MIT
#

"""This module exports the Ghdl plugin class."""
from SublimeLinter.lint import Linter, util


class Ghdl(Linter):

    """Provides an interface to ghdl."""

    cmd = 'ghdl -s ${args} ${file}'
    error_stream = util.STREAM_BOTH
    on_stderr = None
    defaults = {
        'selector': 'source.vhdl',
    }

    # Here is a sample ghdl error output:
    # ----8<------------
    # filtre8.vhd:35:3: object class keyword such as 'variable' is expected
    # ----8<------------

    regex = (
        r"^(?P<path>.*):(?P<line>[0-9]+):(?P<col>[0-9]+)"
        r"(?P<error>): (?P<message>.*)"
    )
