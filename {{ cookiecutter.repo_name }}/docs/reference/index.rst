=========
Reference
=========

.. toctree:
   :glob:

   {{ cookiecutter.package_name }}*


{{ cookiecutter.package_name }}
{% for _ in cookiecutter.package_name %}={% endfor %}

.. automodule:: {{ cookiecutter.package_name }}.cli
   :members:
   :undoc-members:
   :show-inheritance:

   .. autofunction:: main
