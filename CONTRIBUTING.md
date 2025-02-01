# This document explain how a developer can start and contribute to this project

## Clone the project
`git clone https://github.com/Happy-Kumar-Sharma/ml-project.git`

## move into the project folder
`cd ml-project`

## Install the virtualenv
`pip install virtualenv`

## Enter into virtual env
`python -m venv .venv`

## Activate the virtual env
` source .venv/Scripts/activate`

## Install packages from requirements.txt file
`pip install -r requirements.txt`

## Install pre-commit -- not to follow [Optional]
First, install the pre-commit package by running
`pip install pre-commit`

## Install the pre-commit hooks
`pre-commit install`

## Delete precommit hooks [Not required]
`pre-commit clean`

## Auto update precommit [Not required]
`pre-commit autoupdate`

## Check standard guidline of this project [Optional]
`pre-commit run --all-files`
