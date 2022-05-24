from datetime import datetime, timezone


class Request_Context:
    def __init__(self, request, **kwargs):
        from .models import Post, Comment
        self.request = request
        self.user = request.user
        if kwargs.get('category', False):
            if kwargs.get('post_id', False):
                self.post = Post.objects.get(id=kwargs['post_id'])
                self.comments = Comment.objects.filter(post=self.post)
            else:
                self.posts = Post.objects.filter(
                    category__name=kwargs['category'])
        else:
            self.posts = Post.objects.all().order_by('-created_on')

    @property
    def categories(self):
        from .models import Category
        return Category.objects.all()


def timeDeltaNow(creation_time):
    now = datetime.now(timezone.utc)
    difference = now - creation_time
    seconds_in_day = 24 * 60 * 60
    result = divmod(difference.days * seconds_in_day +
                    difference.seconds, 60)

    return result


def timeHuman(time_delta):
    if len(time_delta) == 2:
        if time_delta[0] == 0:
            return 'less than a minute ago'
        else:
            return f'{time_delta[0]} minutes ago'
    elif len(time_delta) == 3:
        return f'{time_delta[0]} days ago'
