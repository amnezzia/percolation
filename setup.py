try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'percolation simulation',
    'author': 'Misha',
    'url': 'http://...',
    'download_url': 'http://...',
    'author_email': '',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['percolation'],
    'scripts': [],
    'name': 'percolation'
}

setup(**config)