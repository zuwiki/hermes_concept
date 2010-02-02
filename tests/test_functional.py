from components import Script, Page
from nose.tools import raises


class test_executions():

    def setUp(self):
        self.page = Page('This page only contains text content.')

    def test_page_should_be_runnable_even_without_a_script(self):
        assert self.page.run()

    def test_should_puke_when_scripts_error(self):
        self.page.script = Script('assert False == True')
        assert False in self.page.run()

    def test_script_should_have_access_to_page(self):
        script_body = 'assert page.content == "This page only contains text content."'
        self.page.script = Script(script_body)
        assert self.page.run() == True

    def test_script_should_be_able_to_modify_page_content(self):
        self.page.script = Script(
            'page.content = page.content.replace("only", "just")')
        self.page.run()
        assert self.page.content == 'This page just contains text content.'


