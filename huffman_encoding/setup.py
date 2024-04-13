from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="compression",
    version="0.1.0",
    author="Mridul Pant",
    author_email="mridulpant2010@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mridulpant2010/codingchallenges/tree/main/wc",
    project_urls={
        "Bug Tracker": "https://github.com/mridulpant2010/codingchallenges/tree/main/wc", #TODO: correct this link.
    },
    packages=find_packages(include=["url_shortening", "url_shortening.*"]),
    install_requires=["flask"],
    setup_requires=["flake8"],
    tests_require=["pytest"],
    python_requires=">=3.6",
)