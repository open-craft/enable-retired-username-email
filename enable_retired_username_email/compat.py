# pylint: disable=import-outside-toplevel
"""
Proxies, and compatibility code for edx-platform features.

This module moderates access to all edx-platform features allowing for
cross-version compatibility code.

It is also simplifies running tests outside of edx-platform's environment
by stubbing these functions in unit tests.
"""


def get_retired_email_hash(email):
    """
    Compatibility function for the get_retired_email_by_email.

    Returns the hashed email if get_retired_email_by_email is imported else
    returns empty string.
    """
    try:
        from common.djangoapps.student.models import get_retired_email_by_email
        return get_retired_email_by_email(email)
    except ImportError:
        return ''


def get_user_retirement_status_model():
    """
    Get UserRetirementStatus model.
    """
    try:
        from openedx.core.djangoapps.user_api.models import UserRetirementStatus
        return UserRetirementStatus
    except ImportError:
        return object


def get_retirement_state_model():
    """
    Get RetirementState model.
    """
    try:
        from openedx.core.djangoapps.user_api.models import RetirementState
        return RetirementState
    except ImportError:
        return object
