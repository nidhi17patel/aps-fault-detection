from setuptools import find_packages,setup


def get_requirements():
    pass

setup(
    name="sensor",
    version="0.0.2",
    author="nidhi17patel",
    author_email="nidhi17patel@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),
)