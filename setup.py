from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="llm-passages",
    description="Extract text from HTML to feed vector embeddings",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Brian M. Dennis",
    url="https://github.com/crossjam/llm-passages",
    project_urls={
        "Issues": "https://github.com/crossjam/llm-passages/issues",
        "CI": "https://github.com/crossjam/llm-passages/actions",
        "Changelog": "https://github.com/crossjam/llm-passages/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["llm_passages"],
    entry_points="""
        [console_scripts]
        llm-passages=llm_passages.cli:cli
    """,
    install_requires=["click"],
    extras_require={
        "test": ["pytest"]
    },
    python_requires=">=3.7",
)
