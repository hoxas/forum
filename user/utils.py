from common.utils import *


class Request_Context(Request_Context_Generic):
    def __init__(self, request, **kwargs):
        super().__init__(request)
        from user.models import Profile
        self.profile = self.profile_search = False

        if request.user.is_authenticated:
            if kwargs.get('profile', False):
                self.profile_search = Profile.objects.get(
                    displayname=kwargs['profile'])
            else:
                self.profile = Profile.objects.get(
                    user=request.user).displayname
