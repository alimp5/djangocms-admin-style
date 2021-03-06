#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import sys

def noop_gettext(s):
    return s

gettext = noop_gettext

HELPER_SETTINGS = dict(
    LANGUAGES=(
        ('en', u'English'),
        ('de', u'Deutsch'),
        ('it', u'Italiano'),
        ('zh-cn', u'Chinese (Simplified)'),
    ),
    USE_TZ=True,
    TIME_ZONE='Europe/Zurich',
    LANGUAGE_CODE='en',
    PARLER_LANGUAGES={
        1: (
            {'code': 'en', 'fallbacks': ['de',]},
            {'code': 'de', 'fallbacks': ['en',]},
            {'code': 'it', 'fallbacks': ['en',]},
            {'code': 'zh-cn', 'fallbacks': ['en',]},
        ),
        'default': {
            'fallback': 'en',
            'hide_untranslated': False,
        },
    },
    PARLER_ENABLE_CACHING=False,
    CMS_CACHE_DURATIONS={
        'menus': 0,
        'content': 0,
        'permissions': 0,
    },
    CMS_ENABLE_UPDATE_CHECK=False,
    # required for integration tests
    LOGIN_URL='/admin/login/?user-login=test',
    CMS_LANGUAGES={
        1: [
            {
                'code': 'en',
                'name': gettext('English'),
                'fallbacks': ['de',],
            },
            {
                'code': 'de',
                'name': gettext('German'),
                'fallbacks': ['en',],
            },
            {
                'code': 'it',
                'name': gettext('Italian'),
                'fallbacks': ['en',],
            },
            {
                'code': 'zh-cn',
                'name': gettext('Chinese Simplified'),
                'fallbacks': ['en',]
            },
        ],
        'default': {
            'fallbacks': ['en', 'de',],
            'redirect_on_fallback': False,
            'public': True,
            'hide_untranslated': False,
        }
    },
    INSTALLED_APPS=[
        'djangocms_text_ckeditor',
        'reversion',
        'djangocms_grid',

        # aldryn_jobs
        # 'absolute',
        # 'aldryn_common',
        # 'aldryn_boilerplates',
        # 'aldryn_apphooks_config',
        # 'aldryn_reversion',
        # 'aldryn_categories',
        # 'aldryn_jobs',
        # 'aldryn_translation_tools',
        # 'adminsortable2',
        # 'bootstrap3',
        # 'emailit',
        # 'parler',
        # 'sortedm2m',
        # 'standard_form',
    ],
    MIDDLEWARE_CLASSES=[
        'cms.middleware.utils.ApphookReloadMiddleware',
    ],
    TEMPLATE_DIRS=(
        os.path.join(
            os.path.dirname(__file__),
            'integration'
        ),
    ),
    CMS_TEMPLATES=(
        ('fullwidth.html', 'Fullwidth'),
        ('page.html', 'Standard page'),
        ('simple.html', 'Simple page'),
    ),
)


def run():
    from djangocms_helper import runner

    os.environ.setdefault('DATABASE_URL', 'sqlite://localhost/testdb.sqlite')

    # we use '.runner()', not '.cms()' nor '.run()' because it does not
    # add 'test' argument implicitly
    runner.runner([sys.argv[0], 'cms', '--cms', 'server', '--bind', '0.0.0.0'])

if __name__ == "__main__":
    run()
