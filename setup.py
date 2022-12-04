from setuptools import find_packages, setup


setup(
    name="License plate",
    version="1.0.0",
    author="Benjamin Banduhn",
    url="https://github.com/deluge/license-plate",
    packages=find_packages("src", exclude=["testing"]),
    package_dir={"": "src"},
    include_package_data=True,
    tests_require=[],
    install_requires=[],
    dependency_links=[],
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
    ],
)
