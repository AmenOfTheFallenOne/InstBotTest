
import random
from instapy import InstaPy
from instapy import smart_run
from instapy.plugins import InstaPyTelegramBot

# login credentials



dont_likes = ['sex', 'nude']

friends = ['list of friends I do not want to interact with']

#like_tag_list = ['indiegame','gamedev','2dgame','indiegamedev']
#like_tag_list = ['خشکبار','پسته','آجیل','خوراکی','بادام']
like_tag_list = ['تحلیل بنیادی']


# prevent posts that contain some plantbased meat from being skipped
ignore_list = ['']

accounts = ['accounts with similar content']

# get a session!
session = InstaPy(nogui=True)

with smart_run(session):
    # settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=5000,
                                    min_followers=20)
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
    
    session.follow_by_tags(like_tag_list, interact=True,amount = 500)
    
    session.unfollow_users(amount=random.randint(75, 150),
                           instapy_followed_enabled=True,
                           instapy_followed_param="all", 
                           style="FIFO",
                           unfollow_after=48 * 60 * 60, sleep_delay=501)
