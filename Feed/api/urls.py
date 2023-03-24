from django.urls import path

from .views import (
    tweet_action_view,
    tweet_delete_view,
    tweet_detail_view,
    tweet_feed_view,
    tweet_list_view,
    tweet_create_view,
    upload_video_view,
    get_videos_view,
    comment_tweet_view,
    comment1_tweet_view,
    comment2_tweet_view,
    comment3_tweet_view,
    comment_video_view,
    see_all_video_comments,
    see_all_tweet_comments,
    see_all_tweet_comments1,
    see_all_tweet_comments2,
    see_all_tweet_comments3
)
'''
CLIENT
Base ENDPOINT /api/tweets/
'''
urlpatterns = [
    path('', tweet_list_view),
    path('tweets/', tweet_feed_view),
    path('action/', tweet_action_view),
    path('create/', tweet_create_view),
    path('<int:tweet_id>/', tweet_detail_view),
    path('<int:tweet_id>/delete/', tweet_delete_view),
    path('uploadvideos/', upload_video_view),
    path('getvideos/', get_videos_view),
    path('commentweet/', comment_tweet_view),
    path('commentweet1/', comment1_tweet_view),
    path('commentweet2/', comment2_tweet_view),
    path('commentweet3/', comment3_tweet_view),
    path('videocomments/<int:pk>/', see_all_video_comments),
    path('commentvideo/', comment_video_view),
    path('tweetcomments/<int:id>/', see_all_tweet_comments),
    path('tweetcomments1/<int:id>/', see_all_tweet_comments1),
    path('tweetcomments2/<int:id>/', see_all_tweet_comments2),
    path('tweetcomments3/<int:id>/', see_all_tweet_comments3)
]