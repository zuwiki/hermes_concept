from components import Page, Script


class test_EmptyPage():

    def setUp(self):
        self.page = Page()

    def test_should_have_no_content(self):
        assert self.page.content == ''


class test_Page():

    def setUp(self):
        self.page = Page('Just some $id[test] content.')

    def test_should_contain_content(self):
        assert self.page.content == 'Just some $id[test] content.'

    def test_should_allow_changing_content(self):
        mutated_content = 'Just some $id[awesome] content.'
        self.page.content = self.page.content.replace('$id[test]', '$id[awesome]')
        
        assert self.page.content == mutated_content


class test_Page_Script_ownership():

    def setUp(self):
        self.page = Page('I am a test page! How about that?', 
                         Script('print("This is a test script.")'))

    def test_page_should_have_script(self):
        assert self.page.script.body == 'print("This is a test script.")'

    def test_page_should_not_require_script_at_initialization(self):
        assert Page('Only a body').script.body == Script().body


