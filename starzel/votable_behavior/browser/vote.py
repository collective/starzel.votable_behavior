# encoding=utf-8
from zope.publisher.browser import BrowserPage

from starzel.votable_behavior.interfaces import IVoting


class Vote(BrowserPage):

    def __call__(self, rating):
        voting = IVoting(self.context)
        voting.vote(rating, self.request)
        return "success"


class ClearVotes(BrowserPage):

    def __call__(self):
        voting = IVoting(self.context)
        voting.clear()
        return "success"
