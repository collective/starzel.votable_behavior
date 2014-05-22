# encoding=utf-8
from starzel.votable_behavior.interfaces import IVoting
from zope.event import notify
from zope.lifecycleevent import ObjectModifiedEvent
from zope.publisher.browser import BrowserPage


class Vote(BrowserPage):

    def __call__(self, rating):
        voting = IVoting(self.context)
        voting.vote(rating, self.request)
        notify(ObjectModifiedEvent(self.context, "A vote has been submitted"))
        return "success"


class ClearVotes(BrowserPage):

    def __call__(self):
        voting = IVoting(self.context)
        voting.clear()
        notify(ObjectModifiedEvent(self.context,
                                   "All votes have been removed"))
        return "success"
