"""
Signal handler for setting setting modified username and email hash in user model.
"""

import time

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from enable_retired_username_email.compat import get_retired_email_hash, get_user_retirement_status_model

UserRetirementStatus = get_user_retirement_status_model()


@receiver(post_save, sender=UserRetirementStatus)
def replace_username_email_hash(
    instance: UserRetirementStatus,
    created: bool,
    **kwargs
):  # pylint: disable=unused-argument
    """
    This function is triggered when UserRetirementStatus is saved.

    Upon receiving the post_save
    signal for the UserRetirementStatus model,
    appends to the original username and email and
    calculates their hash values. These are then
    set to the User model and the corresponding
    UserRetirementStatus is deleted
    """
    if created:
        instance.retired_username = get_new_retired_username(instance.original_username)
        instance.save()

    elif instance.current_state.state_name == 'COMPLETE':
        user = User.objects.get(username=instance.retired_username)
        user.email = get_modified_email_hash(instance.original_email)
        user.save()

        instance.delete()


def get_new_retired_username(username: str) -> str:
    """
    This function returns new retirment username string.

    This function retrieves the user id from
    user model using username and returns
    a new string to be used an retirement username
    """
    user = User.objects.get(username=username)
    retired_username = f"deleted_user_{user.id}"

    return retired_username


def get_modified_email_hash(email: str) -> str:
    """
    This function generates modified email hash value.

    It appends current timestamp
    to original email
    and then calculates their hash values
    """
    current_timestamp = time.time()
    modified_email = f"{email}+{current_timestamp}"
    modified_email_hash = get_retired_email_hash(modified_email)

    return modified_email_hash
