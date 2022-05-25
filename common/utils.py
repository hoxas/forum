from datetime import datetime, timezone


class Request_Context_Generic:
    def __init__(self, request):
        self.request = request
        self.user = request.user

    @property
    def categories(self):
        from main.models import Category
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
