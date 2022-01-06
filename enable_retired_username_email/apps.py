# -*- coding: utf-8 -*-
# pylint: disable=import-outside-toplevel
"""
enable_retired_username_email Django application initialization.
"""

from __future__ import absolute_import, unicode_literals

from django.apps import AppConfig


class EnableRetiredUsernameEmailConfig(AppConfig):
    """
    Configuration for the enable_retired_username_email Django application.
    """

    name = 'enable_retired_username_email'
    plugin_app = {}

    def ready(self):
        """
        Set up signals for app.
        """
        from enable_retired_username_email import signals  # pylint: disable=unused-import
