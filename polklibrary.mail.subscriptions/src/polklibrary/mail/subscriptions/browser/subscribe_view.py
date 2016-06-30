from plone import api
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

import re

class SubscribeView(BrowserView):

    template = ViewPageTemplateFile("subscribe_view.pt")
    
    email = ''
    subscribed = False
    unsubscribed = False
    
    def __call__(self):
        self.email = ''
        self.subscribed = False
        self.unsubscribed = False
    
    
    
        if 'form.subscriber.submit' in self.request.form:
            email = self.request.form.get('form.subscriber.email','').strip()
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

            if match != None:
                
                if self.context.subscribers:
                    self.context.subscribers += email + '\n'
                else:
                    self.context.subscribers = email + '\n'
                    
                self.subscribed = True
                self.email = email
                
                

        if 'form.subscriber.cancel' in self.request.form:
            email = self.request.form.get('form.subscriber.email','').strip()
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

            if match != None:
                target = email + '\n'
                self.context.subscribers = self.context.subscribers.replace(target, '')
                self.unsubscribed = True
                self.email = email
    
        return self.template()

        
    @property
    def portal(self):
        return api.portal.get()
        