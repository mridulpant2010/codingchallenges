from setuptools import setup,find_packages

setup(
    name="wordcount",
    version="0.1.1",
    author="Mridul Pant",
    author_email="mridulpant2010@gmail.com",
    packages=find_packages(include=['codingchallenges','codingchallenges.*']),
    install_requires=['pandas','tester'],
    setup_requires=['flake8'],
    tests_require = ['pytest']
)

#how to use the entry point

