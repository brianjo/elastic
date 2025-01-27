#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.


import sys

from setuptools import find_packages, setup


def get_version():
    return "0.2.3.dev0"


if __name__ == "__main__":
    if sys.version_info < (3, 8):
        sys.exit("python >= 3.8 required for torchelastic")

    with open("README.md", encoding="utf8") as f:
        readme = f.read()

    with open("requirements.txt") as f:
        reqs = f.read()

    version = get_version()
    print("-- Building version: " + version)

    setup(
        # Metadata
        name="torchelastic",
        version=version,
        author="PyTorch Elastic Devs",
        author_email="torchelastic@fb.com",
        description="PyTorch Elastic Training",
        long_description=readme,
        long_description_content_type="text/markdown",
        url="https://github.com/pytorch/elastic",
        license="BSD-3",
        keywords=["pytorch", "machine learning", "elastic", "distributed"],
        python_requires=">=3.8",
        install_requires=reqs.strip().split("\n"),
        include_package_data=True,
        packages=find_packages(exclude=("*.test", "aws*", "*.fb")),
        test_suite="torchelastic.tsm.test.suites.unittests",
        # PyPI package information.
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: BSD License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Topic :: System :: Distributed Computing",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
        ],
    )
