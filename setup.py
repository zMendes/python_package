from setuptools import setup

setup(
    name="dev_aberto_caio_gustavo_leonardo",
    version="0.1",
    packages=["dev_aberto"],
    author=["caio", "gustavo", "leonardo"],
    install_requires=["requests"],
    scripts=["scripts/hello.py"],
    python_requires=">=3.8.0",
)
