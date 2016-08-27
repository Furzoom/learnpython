try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'PROJECT_NAME',
    'author': 'furzoom',
    'url': 'URL to get it at,',
    'download_url': 'Where to download it.',
    'author_email': 'furzoommn at gmail.com',
    'version': '0.1',
    'install_requires': ['NAME'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
