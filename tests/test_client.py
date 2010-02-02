from components import *

class test_connection():

    def setUp(self):
        self.jid = 'test@zuwiki.net/HermesClient'
        self.password = 'test_password'
        self.endpoint = ('zuwiki.net', 5222)
    
    def test_should_connect_with_jid_and_password(self):
        client = Client(self.jid, self.password, self.endpoint)
        assert client.fulljid == self.jid
        client.connect()
        assert client.state['connected']
