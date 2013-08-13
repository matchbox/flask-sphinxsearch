"""
Flask-SphinxSearch
-------------

Flask extension to work with the Sphinx search engine
(http://sphinxsearch.com/)
"""
from setuptools import setup


setup(
    name='Flask-SphinxSearch',
    version='0.1',
    url='https://github.com/matchbox/flask-sphinxsearch/',
    license='Apache',
    author='Paul Swartz',
    author_email='pswartz@matchbox.net',
    description='Flask extension to work with the Sphinx search engine',
    long_description=__doc__,
    py_modules=['flask_sphinxsearch'],
    zip_safe=True,
    include_package_data=False,
    platforms='any',
    install_requires=[
        'Flask',
        'sphinxsearch'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
