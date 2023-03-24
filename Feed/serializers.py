from email.mime import image
from django.conf import settings
from rest_framework import serializers
from Profiles.serializers import PublicProfileSerializer
from .models import Tweet, Comment, EuropaVideo, CommentEuropaVideo, Comment1, Comment2, Comment3
from django.contrib.humanize.templatetags.humanize import naturaltime


# MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH
TWEET_ACTION_OPTIONS = settings.TWEET_ACTION_OPTIONS

class TweetActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank=True, required=False)
    #image = serializers.ImageField(blank=True,required=False)

    def validate_action(self, value):
        value = value.lower().strip() # "Like " -> "like"
        if not value in TWEET_ACTION_OPTIONS:
            raise serializers.ValidationError("This is not a valid action for tweets")
        return value

class CommentActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank=True, required=False)
    #image = serializers.ImageField(blank=True, required=False)

    def validate_action(self,value):
        value = value.lower().strip()
        if not value in TWEET_ACTION_OPTIONS:
            raise serializers.ValidationError("This is not a valid action for tweets")
        return value


class TweetCreateSerializer(serializers.ModelSerializer):
    # user = PublicProfileSerializer(source='user.profile', read_only=True) # serializers.SerializerMethodField(read_only=True)
    # likes = serializers.SerializerMethodField(read_only=True)
    #image = serializers.SerializerMethodField()
    class Meta:
        model = Tweet
        fields = [
            # 'user', 
            # 'id', 
            'content', 
            # 'likes',
            'video',
            'image', 
            # 'timestamp'
            ]

 
    
    def get_likes(self, obj):
        return obj.likes.count()


    # def get_image(self, obj):
    #     try:
    #         image = obj.image.url
    #     except:
    #         image = None
    #     return image 
    
    # def validate_content(self, value):
    #     if len(value) > MAX_TWEET_LENGTH:
    #         raise serializers.ValidationError("This tweet is too long")
    #     return value

class CommentCreateSerializer(serializers.ModelSerializer):
    # user = PublicProfileSerializer(source='user.profile', read_only=True) # serializers.SerializerMethodField(read_only=True)
    # likes = serializers.SerializerMethodField(read_only=True)
   # image = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            # 'user', 
            # 'id', 
            # 'tweet',
            'content', 
            # 'likes',
            # 'image',  
            # 'timestamp'
            ]


    def get_likes(self, obj):
        return obj.likes.count()

class Comment1CreateSerializer(serializers.ModelSerializer):
    user = PublicProfileSerializer(source='user.profile', read_only=True) # serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
   # image = serializers.SerializerMethodField()
    class Meta:
        model = Comment1
        fields = ['user', 'id', 'comment','content', 'likes','image',  'timestamp']


    def get_likes(self, obj):
        return obj.likes.count()

class Comment2CreateSerializer(serializers.ModelSerializer):
    user = PublicProfileSerializer(source='user.profile', read_only=True) # serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
   # image = serializers.SerializerMethodField()
    class Meta:
        model = Comment2
        fields = ['user', 'id', 'comment1','content', 'likes','image',  'timestamp']


    def get_likes(self, obj):
        return obj.likes.count()
class Comment3CreateSerializer(serializers.ModelSerializer):
    user = PublicProfileSerializer(source='user.profile', read_only=True) # serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
   # image = serializers.SerializerMethodField()
    class Meta:
        model = Comment3
        fields = ['user', 'id', 'comment2','content', 'likes','image',  'timestamp']


    def get_likes(self, obj):
        return obj.likes.count()

#     # def get_image(self, obj):
#     #     try:
#     #         image = obj.image.url
#     #     except:
#     #         image = None
#     #     return image 

#     def validate_content(self, value):
#         if len(value) > MAX_TWEET_LENGTH:
#             raise serializers.ValidationError("This tweet is too long")
#         return value

#     # def get_user(self, obj):
#     #     return obj.user.id




