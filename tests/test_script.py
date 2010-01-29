from components import Script
from nose.tools import raises
from types import CodeType

class test_Script():

    def setUp(self):
        self.script = Script('print("test")')

    def test_should_contain_body(self):
        assert self.script.body == 'print("test")'

    @raises(AttributeError)
    def test_should_not_allow_changing_body(self):
        self.script.body = 'should fail'

    def test_should_allow_empty_body(self):
        assert Script('')
        assert Script()

    def test_should_compile_body_to_code_object(self):
        assert isinstance(self.script.code, CodeType)

class test_Script_execute():

    def test_should_execute_code(self):
        script = Script(
            'test_variable = "I am testing!"\n' \
            'assert test_variable == "I am testing!"')
        assert script.execute()

    def test_should_be_able_to_set_method_on_self(self):
        script = Script(
            'def my_print(str):\n' \
            '    return str\n\n' \
            'self.my_print = my_print')
        script.execute()
        assert script.my_print
        assert script.my_print('test') == 'test'


