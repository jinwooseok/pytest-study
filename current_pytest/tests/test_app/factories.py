'''model bakery 인터페이스'''
from model_bakery import baker

class BakeryFactory:
    '''모든 모델에 대한 베이커리 팩토리를 만들기 위한 클래스'''
    def __init__(self, model_name, add_param={}, n=1):
        self.name = model_name
        self.add_param = add_param
        self.n = n

    def make(self, _fill_optional=None):
        '''모델 데이터 생성'''
        if _fill_optional is None:
            return baker.make(
                self.name,
                **self.add_param,
                _quantity=self.n
            )
        else:
            return baker.make(
                self.name,
                **self.add_param,
                _fill_optional=_fill_optional,
                _quantity=self.n
            )

    def prepare(self, _fill_optional=None):
        '''모델 데이터 빌드'''
        if _fill_optional is None:
            return baker.prepare(
                self.name,
                **self.add_param,
                _quantity=self.n
            )   
        else:
            return baker.prepare(
                self.name,
                **self.add_param,
                _fill_optional=_fill_optional,
                _quantity=self.n
            )

class TransactionBakery(BakeryFactory):
    '''Transaction 모델 데이터 생성'''
    def __init__(self, add_param={}, n=1):
        self.name = 'app1.Transaction'
        super().__init__(self.name, add_param, n)

class CurrencyBakery(BakeryFactory):
    '''Currency 모델 데이터 생성'''
    def __init__(self, add_param={}, n=1):
        self.name = 'app1.Currency'
        super().__init__(self.name, add_param, n)
