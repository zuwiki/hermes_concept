class Page(object):

    def __init__(self, content='', script=None):
        self.content = content
        self.script = script if script else Script()

    def run(self):
        '''"Runs" the page, which currently just means executing the page's
        associated script if it exists and will soon mean rendering the page to
        stdout.'''
        return self.script.execute(self) if self.script else False


class Script(object):

    def __init__(self, body=''):
        self._body = body
        self._code = compile(self._body, repr(self), 'exec')

    def _get_body(self):
        return self._body
    body = property(_get_body)

    def _get_code(self):
        return self._code
    code = property(_get_code)

    def execute(self, page=None):
        '''Calls __execute, which eval()'s the script's code object. `page` will
        be available as a local variable.
        
        Returns True if the script executed without problems, and a tuple of the
        form (False, error) if the script raises an Exception.'''

        return Script.__execute(self.code, page)

    @staticmethod
    def __execute(code, page):
        '''Wrapper for script execution for when it needs more padding later.'''
        try:
            eval(code, None, {'page': page})
        except Exception as error:
            return (False, error)
        else:
            return True


class Dispatcher(object):
    pass


