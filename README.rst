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

**Development**

1. Login to LMS Shell
2. Checkout this repository
3. ``cd enable-retired-username-email``
4. ``pip install -e .``

**Production**

For native installation of the Open edX platform based on the `ansible-configurations <https://github.com/openedx/configuration/blob/f676c356a5424a52ebff01da7a8a7d96189f2579/playbooks/roles/edxapp/defaults/main.yml#L542>`_ 
you can use `EDXAPP_PRIVATE_REQUIREMENTS <https://github.com/openedx/configuration/blob/f676c356a5424a52ebff01da7a8a7d96189f2579/playbooks/roles/edxapp/defaults/main.yml#L542>`_ variable as shown below ::
    
    EDXAPP_PRIVATE_REQUIREMENTS:
        - name: git+https://github.com/open-craft/enable-retired-username-email.git@v1.0#egg=enable-retired-username-email
          extra_args: -e



Usage
-----

**No other configuration needed to run the app**

All actions in this app is triggered by the ``post_save`` signal from ``UserRetirementStatus`` table


Just setup the retirement states in one of two ways:

1. Using `EDXAPP_RETIREMENT_STATES <https://github.com/openedx/configuration/blob/f676c356a5424a52ebff01da7a8a7d96189f2579/playbooks/roles/edxapp/defaults/main.yml#L857>`_ ansbile variable
::
    EDXAPP_RETIREMENT_STATES:
        - PENDING
        - RETIRING_ENROLLMENTS
        - ENROLLMENTS_COMPLETE
        - RETIRING_LMS_MISC
        - LMS_MISC_COMPLETE
        - RETIRING_LMS
        - LMS_COMPLETE
        - RETIRING_FORUM
        - FORUM_COMPLETE
        - ERRORED
        - ABORTED
        - COMPLETE

2. Manually using the `populate_retirement_states <https://github.com/openedx/edx-platform/blob/master/openedx/core/djangoapps/user_api/management/commands/populate_retirement_states.py>`_ management command
    
And drive the retirement workflow either from external services through `user APIs <https://github.com/openedx/edx-platform/blob/master/openedx/core/djangoapps/user_api/urls.py>`_ , or through the `retirement cron job <https://github.com/openedx/configuration/blob/f676c356a5424a52ebff01da7a8a7d96189f2579/playbooks/roles/user_retirement_pipeline/tasks/main.yml#L72>`_, this app should just do its job out of the box.

License
-------

The code in this repository is licensed under the AGPL 3.0 unless
otherwise noted.

Please see ``LICENSE.txt`` for details.

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email contact@opencraft.com
