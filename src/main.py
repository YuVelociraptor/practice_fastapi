from fastapi import FastAPI

fast_api = FastAPI()

@fast_api.get("/")
def root_path():
    return "test"