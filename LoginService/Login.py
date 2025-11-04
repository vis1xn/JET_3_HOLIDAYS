from fastapi import FastAPI, HTTPException, status
from .schemas import UserLogin, UserSignUp, UserUpdate

LoginService = FastAPI()
users: list[UserSignUp] = []

@LoginService.post("/api/signup", status_code=status.HTTP_201_CREATED)
def signup(user: UserSignUp):
    # Check for duplicate email
    if any(u.email == user.email for u in users):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail="Email already exists"
        )
    
    # Check for duplicate username
    if any(u.username == user.username for u in users):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail="Username already exists"
        )
    
    users.append(user)
    return {"message": "User created successfully", "username": user.username}

@LoginService.post("/api/login", status_code=status.HTTP_200_OK)
def login(user: UserLogin):
    for u in users:
        if u.email == user.email and u.password == user.password:
            return {
                "message": "Login successful",
                "username": u.username,
                "name": u.name
            }
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail="Invalid email or password"
    )

@LoginService.delete("/api/users/{username}", status_code=status.HTTP_200_OK)
def delete_user(username: str):
    for u in users:
        if u.username == username:
            users.remove(u)
            return {"message": f"User '{username}' deleted successfully"}
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="User not found"
    )

@LoginService.put("/api/users/{username}", status_code=status.HTTP_200_OK)
def update_user(username: str, updated_user: UserUpdate):
    for index, u in enumerate(users):
        if u.username == username:
            # Update only the fields provided
            updated_data = u.dict()
            updated_data.update(updated_user.dict(exclude_unset=True))
            users[index] = UserSignUp(**updated_data)
            return {
                "message": f"User '{username}' updated successfully", 
                "user": users[index]
            }
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="User not found"
    )