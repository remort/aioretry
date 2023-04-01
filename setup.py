from setuptools import setup


setup(
    name='aioretry-decorator',
    version='1.0.0',
    description='Handy decorator to set retry policies for async callables with some handy features',

    url='https://github.com/remort/aioretry',
    author='Vadim Bazhov',
    author_email='master@remort.net',

    py_modules=['aioretry_decorator'],
)
