{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}


{{ cookiecutter.project_short_description }}


Installation
============

Simply run:

::

    $ pip install .


Usage
=====

To use it:

::

    $ {{ cookiecutter.script_name }} --help

