# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='django-feedback-api',
    version='0.0.1',
    author='Konstantin Kruglov',
    author_email='kruglovk@gmail.com',
    description='RestAPI',
    url='https://github.com/k0st1an/django-feedback-api',
    packages=find_packages(exclude=['dj_feedback_api']),
    license='Apache License Version 2.0',
    install_requires=[
        'Django==1.10.3',
        'djangorestframework==3.5.3'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: POSIX :: Linux',
        'Framework :: Django',
        'Framework :: Django :: 1.10'
    ],
)
