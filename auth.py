import os
from fastapi import Request, Response
from starlette_admin.auth import AuthProvider
from starlette.exceptions import HTTPException
from starlette import status
from config import ADMIN_USERNAME, ADMIN_PASSWORD

class MyAuthProvider(AuthProvider):
    async def login(self, username: str, password: str, remember_me: bool, request: Request, response: Response) -> Response:
        env_user = ADMIN_USERNAME
        env_pass = ADMIN_PASSWORD

        if username == env_user and password == env_pass:
            request.session.update({"username": username})
            return response

        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    async def is_authenticated(self, request: Request) -> bool:
        env_user = os.getenv("ADMIN_USERNAME")
        return request.session.get("username") == env_user

    async def logout(self, request: Request, response: Response) -> Response:
        request.session.clear()
        return response