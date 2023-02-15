from setuptools import setup, find_packages
from googletrans import __version__ as VERSION

requirements = [
]

test_requirements = [
]

setup(
    name                = 'googletrans-python',
    version             = VERSION,
    description         = 'googletrans-python package.',
    long_description    = "googletrans",
    author              = "leeyunjai",
    author_email        = 'leeyunjai1982@gmail.com',
    url                 = 'https://github.com/leeyunjai/googletrans-python',
    packages            = find_packages(),
    install_requires    = requirements,
    keywords            = 'googletrans',
    classifiers         = [
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    test_suite          = 'tests',
    tests_require       = test_requirements
)
