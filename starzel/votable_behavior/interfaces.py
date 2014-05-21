# encoding=utf-8
from zope import schema
from zope.interface import Interface
from plone.autoform import directives as form
from plone.supermodel import model

class IVotableLayer(Interface):
    """Marker interface for the Browserlayer
    """

# Ivotable is the marker interface for contenttypes how support this behavior
class IVotable(Interface):
    pass

# This is the behaviors interface. When doing IVoting(object),you receive an
# adapter
class IVoting(model.Schema):

    form.omitted("votes")
    form.omitted("voted")
    votes = schema.Dict(key_type=schema.TextLine(), value_type=schema.Int())
    voted = schema.List(value_type=schema.TextLine())

    def vote(request):
        """
        Store the vote information, store the request hash to ensure
        that the user does not vote twice
        """
        
    def average_vote():
        """
        Return the average voting for an item
        """

    def has_votes():
        """
        Return whether anybody ever voted for this item
        """
        
    def already_voted(request):
        """
        Return the information wether a person already voted.
        This is not very high level and can be tricked out easily
        """

    def clear():
        """
        Clear the votes. Should only be called by admins
        """
