import os
import io

from setuptools import setup


cwd = os.path.abspath(os.path.dirname('__file__'))

with io.open(os.path.join(cwd, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='jolokia',
    version='0.0.1',
    description='A Python Jolokia client',
    long_description=long_description,
    url='https://github.com/wbrefvem/python-jolokia',
    author='Will Refvem',
    author_email='wrefvem@redhat.com',
    license='Apache 2.0',

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='jolokia http jmx',
    install_requires=['requests']
)
