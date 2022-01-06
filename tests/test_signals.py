"""
Tests for signal receivers of custom_verification_app.
"""
from unittest.mock import MagicMock, patch

from django.contrib.auth.models import User
from django.test import TestCase

from enable_retired_username_email.signals import replace_username_email_hash


class PostRetirmentCompleteTests(TestCase):
    """
    Tests for signal receivers of custom_verification_app.
    """

    def setUp(self):
        self.original_username = "testuser"
        self.original_email = "test@example.com"

        self.retired_username = "retired_test_user"
        self.retired_email = "retired_test_email@example.com"

        self.modified_username = "deleted_user_1"
        self.modified_email = "modified_email_hash@example.com"

        self.test_user = User.objects.create(username=self.original_username, email=self.retired_email)

        super(PostRetirmentCompleteTests, self).setUp()

    def test_retired_username_modified_after_retirement_started(self):
        """
        Tests retirement username hash is replaced with an friendly string on retirement creation.
        """
        retirement_status = MagicMock()
        retirement_status.current_state.state_name = 'PENDING'
        retirement_status.original_username = self.original_username
        retirement_status.original_email = self.original_email
        retirement_status.retired_username = self.retired_username

        replace_username_email_hash(created=True, instance=retirement_status)

        self.test_user.refresh_from_db()

        self.assertEqual(retirement_status.retired_username, self.modified_username)

    @patch('enable_retired_username_email.signals.get_retired_email_hash')
    def test_email_modified_after_retirement_complete(self, get_email_hash):
        """
        Tests retirement email hash is replaced with a modified email hash on retirement completion.
        """
        self.test_user.username = self.modified_username
        self.test_user.save()

        retirement_status = MagicMock()
        retirement_status.current_state.state_name = 'COMPLETE'
        retirement_status.original_username = self.original_username
        retirement_status.original_email = self.original_email
        retirement_status.retired_username = self.modified_username

        get_email_hash.return_value = self.modified_email

        replace_username_email_hash(created=False, instance=retirement_status)

        self.test_user.refresh_from_db()

        self.assertEqual(self.test_user.email, self.modified_email)
