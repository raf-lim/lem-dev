from django.db import models


class ReactionManager(models.Manager):
    pass


class ReactionQuerySet(models.QuerySet):
    """
    A queryset for Reaction models.
    """

    def likes(self):
        """
        Return a queryset of reactions that are like type.
        """
        return self.filter(reaction_type="L")

    def dislikes(self):
        """
        Return a queryset of reactions that are dislike type.
        """
        return self.filter(reaction_type="D")


ReactionManager = ReactionManager.from_queryset(ReactionQuerySet)
