import sleekxmpp as xmpp

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

        return self.__execute(self.code, page)

    def __execute(self, code, page):
        '''Wrapper for script execution for when it needs more padding later.'''
        try:
            eval(code, None, {'page': page, 'self': self})
        except Exception as error:
            return (False, error)
        else:
            return True

    def handle(stanza):
        '''This is a placeholder method meant to be replaced by scripts, as this
        method is called when this script's originating JID sends any stanza'''
        print(repr(stanza))


class Dispatcher(xmpp.ClientXMPP):
    
    def __init__(self, jid=None, password=None, endpoint=tuple()):
        self.pages = {}
        self.endpoint = endpoint
        self.networked = False
        if jid and password:
            xmpp.ClientXMPP.__init__(self, jid, password)
            self.networked = True
            self.add_event_handler("session_start", self.start, threaded=False)
            for plug in ['0004', '0030', '0060', '0199']:
                self.registerPlugin('xep_%s' % plug)

    def start(self, event):
        self.getRoster()
        self.sendPresence(ptype='chat')
        
        while True:
            pass


    def load(self, text, jid):
        self.pages[jid] = Dispatcher.__parse(text)
        if self.networked:
            self.registerHandler(xmpp.Callback(
                'Stanzas for %s' % jid,
                xmpp.MatchXMLMask("<message from='%s' />" % jid),
                self.pages[jid].script.handle,
                thread=False))

    def connect(self):
        if self.networked:
            return xmpp.ClientXMPP.connect(self, self.endpoint)
        else:
            return False

    @staticmethod
    def __parse(text):
        text = text.split('\n[--endscript--]\n', 1)
        if len(text) > 1:
            return Page(text[1], Script(text[0]))
        else:
            return Page(text[0])

