enable_retired_username_email
=============================
.. image:: https://circleci.com/gh/open-craft/enable-retired-username-email.svg?style=svg
    :target: https://circleci.com/gh/open-craft/enable-retired-username-email

Custom Django app to enable reuse of username and email after retirement on Open edX.

Overview
--------

This app enables reuse of username and email after user retirement on Open edX Platfrom

Currently, once a user is retired, their email and username is not allowed to be reused for registration for new user.
However, there are some use-cases where it is useful to allow this reuse, such as, if the user management is handled by an external system, which manages the user in LMS through API calls.

Further the retired username is changed from a hash value to a friendly name of the form ``deleted_user_3``.
This is done so as the new format looks far friendlier than the orginal hashed username in places like the discussion forum.

Installation
------------

1. Login to LMS Shell
2. Checkout this repository
3. ``cd enable-retired-username-email``
4. ``pip install -e .``
5. This app could also be installed using `ansible-configurations <https://github.com/openedx/configuration/blob/f676c356a5424a52ebff01da7a8a7d96189f2579/playbooks/roles/edxapp/defaults/main.yml#L542>`_

No other configuration needed to run the app
All actions in this app is triggered by the ``post_save`` signal from ``UserRetirementStatus`` table
Drive the retirement workflow either from external services through `user APIs <https://github.com/openedx/edx-platform/blob/master/openedx/core/djangoapps/user_api/urls.py>`_ , or through the `retirement cron job <https://github.com/openedx/configuration/blob/f676c356a5424a52ebff01da7a8a7d96189f2579/playbooks/roles/user_retirement_pipeline/tasks/main.yml#L72>`_, this app should just do its job out of the box.

License
-------

The code in this repository is licensed under the AGPL 3.0 unless
otherwise noted.

Please see ``LICENSE.txt`` for details.

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email contact@opencraft.com
