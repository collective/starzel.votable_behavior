# -*- coding: utf-8 -*-
from plone import api
from plone.restapi.deserializer import json_body
from plone.restapi.services import Service
from starzel.votable_behavior import DoVote
from starzel.votable_behavior.interfaces import IVoting
from zope.globalrequest import getRequest


class Vote(Service):
    """Vote for an object"""

    def reply(self):

        can_vote = not api.user.is_anonymous() and api.user.has_permission(DoVote, obj=self.context)
        if can_vote:
            voting = IVoting(self.context)
            data = json_body(self.request)
            vote = data['rating']
            voting.vote(vote, self.request)

        return vote_info(self.context, self.request)


class Delete(Service):
    """Unlock an object"""

    def reply(self):
        voting = IVoting(self.context)
        voting.clear()
        return vote_info(self.context, self.request)


class Votes(Service):
    """Voting information about the current object"""

    def reply(self):
        return vote_info(self.context, self.request)


def vote_info(obj, request=None):
    """Returns voting information about the given object."""
    if not request:
        request = getRequest()
    voting = IVoting(obj)
    can_vote = not api.user.is_anonymous() and api.user.has_permission(DoVote, obj=obj)
    info = {
        'average_vote': voting.average_vote(),
        'has_votes': voting.has_votes(),
        'already_voted': voting.already_voted(request),
        'can_vote': can_vote,
    }
    return info
