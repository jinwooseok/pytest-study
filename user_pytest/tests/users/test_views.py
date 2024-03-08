import pytest
import factories
from django.urls import reverse
from users.models import User
from users.views import sign_up

#여기있는 파일들 마커는 다 unit임을 선언
pytestmark = [pytest.mark.unit]

class TestUserViews:
    def test_sign_up(self, mocker, rf):
        #arrange -> 데이터 준비 단계 (Given)
        user = factories.UserFactory.build()
        url = reverse('sign-up')
        request = rf.post(url,
                        data={'username': user.username, 'password': user.password},
                        content_type='application/json')
        
        mocker.patch.object(User, 'save')
        
        #act -> 테스트 대상 메서드를 호출하는 단계 (When)
        response = sign_up(request)
        assert response.status_code == 201