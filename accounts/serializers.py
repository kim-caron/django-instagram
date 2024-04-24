from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    '''
    [프로필 정보 조회]
    프로필 페이지를 표시하는데 필요한 정보들을 가져옵니다.

    1. 유저의 기본 정보 (닉네임, 프로필 사진, 자기 소개, 링크, 비공개 계정 여부, 인증 계정 여부)
    2. 유저의 팔로우 정보
    3. 작성한 게시글 정보
    4. 스토리 정보
    5. 하이라이트 정보
    '''
    # 역참조 데이터 정보
    

    # 유저의 기본 정보
    class Meta:
        model = get_user_model()
        fields = '__all__'
