
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.task import TaskCreate, TaskResponse
from app.services import task as task_service

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


# @router.get("/", response_model=list[TaskResponse])
# def get_tasks(db: Session = Depends(get_db)):
#     tasks = db.query(Task).all()

#     return tasks

@router.get("/", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):

    return task_service.get_all_tasks(db)

@router.post("/", response_model=TaskResponse,status_code=201)
def create_task(task_data:TaskCreate, db: Session = Depends(get_db)):
    return task_service.create_task(db, task_data)
    

