import os
from setuptools import setup, find_packages


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as file_handle:
        return file_handle.read()


setup(
    name = "simple_midi_parser",
    version = "0.1.0",
    url="https://pypi.python.org/pypi/simple_midi_parser",
    packages = find_packages(),
    author="Panos Kountanis",
    author_email="panosktn@gmail.com",
    description="Simple MIDI file parser",
    long_description=read("README.rst"),
    install_requires = [
        'six>=1.8.0'
    ],
    setup_requires= [
        'nose>=1.0',
        'mock'
    ]
)
