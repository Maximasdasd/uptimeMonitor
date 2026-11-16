from fastapi import APIRouter
from uptimemonitor.services.users import UsersService
from uptimemonitor.schemas.users_schemas import UserCreate, UserResponse
from uptimemonitor.dependencies.users import get_user_service
from fastapi import Depends


from typing import Annotated

authrouter = APIRouter()


@authrouter.post("/register", response_model=UserResponse, status_code=201)
async def register(user_data: UserCreate, user_service: Annotated[UsersService, Depends(get_user_service)]) -> UserResponse:
    return await user_service.register(user_data)