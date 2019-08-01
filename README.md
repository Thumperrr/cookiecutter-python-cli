## What is this?

A default template for a new CLI project, written in Python, to be used
with the [cookiecutter](https://cookiecutter.readthedocs.io) utility. 
Deals with all the boilerplate involved in the setuptools setup, etc.


## How do I use this?

1. Install Cookiecutter:
   `$ pip install cookiecutter`.
2. Now use Cookiecutter to create your brand new project:
   `$ cookiecutter https://github.com/Thumperrr/cookiecutter-python-cli.git`


## How to answer these questions?

When running Cookiecutter, you'll need to provide some values.
Here's what they're for:

* `full_name` -- Author name
* `email` -- Author email
* `github_username` -- for automatically including project URLs
* `project_name` -- "My Tool"   (Used for marketing.  Keep it short and capitalize accordingly.)
* `repo_name` -- "python-mytool"  (Name of the GitHub repo.)
* `pypi_name` -- "mytool"   (Name on PyPI, i.e. what people type to `pip install`.)
* `script_name` -- "my-tool"  (Binary of the script, i.e. what people will run on the command line.)
* `package_name` -- "my_tool"  (Name of the Python module/package used internally.)
* `project_short_description` -- A brief description of the project included in READMEs
* `release_date` -- Project release date
* `year` -- Release year
* `version` -- Release version
* `license` -- Select a license to include in repository
* `year_from` -- copyright year from
* `year_to` -- copyright year to


## License

Liberally licensed under MIT terms.
