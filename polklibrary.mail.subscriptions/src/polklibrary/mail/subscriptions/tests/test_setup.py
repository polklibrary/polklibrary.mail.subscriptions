# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from polklibrary.mail.subscriptions.testing import POLKLIBRARY_MAIL_SUBSCRIPTIONS_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that polklibrary.mail.subscriptions is properly installed."""

    layer = POLKLIBRARY_MAIL_SUBSCRIPTIONS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if polklibrary.mail.subscriptions is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('polklibrary.mail.subscriptions'))

    def test_browserlayer(self):
        """Test that IPolklibraryMailSubscriptionsLayer is registered."""
        from polklibrary.mail.subscriptions.interfaces import IPolklibraryMailSubscriptionsLayer
        from plone.browserlayer import utils
        self.assertIn(IPolklibraryMailSubscriptionsLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = POLKLIBRARY_MAIL_SUBSCRIPTIONS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['polklibrary.mail.subscriptions'])

    def test_product_uninstalled(self):
        """Test if polklibrary.mail.subscriptions is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('polklibrary.mail.subscriptions'))

    def test_browserlayer_removed(self):
        """Test that IPolklibraryMailSubscriptionsLayer is removed."""
        from polklibrary.mail.subscriptions.interfaces import IPolklibraryMailSubscriptionsLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPolklibraryMailSubscriptionsLayer, utils.registered_layers())
