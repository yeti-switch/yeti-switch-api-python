from setuptools import setup
from yeti_switch_api import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="yeti_switch_api",
    version=__version__,
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
    packages=["yeti_switch_api"],
    python_requires=">=3.7",
    install_requires=["jsonapi_requests", "requests"],
    keywords=["yeti-switch", "yeti-web"],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
