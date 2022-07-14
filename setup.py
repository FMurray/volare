from os import path
import re
from setuptools import setup, find_packages

name = "volare"
here = path.abspath(path.dirname(__file__))

# get package version
with open(path.join(here, name, "__init__.py"), encoding="utf-8") as f:
    result = re.search(r'__version__ = ["\']([^"\']+)', f.read())

    if not result:
        raise ValueError("Can't find the version in kedro/__init__.py")

    version = result.group(1)

# get the dependencies and installs
with open("requirements.txt", encoding="utf-8") as f:
    requires = [x.strip() for x in f if x.strip()]

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    readme = f.read()

setup(
    name=name,
    version=version,
    description="Framework for serverless data pipelines",
    license="MIT",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="",    # TODO add github
    python_requires=">=3.7, <3.11",
    packages=find_packages(exclude=["docs*", "tools*", "libs*"]),
    include_package_data=True,
    install_requires=requires,
    author="Volo",
    entry_points={"console_scripts": ["kedro = kedro.framework.cli:main"]}
)