from fastapi import FastAPI
from .schemas import UserLogin UserSignUp

LoginService = FastAPI()
users: list[UserSignUp] = []

@LoginService.post("/api/signup", status_code=status.HTTP_201_CREATED)
def signup(user: UserSignUp)
    if any(u.email == user.email for u in users):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="email already exists")
    users.append(user)
    return user

@LoginService.post("/api/login", status_code=status.HTTP_201_CREATED)
def login(user: UserLogin)
    for u in users:
        if u.username == username:
            return u
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user name not found")


