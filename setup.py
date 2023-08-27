from setuptools import setup, find_packages
from packaging.version import Version
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().split("\n")

version_string = os.environ.get("RELEASE_VERSION", "0.0.0.dev0")
version = Version(version_string)

setup(
    name="yeti_switch_api",
    version=str(version),
    author="Denys Talakevych",
    author_email="<senid231@gmail.com>",
    url="https://github.com/senid231/yeti-admin-python",
    project_urls={
        "Bug Tracker": "https://github.com/senid231/yeti-admin-python/issues",
    },
    description="Yeti-web Admin API SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(exclude=["examples"]),
    python_requires=">=3.7",
    install_requires=requirements,
    keywords=["yeti-switch", "yeti-web"],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
