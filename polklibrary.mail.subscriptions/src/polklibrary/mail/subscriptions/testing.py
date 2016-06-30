# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import polklibrary.mail.subscriptions


class PolklibraryMailSubscriptionsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=polklibrary.mail.subscriptions)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'polklibrary.mail.subscriptions:default')


POLKLIBRARY_MAIL_SUBSCRIPTIONS_FIXTURE = PolklibraryMailSubscriptionsLayer()


POLKLIBRARY_MAIL_SUBSCRIPTIONS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(POLKLIBRARY_MAIL_SUBSCRIPTIONS_FIXTURE,),
    name='PolklibraryMailSubscriptionsLayer:IntegrationTesting'
)


POLKLIBRARY_MAIL_SUBSCRIPTIONS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(POLKLIBRARY_MAIL_SUBSCRIPTIONS_FIXTURE,),
    name='PolklibraryMailSubscriptionsLayer:FunctionalTesting'
)


POLKLIBRARY_MAIL_SUBSCRIPTIONS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        POLKLIBRARY_MAIL_SUBSCRIPTIONS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PolklibraryMailSubscriptionsLayer:AcceptanceTesting'
)
