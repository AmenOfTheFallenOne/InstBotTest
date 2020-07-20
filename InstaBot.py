
import random
from instapy import InstaPy
from instapy import smart_run

# login credentials
#insta_username = 'khoshkbar_mojallal'
#insta_password = '09124449704'
insta_username = 'economic_intelligence'
insta_password = '@hldv.,pdn'


dont_likes = ['sex', 'nude']

friends = ['list of friends I do not want to interact with']

#like_tag_list = ['indiegame','gamedev','2dgame','indiegamedev']
#like_tag_list = ['خشکبار','پسته','آجیل','خوراکی','بادام']
like_tag_list = ['بورس','ارز','بازار سرمایه','بازار','سواد مالی']

# prevent posts that contain some plantbased meat from being skipped
ignore_list = ['']

accounts = ['accounts with similar content']

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

with smart_run(session):
    # settings
    session.set_delimit_liking(enabled=True, max_likes=1005, min_likes=20)
    session.set_relationship_bounds(enabled=True,
                                    min_followers=100,
                                    max_followers=10000)
    session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes_hourly=57,
                              peak_likes_daily=585,
                               peak_comments_hourly=21,
                               peak_comments_daily=182,
                                peak_follows_hourly=15,
                                peak_follows_daily=100,
                                 peak_unfollows_hourly=35,
                                 peak_unfollows_daily=402,
                                  peak_server_calls_hourly=None,
                                  peak_server_calls_daily=4700)
    session.set_dont_include(friends)
    session.set_dont_like(dont_likes)
    #session.set_ignore_if_contains(ignore_list)

    session.set_user_interact(amount=2, randomize=True, percentage=60)
    session.set_do_follow(enabled=True, percentage=60)
    session.set_do_like(enabled=True, percentage=80)

    # activity
    
    session.follow_by_tags(random.sample(like_tag_list, 3),
                         amount=random.randint(100, 200), interact=True)
    session.like_by_tags(random.sample(like_tag_list, 3),
                         amount=random.randint(50, 100), interact=True)
    session.unfollow_users(amount=random.randint(75, 150),
                           instapy_followed_enabled=True,
                           instapy_followed_param="all", 
                           style="FIFO",
                           unfollow_after=48 * 60 * 60, sleep_delay=3600)

   # """ Joining Engagement Pods...
   # """
   # photo_comments = ['Nice shot! @{}',
   #     'I love your profile! @{}',
    #    'Wonderful :thumbsup:',
     #   'Just incredible :open_mouth:',
     #   'What camera did you use @{}?',
      #  'Love your posts @{}',
      #  'Looks awesome @{}',
      #  'Getting inspired by you @{}',
      #  ':raised_hands: Yes!',
      #  'I can feel your passion @{} :muscle:']

  #  session.set_do_comment(enabled = True, percentage = 95)
  #  session.set_comments(photo_comments, media = 'Photo')
   ## session.join_pods(topic='travel')
