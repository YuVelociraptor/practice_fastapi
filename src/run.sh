#!/bin/bash
poetry config virtualenvs.create false
poetry run uvicorn main:app --host 0.0.0.0