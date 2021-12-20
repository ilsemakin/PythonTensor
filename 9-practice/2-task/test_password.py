import password as pwd

class TestPassword:
    def test_password_SQFWQFW2(self):
        assert pwd.input_password('SQFWQFW2')
    
    def test_password_fwqfeq352(self):
        assert pwd.input_password('fwqfeq352')

    def test_password_dDqG5(self):
        assert not pwd.input_password('dDqG5')

    def test_password_12345678(self):
        assert not pwd.input_password('12345678')

    def test_password_2PASwoRd5(self):
        assert not pwd.input_password('2PAsSwoRd5')

    def test_password_Spassword(self):
        assert not pwd.input_password('password')