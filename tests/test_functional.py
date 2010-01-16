from components import Script, Page

class test_associations():

    def setUp(self):
        self.page = Page('I am a test page! How about that?', 
                         Script('print("This is a test script.")'))

    def test_page_should_have_script(self):
        assert self.page.script.body == 'print("This is a test script.")'

    def test_page_should_not_require_script_at_initialization(self):
        assert Page('Only a body').script.body == Script().body

class test_executions():

    def setUp(self):
        self.page = Page('This page only contains text content.')

    def test_page_should_be_runnable(self):
        assert self.page.run()

    def test_script_should_be_executed_when_page_is_run(self):
        '''I don't really know how to test this yet, to be honest, except
        perhaps by testing that the page content gets changed, which we do
        anyway.'''

    def test_script_should_have_access_to_page(self):
        '''Note that the assertion in the script body doesn't actually run, or
        if it does it doesn't puke when the assertion is invalid. Not sure
        why yet. Oh how the list of problems keeps growing.'''
        script_body = 'assert page.content == "This page only contains text content."'
        self.page.script = Script(script_body)
        assert self.page.run() == True

    def test_script_should_be_able_to_modify_page_content(self):
        self.page.script = Script(
            'page.content = page.content.replace("only", "just")')
        self.page.run()
        assert self.page.content == 'This page just contains text content.'


