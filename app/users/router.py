from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Користувачи"]
)

@router.post("/register")
async def register_user():
    pass