class CommentTweetSerializer(serializers.ModelSerializer):
    user = PublicProfileSerializer(source='user.profile', read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    image = serializers.SerializerMethodField()
    parent = CommentCreateSerializer(read_only=True)
    total_comments = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
                'user', 
                'id', 
                'tweet',
                'content',
                'image',
                'likes',
                'is_retweet',
                'parent',
                'timestamp',
                'total_comments']
    def get_likes(self,obj):
        return obj.likes.count()

    def get_total_comments(self, obj, **kwargs):
        
        total = Comment1.objects.filter(comment=obj.id).count()
        return total


    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image 

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['timestamp'] = naturaltime(instance.timestamp)
        return representation

class Comment1TweetSerializer(serializers.ModelSerializer):
    user = PublicProfileSerializer(source='user.profile', read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    image = serializers.SerializerMethodField()
    parent = Comment1CreateSerializer(read_only=True)
    total_comments = serializers.SerializerMethodField()
    class Meta:
        model = Comment1
        fields = [
                'user', 
                'id', 
                'comment',
                'content',
                'image',
                'likes',
                'is_retweet',
                'parent',
                'timestamp',
                'total_comments']
    def get_likes(self,obj):
        return obj.likes.count()

    def get_total_comments(self, obj, **kwargs):
        
        total = Comment2.objects.filter(comment1=obj.id).count()
        return total


    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image 

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['timestamp'] = naturaltime(instance.timestamp)
        return representation

class Comment2TweetSerializer(serializers.ModelSerializer):
    user = PublicProfileSerializer(source='user.profile', read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    image = serializers.SerializerMethodField()
    parent = Comment2CreateSerializer(read_only=True)
    total_comments = serializers.SerializerMethodField()
    class Meta:
        model = Comment2
        fields = [
                'user', 
                'id', 
                'comment1',
                'content',
                'image',
                'likes',
                'is_retweet',
                'parent',
                'timestamp',
                'total_comments']
    def get_likes(self,obj):
        return obj.likes.count()

    def get_total_comments(self, obj, **kwargs):
        
        total = Comment3.objects.filter(comment2=obj.id).count()
        return total


    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image 

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['timestamp'] = naturaltime(instance.timestamp)
        return representation

class Comment3TweetSerializer(serializers.ModelSerializer):
    user = PublicProfileSerializer(source='user.profile', read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    image = serializers.SerializerMethodField()
    parent = Comment3CreateSerializer(read_only=True)
    total_comments = serializers.SerializerMethodField()
    class Meta:
        model = Comment3
        fields = [
                'user', 
                'id', 
                'comment2',
                'content',
                'image',
                'likes',
                'is_retweet',
                'parent',
                'timestamp',
                'total_comments']
    def get_likes(self,obj):
        return obj.likes.count()

    # def get_total_comments(self, obj, **kwargs):
        
    #     total = Comment.objects.filter(comment3=obj.id).count()
    #     return total


    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image 

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['timestamp'] = naturaltime(instance.timestamp)
        return representation




class TweetSerializer(serializers.ModelSerializer):
    user = PublicProfileSerializer(source='user.profile', read_only=True)
    #tweets_comments = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField(read_only=True)
    #image = serializers.SerializerMethodField()
    parent = TweetCreateSerializer(read_only=True)
    total_comments = serializers.SerializerMethodField()
    class Meta:
        model = Tweet
        fields = [
                'user', 
                'id', 
                'content',
                'image',
                'likes',
                'is_retweet',
                'parent',
                'timestamp',
                'total_comments']

    def get_likes(self, obj):
        return obj.likes.count()

    def get_total_comments(self, obj, **kwargs):
        
        total = Comment.objects.filter(tweet=obj.id).count()
        return total

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['timestamp'] = naturaltime(instance.timestamp)
        return representation

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EuropaVideo
        fields = [
            'user', 
            'videoname', 
            'video',
            'about',
            ]

class CommentVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentEuropaVideo
        fields = [
            'user', 
            'uploadedvideo', 
            'comment',
            ]

    # def get_comments(self, tweet_id):
    #     comment_query  = Comment.objects.filter(
    #             id=tweet_id)
    #     tweets_comments = CommentSerializer(comment_query, many=True)
    #     return tweets_comments

    # def get_comments_count(self,obj):
    #     return obj.tweets_comments.count()



    # def get_image(self, obj):
    #     try:
    #         image = obj.image.url
    #     except:
    #         image = None
    #     return image 
        