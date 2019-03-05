from setuptools import setup, find_packages


with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setup(
    name="dj-cref",
    version="0.0.5",
    description="The django generic view output unit",
    license="MIT",
    author="Kazuma Murata",
    author_email="mrt014kzm@gmail.com",
    packages=find_packages(exclude=['venv/', 'Makefile']),
    install_requires=install_requirements,
    keywords="django,generic,output",
    url="https://github.com/Canon11/dj-cref",
    entry_points={
        "console_scripts": [
            "dj-cref=command.main:main",
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ]
)
