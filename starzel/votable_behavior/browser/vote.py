# encoding=utf-8
from five import grok

from starzel.votable_behavior.interfaces import IVotable, IVoting


class Vote(grok.View):
    grok.context(IVotable)
    grok.require("zope2.View")

    def render(self, rating):
        voting = IVoting(self.context)
        voting.vote(rating, self.request)
        return "success"


class ClearVotes(grok.View):
    grok.context(IVotable)
    grok.require("zope2.ViewManagementScreens")

    def render(self):
        voting = IVoting(self.context)
        voting.clear()
        return "success"
