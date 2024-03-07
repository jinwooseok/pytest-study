#conftest : factory를 고정시킬거임
from . import factories
def utbb():
    def filled_user_bakery_batch():
        '''공장에다가 이거 생성요청하는거임..
        baker인 경우 static이니까 그냥 써도 되고
        만약 factory_boy쓴다고하면 import해야할듯'''
        factories.UserFactory.create_batch(10)
        