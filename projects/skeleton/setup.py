try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Me ',
    'url': 'location is here',
    'download_url': 'find me here',
    'author_email': 'My Email',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname',
    'description': 'My Project',
    'description': 'My Project'
}

setup(**config)
