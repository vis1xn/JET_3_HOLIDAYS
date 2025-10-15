from fastapi import FastAPI
from .schemas import UserLogin, UserSignUp

LoginService = FastAPI()
users: list[UserSignUp] = []

@LoginService.post("/api/signup", status_code=status.HTTP_201_CREATED)
def signup(user: UserSignUp):
    if any(u.email == user.email for u in users):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="email already exists")
    users.append(user)
    return user

@LoginService.post("/api/login", status_code=status.HTTP_201_CREATED)
def login(user: UserLogin):
    for u in users:
        if u.username == username:
            return u
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="username not found")

@LoginService.delete("/api/users/{username}", status_code=status.HTTP_200_OK)
def delete_user(username: str):
    for u in users:
        if u.username == username:
            users.remove(u)
            return {"message": f"User '{username}' deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@LoginService.put("/api/users/{username}", status_code=status.HTTP_200_OK)
def update_user(username: str, updated_user: User):
    for index, u in enumerate(users):
        if u.username == username:
            users[index] = updated_user
            return {"message": f"User '{username}' updated successfully", "user": updated_user}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
