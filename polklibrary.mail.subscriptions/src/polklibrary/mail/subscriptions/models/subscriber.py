from plone import api
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema
from zope.interface import directlyProvides
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

class ISubscriber(model.Schema):

    title = schema.TextLine(
            title=u"Title",
            required=True,
        )
        
    body = RichText(
            title=u"Subscription Welcome Page",
            default_mime_type='text/structured',
            required=False,
            default=u"",
        )
    
    subscribers = schema.Text(
            title=u"Subscribers",
            description=u"One email per line.",
            required=False,
            default=u"",
        )
        
    notes = schema.Text(
            title=u"Internal Notes",
            required=False,
            default=u"",
        )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        