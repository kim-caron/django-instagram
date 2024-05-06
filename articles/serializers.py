from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Article, Comment, ArticleMediaFile

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('key','user','like_users','save_users',)


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article', 'user', 'main_comment',)


class ArticleMediaFileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ArticleMediaFile
        fields = '__all__'
        read_only_fields = ('article',)


class CommentListSerializer(serializers.ModelSerializer):

    class CommentUserInfoSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username','profile_image')
 
    user = CommentUserInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        excludes = ('like_users')


class ArticleListSerializer(serializers.ModelSerializer):
    
    files = ArticleMediaFileSerializer(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    like_users_count = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user','like_users','save_users',)


class ProfileSerializer(serializers.ModelSerializer):
    
    class ProfileArticleSerializer(serializers.ModelSerializer):
        
        files = ArticleMediaFileSerializer(many=True, read_only=True)
        comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
        like_users_count = serializers.IntegerField(source='like_users.count', read_only=True)

        class Meta:
            model = Article
            fields = ('key','private',)

    articles = ProfileArticleSerializer(many=True, read_only=True)
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)
    followings_count = serializers.IntegerField(source='followings.count', read_only=True)
    articles_count = serializers.IntegerField(source='article_set.count', read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = '__all__'


class ArticleDetailSerializer(serializers.ModelSerializer):

    files = ArticleMediaFileSerializer(many=True, read_only=True)
    comment_set = CommentSerializer

    class Meta:
        model = Article
        fields = '__all__'

