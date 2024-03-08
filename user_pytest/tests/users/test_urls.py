from factories import UserFactory
import pytest
from users.models import User

#pytest.mark.django_db를 사용하면 테스트가 실행되기 전에 데이터베이스를 설정하고 테스트가 끝나면 롤백한다.
pytestmark = pytest.mark.django_db

class TestUserSignUpEndpoints:
    endpoint = '/users/sign-up/'

    #api_client는request 요청의 역할을 함
    def test_create(self, api_client):
        #arrange -> 데이터 준비 단계 (Given)   
        user : User = UserFactory.build()
        #요청 데이터
        request_data = {
            'username': user.username,
            'password': user.password
        }
        #act -> 테스트 대상 메서드를 호출하는 단계 (When)
        #실제 응답
        response = api_client().post(
            self.endpoint,
            data = request_data,
            format="json",
        )
        #assert -> 결과를 검증하는 단계 (Then)
        assert response.status_code == 201
        assert User.objects.filter(username=user.username, password=user.password).exists()
    def test_get(self, api_client):
        response = api_client().get(self.endpoint)
        assert response.status_code == 200
#csrf 테스트도 하기