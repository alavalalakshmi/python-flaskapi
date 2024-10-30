def get_statement(cc):
    cc.get_statement()
class CreditCard:
    def __init__(self, balanceDue, cvvNo):
        self.balanceDue = balanceDue
        self.cvvNo = cvvNo

    def get_statement(self):
        print("\nYour Credit Card Balance Due Amount need to be paid is "+ str(self.balanceDue))

class GoldCard(CreditCard):
    def __init__(self, balanceDue, cvvNo):
        super().__init__(balanceDue,cvvNo)
        self.cashBack = 5
    def get_statement(self):
        cashBackAmt = (self.balanceDue * self.cashBack)/100
        self.balanceDue = self.balanceDue - cashBackAmt
        print("\nYour Gold Card Balance Due Amount need to be paid is "+ str(self.balanceDue))
class PlatinumCard(CreditCard):
    def __init__(self, balanceDue, cvvNo):
        super().__init__(balanceDue,cvvNo)
        self.cashBack = 10
    def get_statement(self):
        cashBackAmt = (self.balanceDue * self.cashBack)/100
        self.balanceDue = self.balanceDue - cashBackAmt
        print("\nYour Platinum Card Balance Due Amount need to be paid is "+ str(self.balanceDue))
class SilverCard(CreditCard):
    def __init__(self, balanceDue, cvvNo):
        super().__init__(balanceDue,cvvNo)
        self.cashBack = 2
