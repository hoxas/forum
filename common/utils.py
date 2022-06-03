from datetime import datetime, timezone
from django.db.models import QuerySet


class Request_Context_Generic:
    def __init__(self, request):
        from main.forms import PostForm
        self.request = request
        self.user = request.user
        self.PostForm = PostForm
        self.category = False

    @property
    def categories(self) -> QuerySet:
        from main.models import Category
        return Category.objects.all()

    @property
    def all_posts_count(self) -> int:
        from main.models import Post
        return Post.objects.count()

    @property
    def profile(self):
        if self.user.is_authenticated:
            from main.models import Profile
            return Profile.objects.get(user=self.user)
        else:
            return False

    @property
    def get_initial_post_form(self):
        if self.category is not False:
            if self.category != 'main':
                return self.PostForm(initial={'category': self.category})
        return self.PostForm()


def timeDeltaNow(creation_time) -> tuple:
    now = datetime.now(timezone.utc)
    difference = now - creation_time
    seconds_in_day = 24 * 60 * 60
    result = divmod(difference.days * seconds_in_day +
                    difference.seconds, 60)
    return result


def timeHuman(time_delta) -> str:
    minutes_in_hour = 60
    minutes_in_day = 24 * minutes_in_hour
    minutes_in_year = 365 * minutes_in_day

    if time_delta[0] == 0:
        return 'less than a minute ago'
    elif time_delta[0] < minutes_in_hour:
        return f'{time_delta[0]} minutes ago'
    elif time_delta[0] < minutes_in_day:
        return f'{time_delta[0] // minutes_in_hour} hours ago'
    elif time_delta[0] < minutes_in_year:
        return f'{time_delta[0] //  minutes_in_day} days ago'
    elif time_delta[0] >= minutes_in_year:
        return f'{time_delta[0] // minutes_in_year} years ago'
