from fastapi import APIRouter, status, Header, HTTPException

# router = APIRouter(
#     prefix="/dependencies",
#     tags=["dependencies"],
#     responses={
#         status.HTTP_404_NOT_FOUND: {
#             "description": "Not found",
#         },
#     },
# )


async def get_token_header(internal_token: str = Header()):
    if internal_token != "allowed":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Internal-Token headeer invalid",
        )


# @router.get("/")
# async def get_company_name():
#     return {
#         "company_name": "Example Company, LLC",
#     }


# @router.get("/employees")
# async def number_of_employees():
#     return 162
