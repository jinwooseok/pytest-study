import factory #factory는 상속을 해야하는 번거로움이 있기는 함

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'users.User' #user모델
        
    username = factory.faker.Faker('user_name')
    password = factory.faker.Faker('password')






from model_bakery import baker # static method이므로 사용하기 편할듯

#baker.make('users.User', _quantity=10) #이거는 데이터를 영속화해서 생성한다.

# baker.prepare('users.User', _quantity=10) # 10개의 비영속 더미 데이터 생산


