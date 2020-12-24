from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_requirements():
    with open('requirements.txt') as requirements:
        req = requirements.read().splitlines()
    return req


setup(
    name='django-usertracker',
    description='Have better control over your users',
    long_description=long_description,
    author='Nathaniel Cherian',
    author_email='me@nathanielc.com',
    url='https://github.com/nathanielCherian/django-usertracker',
    download_url='',
    license='MIT',
    packages=find_packages(exclude=('example', 'tests',)),
    install_requires=get_requirements(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Tracking',
    ],
)