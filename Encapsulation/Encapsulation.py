# public attribute

# class Bank:
#     def __init__(self,balance,account_id):
#         self.balance=balance
#         self.account_id=account_id

# print(Bank(4000,1234).balance)
# print(Bank(4000,1234).account_id)
        
# protected attribute 

# class Bank:
#     def __init__(self,balance,account_id):
#         self._balance=balance
#         self._account_id=account_id

# print(Bank(4000,1234)._balance)
# print(Bank(4000,1234)._account_id)

class Bank:
    def __init__(self,balance,account_id):
        self.__balance=balance
        self.__account_id=account_id
        



b=Bank(50000,1234567890)
print(b._Bank__account_id)
print(b._Bank__balance)


