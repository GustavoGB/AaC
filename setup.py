from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    readme_description = fh.read()

runtime_dependencies = [
    "attrs >= 21.2",
    "coverage >= 6.0",
    "jsonschema >= 4.0",
    "pyrsistent >= 0.18",
    "PyYAML >= 5.4",
    "six >= 1.16",
    "click >= 8.0",
    "pathspec >= 0.9",
    "platformdirs >= 2.4",
    "regex >= 2021.9",
    "typing-extensions >= 3.10",
    "pluggy >= 1.0",
    "iteration_utilities >= 0.11",
    "Jinja2 >= 3.0",
    "MarkupSafe >= 2.0",
]

development_dependencies = [
    "wheel == 0.37.0",
    "black == 21.9b0",
    "mccabe == 0.6.1",
    "mypy-extensions == 0.4.3",
    "pycodestyle >= 2.8.0",
    "pyflakes >= 2.4",
    "build == 0.7.0",
    "twine == 3.4.2",
    "Sphinx == 4.2.0",
    "sphinxcontrib-applehelp == 1.0.2",
    "sphinxcontrib-devhelp == 1.0.2",
    "sphinxcontrib-htmlhelp == 2.0.0",
    "sphinxcontrib-jsmath == 1.0.1",
    "sphinxcontrib-qthelp == 1.0.3",
    "sphinxcontrib-serializinghtml == 1.1.5",
    "furo == 2021.10.9",
    "pipdeptree >= 2.2.0",
    "Pygments >= 2.5.1",
]

test_dependencies = [
    "tox >= 3.24",
    "nose2 >= 0.10.0",
    "coverage >= 6.0",
    "flake8 >= 3.9",
    "flake8-docstrings >= 1.6.0",
    "flake8-fixme >= 1.1.1",
    "flake8-eradicate >= 1.2.0",
    "flake8-assertive >= 1.3.0",
    "eradicate<3.0,>=2.0",
]

setup(
    name="aac",
    version="0.0.4",
    description=(
        "A distinctly different take on Model-Based System Engineering (MBSE) that allows a system modeller to define a system in simple yaml. "
    ),
    license="",
    long_description=readme_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="src", exclude="tests"),
    package_dir={"": "src"},
    package_data={'aac.spec': ['spec.yaml'], '': ['*.jinja2']},
    install_requires=runtime_dependencies,
    setup_requires=development_dependencies,
    tests_require=test_dependencies,
    entry_points={
        "console_scripts": [
            "aac=aac.cli:run_cli",
        ]
    },
    extras_require={
        "test": test_dependencies,
        "dev": development_dependencies,
        "all": test_dependencies + development_dependencies,
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
    ],
    keywords=["MBSE"],
)
