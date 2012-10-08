# encoding=utf-8
from zope.interface import Interface

# Ivotable is the marker interface for contenttypes how support this behavior
class IVotable(Interface):
    pass

# This is the behaviors interface. When doing IVoting(object),you receive an
# adapter
class IVoting(Interface):
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
