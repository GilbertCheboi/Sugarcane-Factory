import random
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.db.models import Q

User = settings.AUTH_USER_MODEL

class EuropaTweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class EuropaCommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class EuropaCommentLike1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment1 = models.ForeignKey("Comment1", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class EuropaCommentLike2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment2 = models.ForeignKey("Comment2", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class EuropaCommentLike3(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment3 = models.ForeignKey("Comment3", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class TweetQuerySet(models.QuerySet):
    def by_username(self, username):
        return self.filter(user__username__iexact=username)

    def feed(self, user):
        profiles_exist = user.following.exists()
        followed_users_id = []
        if profiles_exist:
            followed_users_id = user.following.values_list("user__id", flat=True) # [x.user.id for x in profiles]
        return self.filter(
            Q(user__id__in=followed_users_id) |
            Q(user=user)
        ).distinct().order_by("-timestamp")

class TweetManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return TweetQuerySet(self.model, using=self._db)

    def feed(self, user):
        return self.get_queryset().feed(user)




class Tweet(models.Model):
    # Maps to SQL data
    # id = models.AutoField(primary_key=True)
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Europatweets") # many users can many tweets
    likes = models.ManyToManyField(User, related_name='Europatweet_user', blank=True, through=EuropaTweetLike)
    content = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    #comments = models.ForeignKey("Comment", on_delete=models.CASCADE, related_name="Baseballcomments")

    objects = TweetManager()
    # def __str__(self):
    #     return self.content
    
    class Meta:
        ordering = ['-id']
    
    @property
    def is_retweet(self):
        return self.parent != None
    
    def serialize(self):
        '''
        Feel free to delete!
        '''
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200)
        }

    # @property
    # def comments(self):
    #     instance = self
    #     qs = Comment.objects.filter_by_instance(instance)
    #     return qs

    # @property
    # def get_content_type(self):
    #     instance = self
    #     content_type = ContentType.objects.get_for_model(instance.__class__)
    #     return content_type



class Comment(models.Model):
    #id = models.AutoField(primary_key=True)
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    tweet = models.ForeignKey(Tweet,  on_delete=models.CASCADE, null=True, related_name="Europa_comments")
    # user=models.ForeignKey(User,on_delete=models.CASCADE, related_name="Europacomments")
    likes = models.ManyToManyField(User, related_name='Europacomment_user', blank=True, through=EuropaCommentLike)
    content=models.TextField(blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    

    objects = TweetManager()

 #   def __str__(self):
  #      return 'comment on {} by {}'.format(self.post.title,self.user.username)




    class Meta:
        ordering = ['-id']
    
    @property
    def is_retweet(self):
        return self.parent != None
    
    def serialize(self):
        '''
        Feel free to delete!
        '''
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200)
        }




    class Meta:
        ordering = ['-id']
    
    @property
    def is_retweet(self):
        return self.parent != None
    from django.db import models

class Comment1(models.Model):
    #id = models.AutoField(primary_key=True)
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    comment = models.ForeignKey(Comment,  on_delete=models.CASCADE, null=True, related_name="Europa_comments1")
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name="Europacomments1")
    likes = models.ManyToManyField(User, related_name='Europacomment1_user', blank=True, through=EuropaCommentLike1)
    content=models.TextField(blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    

    objects = TweetManager()

 #   def __str__(self):
  #      return 'comment on {} by {}'.format(self.post.title,self.user.username)




    class Meta:
        ordering = ['-id']
    
    @property
    def is_retweet(self):
        return self.parent != None
    
    def serialize(self):
        '''
        Feel free to delete!
        '''
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200)
        }




    class Meta:
        ordering = ['-id']
    
    @property
    def is_retweet(self):
        return self.parent != None
    from django.db import models

class Comment2(models.Model):
    #id = models.AutoField(primary_key=True)
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    comment1 = models.ForeignKey(Comment1,  on_delete=models.CASCADE, null=True, related_name="Europa_comments2")
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name="Europacomments2")
    likes = models.ManyToManyField(User, related_name='Europacomment2_user', blank=True, through=EuropaCommentLike2)
    content=models.TextField(blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    

    objects = TweetManager()

 #   def __str__(self):
  #      return 'comment on {} by {}'.format(self.post.title,self.user.username)




    class Meta:
        ordering = ['-id']
    
    @property
    def is_retweet(self):
        return self.parent != None
    
    def serialize(self):
        '''
        Feel free to delete!
        '''
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200)
        }




    class Meta:
        ordering = ['-id']
    
    @property
    def is_retweet(self):
        return self.parent != None
    from django.db import models

class Comment3(models.Model):
    #id = models.AutoField(primary_key=True)
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    comment2 = models.ForeignKey(Comment2,  on_delete=models.CASCADE, null=True, related_name="Europa_comments3")
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name="Europacomments3")
    likes = models.ManyToManyField(User, related_name='Europacomment3_user', blank=True, through=EuropaCommentLike3)
    content=models.TextField(blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    

    objects = TweetManager()

 #   def __str__(self):
  #      return 'comment on {} by {}'.format(self.post.title,self.user.username)




    class Meta:
        ordering = ['-id']
    
    @property
    def is_retweet(self):
        return self.parent != None
    
    def serialize(self):
        '''
        Feel free to delete!
        '''
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200)
        }




    class Meta:
        ordering = ['-id']
    
    @property
    def is_retweet(self):
        return self.parent != None
    from django.db import models
# Create your models here.
class EuropaVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    videoname = models.CharField(max_length=50)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    about = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.videoname

class CommentEuropaVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    uploadedvideo = models.ForeignKey(EuropaVideo, on_delete=models.CASCADE, related_name="europa_uploadedvideo")
    comment = models.CharField(max_length=275, null=False)