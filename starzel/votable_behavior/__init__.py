from zope.i18nmessageid import MessageFactory

# Set up the i18n message factory for our package
MessageFactory = MessageFactory('starzel.votable_behavior')

# permissions
ViewVote = 'starzel.votable_behavior: View Vote'
DoVote = 'starzel.votable_behavior: Do Vote'
