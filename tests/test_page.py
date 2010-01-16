from components import Page

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

