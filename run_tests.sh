#!/bin/bash
export $(cat .env | sed -e /^$/d -e /^#/d | xargs)
pytest -s -vvvv --cov=security --cov-report term-missing
