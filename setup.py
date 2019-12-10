# encoding: utf8
from setuptools import setup, find_namespace_packages

setup(
    name='aixiaotong-python-sdk',
    version='0.1.0',
    packages=find_namespace_packages(include=['aixiaotong.*']),
    include_package_data=True,
    install_requires=[
        'requests',
    ],
    description='aixiaotong python sdk',
    keywords='aixiaotong',
    url="https://ai-xiaotong.com",
)