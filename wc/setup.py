from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="ccwc",
    version="0.1.5.2",
    author="Mridul Pant",
    author_email="mridulpant2010@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mridulpant/wordcount",
    project_urls={
        "Bug Tracker": "https://github.com/mridulpant/wordcount/issues",
    },
    packages=find_packages(include=["wc", "wc.*"]),
    install_requires=["typer"],
    setup_requires=["flake8"],
    tests_require=["pytest"],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "ccwc=codingchallenges.wc.src.main:main",
        ],
    },
)

