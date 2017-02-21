#!/usr/bin/env python

from setuptools import setup, find_packages


version = '0.0.1'

setup(name='ooi-data',
      version=version,
      description='OOI Data Model',
      url='https://github.com/oceanobservatories/ooi-data',
      license='BSD',
      author='Ocean Observatories Initiative',
      author_email='contactooici@oceanobservatories.org',
      keywords=['ooici'],
      packages=find_packages(),
      package_data={},
      dependency_links=[
      ],
      entry_points={},
      )
