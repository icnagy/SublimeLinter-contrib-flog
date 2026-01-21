from SublimeLinter.lint import RubyLinter, LintMatch

"""This module exports the Flog plugin class."""

class Flog(RubyLinter):

    defaults = {
        'selector': 'source.ruby',
        'executable': 'flog',
        'threshold': 12.0
    }

    cmd = ('${executable}', '${args}', '${temp_file}')
    regex = (
        r'\s*(?P<message>[\d\.]+):[^/]+(?P<filename>.+):(?P<line>\d+)-(?P<end_line>\d+)'
    )
    tempfile_suffix = 'rb'

    def split_match(self, match):
        """Add near detail to error dict."""

        error = super().split_match(match)
        error['error_type'] = 'error' if float(error['message']) > self.settings.get('threshold') else 'warning'

        return error
