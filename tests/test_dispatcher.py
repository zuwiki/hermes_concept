from components import Dispatcher, Page

class test_associations():
    
    def setUp(self):
        self.dispatcher = Dispatcher()

    def test_should_allow_adding_pages_keyed_by_JID(self):
        page = Page('This is just some extra awesome content')
        jid = 'fake_user@example.com/www'
        self.dispatcher.pages[jid] = page
        assert page in self.dispatcher.pages

class test_loading_pages():

    def setUp(self):
        self.dispatcher = Dispatcher()

