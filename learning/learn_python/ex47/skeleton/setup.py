try:
    from setuptools import setup
except ImportError:
    from distutils.core import setuptools

config = {
    'description': 'My Project',
    'author': 'Samuel',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'faithfulmaster@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['nose'],
    'scripts': [],
    'name': 'Beginner'
}

setup(**config)
