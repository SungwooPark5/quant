from fastapi import APIRouter

router = APIRouter(tags=["ticker"])


@router.get("/ticker/test")
async def test():
    return {"message": "test"}
