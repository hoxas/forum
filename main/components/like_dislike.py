
from django_unicorn.components import UnicornView
from user.models import Profile
from ..models import Comment


class LikeDislikeView(UnicornView):
    profile: Profile = None
    comment: Comment = None
    likes: int = 0
    dislikes: int = 0

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.comment_id = kwargs.get("comment_id")

    def mount(self):
        self.profile = self.request.user.profile
        self.comment = Comment.objects.get(id=self.comment_id)
        self.likes = self.comment.likes.count()
        self.dislikes = self.comment.dislikes.count()

        return super().mount()

    def like(self):
        if self.profile in self.comment.likes.all():
            self.comment.likes.remove(self.profile)
        elif self.profile in self.comment.dislikes.all():
            self.comment.dislikes.remove(self.profile)
            self.comment.likes.add(self.profile)
            self.dislikes = self.comment.dislikes.count()
        else:
            self.comment.likes.add(self.profile)
        self.likes = self.comment.likes.count()

    def dislike(self):
        if self.profile in self.comment.dislikes.all():
            self.comment.dislikes.remove(self.profile)
        elif self.profile in self.comment.likes.all():
            self.comment.likes.remove(self.profile)
            self.comment.dislikes.add(self.profile)
            self.likes = self.comment.likes.count()
        else:
            self.comment.dislikes.add(self.profile)
        self.dislikes = self.comment.dislikes.count()
