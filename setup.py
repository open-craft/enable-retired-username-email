#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Package metadata for enable_retired_username_email.
"""
from __future__ import absolute_import, print_function

import os
import re
import sys
from typing import List

from setuptools import find_packages, setup


def get_version(*file_paths):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


def load_requirements(*requirements_paths) -> List[str]:
    """
    Load all requirements from the specified requirements files.
    """
    requirements = set()
    for path in requirements_paths:
        requirements.update(
            line.split('#')[0].strip() for line in open(path).readlines()
            if is_requirement(line.strip())
        )
    return list(requirements)


def is_requirement(line) -> bool:
    """
    Return True if the requirement line is a package requirement.

    The line is considered a package requirement if it is not blank,
    a comment, a URL, or an included file.
    """
    return line and not line.startswith(('-r', '#', '-e', 'git+', '-c'))


VERSION = get_version('enable_retired_username_email', '__init__.py')

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system(u"git tag -a %s -m 'version %s'" % (VERSION, VERSION))
    os.system("git push --tags")
    sys.exit()

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name='enable_retired_username_email_app',
    version=VERSION,
    description="""Enable retired username and email app for Open edX""",
    long_description=README,
    author='OpenCraft',
    author_email='help@opencraft.com',
    url='https://github.com/open-craft/enable-retired-username-email',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django',
    ],
    license="AGPL 3.0",
    zip_safe=False,
    keywords='Django edx',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'lms.djangoapp': [
            'enable_retired_username_email_app = enable_retired_username_email.apps:EnableRetiredUsernameEmailConfig'
        ]
    }
)
