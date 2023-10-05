# llm-passages

[![PyPI](https://img.shields.io/pypi/v/llm-passages.svg)](https://pypi.org/project/llm-passages/)
[![Changelog](https://img.shields.io/github/v/release/crossjam/llm-passages?include_prereleases&label=changelog)](https://github.com/crossjam/llm-passages/releases)
[![Tests](https://github.com/crossjam/llm-passages/workflows/Test/badge.svg)](https://github.com/crossjam/llm-passages/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/crossjam/llm-passages/blob/master/LICENSE)

Extract text from HTML to feed vector embeddings

## Installation

Install this tool using `pip`:

    pip install llm-passages

## Usage

For help, run:

    llm-passages --help

You can also use:

    python -m llm_passages --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd llm-passages
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
