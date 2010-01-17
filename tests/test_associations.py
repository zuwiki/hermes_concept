from components import Page, Script

class test_Page_Script_ownership():

    def setUp(self):
        self.page = Page('I am a test page! How about that?', 
                         Script('print("This is a test script.")'))

    def test_page_should_have_script(self):
        assert self.page.script.body == 'print("This is a test script.")'

    def test_page_should_not_require_script_at_initialization(self):
        assert Page('Only a body').script.body == Script().body


