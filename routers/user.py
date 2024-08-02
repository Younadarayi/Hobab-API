from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Response
from model import model, schemas
from sqlalchemy.orm import Session

from util import util


router = APIRouter(tags=["user"], prefix="/users")


@router.post("/add", status_code=status.HTTP_201_CREATED)
def create_user(
    request: schemas.UserAddRequest,
    db: Session = Depends(util.get_db),
):
    new_user = model.User(
        user_name=request.user_name,
        password=request.password,
        name=request.name,
        user_type_id=request.user_type_id,
        start_work_time=request.start_work_time,
        end_work_time=request.end_work_time,
    )
    user_exist = (
        db.query(model.User).filter(model.User.user_name == new_user.user_name).first()
    )

    if user_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="user exists")
    else:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user


@router.get("/by-type/{type_id}", response_model=List[schemas.UserResponseInfo])
def get_users_by_type(
    type_id: int,
    response: Response,
    db: Session = Depends(util.get_db),
):
    users = db.query(model.User).filter(model.User.user_type_id == type_id).all()
    if not users:
        response.status_code = status.HTTP_404_NOT_FOUND
    return users


@router.get("/all", response_model=List[schemas.UserResponseInfo])
def get_all_users(
    response: Response,
    db: Session = Depends(util.get_db),
):
    users = db.query(model.User).all()
    if not users:
        response.status_code = status.HTTP_404_NOT_FOUND
    return users


@router.get("/{user_id}", response_model=schemas.UserResponseInfo)
def get_user_by_id(
    user_id: int,
    response: Response,
    db: Session = Depends(util.get_db),
):
    user = db.query(model.User).filter(model.User.id == user_id).first()
    print(user)
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
    return user
