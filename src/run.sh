#!/bin/bash
poetry config virtualenvs.create false
poetry run uvicorn main:fast_api --host 0.0.0.0