from fastapi import FastAPI

LoginService = FastAPI()

@LoginService.get("/test")
def test():
    return{"message": "Testing project"}

