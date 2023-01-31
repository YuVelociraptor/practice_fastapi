# practice_fastapi

## Development
### Run on Local Docker
- Port number is `39993`
    - http://localhost:39993
```
docker compose up -d
```

### Run on Local Python and Poetry
- Port number is `8000`
    - http://localhost:8000
```
poetry install
poetry run uvicorn main:fast_api --host 0.0.0.0
```