import re

from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

with open('xkit/__init__.py') as f:
    version = re.findall(r"__version__ = '(.+)'", f.read())[0]

setup(
    name='xkit',
    version=version,
    install_requires=[
        'httpx[socks]',
        'filetype',
        'beautifulsoup4',
        'pyotp',
        'lxml'
    ],
    python_requires='>=3.8',
    description='Twitter API wrapper for python with **no API key required**.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/robinmonsere/xkit',
    package_data={'xkit': ['py.typed']}
)
