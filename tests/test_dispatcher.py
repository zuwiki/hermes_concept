from components import Dispatcher, Page


class test_associations():
    
    def setUp(self):
        self.dispatcher = Dispatcher()

    def test_should_allow_adding_pages_keyed_by_JID(self):
        page = Page('This is just some extra awesome content')
        jid = 'fake_user@example.com/www'
        self.dispatcher.pages[jid] = page
        assert jid in self.dispatcher.pages
        assert self.dispatcher.pages[jid] == page


class test_loading_pages():

    def setUp(self):
        self.dispatcher = Dispatcher()
        self.text = 'This is only text. No trickery here.'
        self.script = 'page.content = page.content + " Although now there is!"'
        self.jid = 'website@example.com/www'

    def test_should_load_simple_text_page(self):
        self.dispatcher.load(self.text, self.jid)
        assert self.dispatcher.pages[self.jid].content == Page(self.text).content

    def test_should_load_page_with_script(self):
        self.dispatcher.load('%s\n[--endscript--]\n%s' % (self.script, self.text),
                             self.jid)
        assert self.dispatcher.pages[self.jid].content == self.text
        assert self.dispatcher.pages[self.jid].script.body == self.script


class test_connection():

    def setUp(self):
        self.jid = 'test@zuwiki.net/HermesClient'
        self.password = 'test_password'
        self.endpoint = ('zuwiki.net', 5222)
        self.dispatcher = Dispatcher(self.jid, self.password, self.endpoint)
    
    def test_should_connect_with_jid_and_password(self):
        assert self.dispatcher.fulljid == self.jid
        assert self.dispatcher.connect()
        assert self.dispatcher.state['connected']

    def test_should_fail_peacefully_without_jid_or_password(self):
        dispatcher = Dispatcher()
        assert dispatcher.connect() == False

