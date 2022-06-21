#!/bin/bash
pip install -U pip wheel
pip wheel . -w dist
python setup.py sdist
printf "\nSuccessfully built my_minipack package"