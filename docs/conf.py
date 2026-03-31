import os
import sys

sys.path.insert(0, os.path.abspath('.'))

# Project info
project = 'Webapps Documents'
author = 'Paulette Frankl'
release = '1.0'

# General config
extensions = []

templates_path = ['_templates']
exclude_patterns = []

# HTML settings
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# ✅ Google Verification (WORKING METHOD)
html_context = {
    "metatags": '<meta name="google-site-verification" content="c6Qrtpo9mGReY09PT1jUg4zAyx0IN8MgDSjPUbgyRww" />'
}
