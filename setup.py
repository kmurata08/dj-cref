from setuptools import setup, find_packages


with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setup(
    name="dj-clef",
    version="0.0.1",
    description="The django generic view output unit",
    author="Canon11",
    packages=find_packages(),
    install_requires=install_requirements,
    entry_points={
        "console_scripts": [
            "dj-clef=command.main:main",
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ]
)
