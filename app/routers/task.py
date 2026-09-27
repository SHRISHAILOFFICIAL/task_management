
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.task import TaskCreate,TaskUpdate, TaskResponse
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

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db)
):

    return task_service.get_task_by_id(db, task_id)

@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db)
):

    return task_service.update_task(
        db,
        task_id,
        task_data
    )

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):

    return task_service.delete_task(db, task_id)
