# encoding=utf-8
from hashlib import md5
from persistent.dict import PersistentDict
from persistent.list import PersistentList
from Products.CMFPlone.utils import safe_bytes
from zope.annotation.interfaces import IAnnotations

# The key must be unique. Using the class name with the complete module name
# is a good idea. But be careful, you might want to change the key if you move
# the location to a different place. Else you won't find your own annotations
KEY = "starzel.votable_behavior.behavior.voting.Vote"


class Vote(object):
    def __init__(self, context):
        self.context = context
        annotations = IAnnotations(context)
        if KEY not in annotations.keys():
            # You know what happens if we don't use persistent classes here?
            annotations[KEY] = PersistentDict({
                "voted": PersistentList(),
                'votes': PersistentDict()
                })
        self.annotations = annotations[KEY]

    def _hash(self, request):
        """
        This hash can be tricked out by changing IP Adresses and might allow
        only a single person of a big company to vote
        """
        hash = md5()
        hash.update(safe_bytes(request.getClientAddr()))
        for key in ["User-Agent", "Accept-Language",
                    "Accept-Encoding"]:
            val = safe_bytes(request.getHeader(key))
            if val:
                hash.update(val)
        return hash.hexdigest()

    def vote(self, vote, request):
        vote = int(vote)
        if self.already_voted(request):
            # Exceptions can create ugly error messages. If you or your user
            # can't resolve the error, you should not catch it.
            # Transactions can throw errors too.
            # What happens if you catch them?
            raise KeyError("You may not vote twice")
        self.annotations['voted'].append(self._hash(request))
        votes = self.annotations['votes']
        if vote not in votes:
            votes[vote] = 1
        else:
            votes[vote] += 1

    def average_vote(self):
        total_votes = sum(self.annotations['votes'].values())
        if total_votes == 0:
            return 0
        total_points = sum([vote * count for (vote, count) in
                            self.annotations['votes'].items()])
        return float(total_points) / total_votes

    def has_votes(self):
        return len(self.annotations.get('votes', [])) != 0

    def already_voted(self, request):
        return self._hash(request) in self.annotations['voted']

    def clear(self):
        annotations = IAnnotations(self.context)
        annotations[KEY] = PersistentDict({'voted': PersistentList(),
                                           'votes': PersistentDict()})
        self.annotations = annotations[KEY]
