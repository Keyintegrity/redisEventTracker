#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='redis-event-tracker',
    version='0.0.1',
    packages=find_packages(),
    requires=['redis (>= 2.7.6)'],
    description='Track your events in redis',
    long_description=open('README.md').read(),
    author='Keyintegrity',
    author_email='info@keyintegrity.com',
    maintainer='Aleksey Pivovarov',
    maintainer_email='lexapi@gmail.com',
    url='https://github.com/Keyintegrity/redisEventTracker',
    download_url='https://github.com/Keyintegrity/redisEventTracker/archive/master.zip',
    license='MIT License',
    keywords='redis events track',
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)