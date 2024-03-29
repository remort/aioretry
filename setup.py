from pathlib import Path

from setuptools import setup

long_description = (Path(__file__).parent / "README.md").read_text()

setup(
    name='aioretry-decorator',
    version='1.0.5',
    description='Handy decorator to set retry policies for async callables with some useful features',

    url='https://github.com/remort/aioretry',
    author='Vadim Bazhov',
    author_email='master@remort.net',

    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    packages=['aioretry_decorator'],
    package_data={
        'aioretry_decorator': ['py.typed'],
    },
)
