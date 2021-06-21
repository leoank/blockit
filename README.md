# blockit

Create blocks from mempool

## Getting started

### Requirements

- Python >=3.8

### Create a python virtual env

Using venv

```bash
python -m venv venv     # create python environment
source ./venv/bin/activate    # activate python enviroment
```

Using conda

```bash
conda create -n blockit python=3.8    # create python environment
conda activate blockit    # activate python enviroment
```

### Install poetry

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Install dependencies and project root

```bash
poetry install
```

> Note: It might happen that project root does not get installed when you first execute the command above. If it is so, then just re-execute the above the command.

### CLI usage
