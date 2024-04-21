from django.db import models
from django.contrib.auth.models import AbstractUser

def profile_image_path(instance, filename):
    return f'profile/{instance.pk}.jpg'

# Create your models here.
class User(AbstractUser):
    '''
    [모델 구성]
    username = 유저의 사용자 이름(닉네임)
    email = 이메일
    password = 패스워드
    followings = 유저 팔로잉 정보 
    friend = 친한 친구 정보
    private = 비공개 여부
    verified = 프로필 인증
    profile_image = 프로필 사진
    introduce = 프로필 소개
    phone = 전화 번호
    name = 본명
    gender = 성별(Null - 밝히고 싶지 않음)
    link = 링크
    userId = 회원가입 시에 입력 받는 휴대폰 번호나 이메일 정보
    created_at = 계정 생성 날짜
    '''
    followings = models.ManyToManyField('self',symmetrical=False,related_name='followers')
    friend = models.ManyToManyField('self',symmetrical=False,related_name='friendly')
    private = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to=profile_image_path,default='default/profile.jpg')
    introduce = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    userId = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)