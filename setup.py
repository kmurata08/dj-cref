from setuptools import setup, find_packages


with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

try:
    with open('README.md') as f:
        readme = f.read()
except IOError:
    readme = ''

setup(
    name="dj-cref",
    version="0.0.6",
    description="The django generic view output unit",
    license="MIT",
    author="Kazuma Murata",
    author_email="mrt014kzm@gmail.com",
    packages=find_packages(exclude=['venv/', 'Makefile']),
    install_requires=install_requirements,
    long_description=readme,
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
