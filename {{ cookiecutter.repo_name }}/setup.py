"""
{{ cookiecutter.project_short_description }}
"""
from setuptools import find_packages, setup

dependencies = ['click']

setup(
    name='{{ cookiecutter.pypi_name }}',
    version='{{ cookiecutter.version }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    license='BSD',
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    description='{{ cookiecutter.project_short_description }}',
    long_description=__doc__,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.script_name }} = {{ cookiecutter.package_name }}.cli:main',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
{%- if cookiecutter.license in ["BSD 2-Clause License", "BSD 3-Clause License"] %}
        'License :: OSI Approved :: BSD License',
{%- elif cookiecutter.license == "MIT license" %}
        'License :: OSI Approved :: MIT License',
{%- elif cookiecutter.license == "ISC license" %}
        'License :: OSI Approved :: ISC License (ISCL)',
{%- elif cookiecutter.license == "Apache Software License 2.0" %}
        'License :: OSI Approved :: Apache Software License',
{%- endif %}
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    project_urls={
            'Changelog': 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/blob/master/CHANGELOG.rst',
            'Issue Tracker': 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues',
        }
)
