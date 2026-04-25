from fastapi import Request, Response
from starlette_admin.auth import AuthProvider

class MyAuthProvider(AuthProvider):
    async def login(self, username: str, password: str, remember_me: bool, request: Request, response: Response) -> Response:
        if username == "admin" and password == "admin":
            request.session.update({"username": username})
            return response
        raise Exception("Invalid credentials")

    async def is_authenticated(self, request: Request) -> bool:
        return request.session.get("username") == "admin"

    async def logout(self, request: Request, response: Response) -> Response:
        request.session.clear()
        return response