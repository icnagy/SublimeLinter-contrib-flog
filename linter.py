from SublimeLinter.lint import RubyLinter, LintMatch

"""This module exports the Flog plugin class."""

class Flog(RubyLinter):

    defaults = {
        'selector': 'source.ruby'
    }

    cmd = ('flog', '--blame', '--methods-only', '${file}')
    regex = (
        r'\s*(?P<message>[\d\.]+):[^/]+(?P<filename>.+):(?P<line>\d+)-(?P<end_line>\d+)'
    )
    tempfile_suffix = 'rb'
