from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate
from app.repositories.task import create_task as create_task_repository, update_task as update_task_repository,delete_task as delete_task_repository
from fastapi import HTTPException

from app.schemas.task import TaskCreate, TaskUpdate

from app.repositories.task import (
    create_task as create_task_repository,
    get_all_tasks as get_all_tasks_repository
)

from app.repositories.task import (
    create_task as create_task_repository,
    get_all_tasks as get_all_tasks_repository,
    get_task_by_id as get_task_by_id_repository
)

def create_task(db: Session, task_data: TaskCreate):

    new_task = Task(
        title=task_data.title,
        description=task_data.description
    )

    return create_task_repository(db, new_task)

def get_all_tasks(db: Session):

    return get_all_tasks_repository(db)

def get_task_by_id(db: Session, task_id: int):

    task = get_task_by_id_repository(db, task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task

def update_task(
    db: Session,
    task_id: int,
    task_data: TaskUpdate
):

    task = get_task_by_id_repository(db, task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    update_data = task_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(task, field, value)

    return update_task_repository(db, task)

def delete_task(db: Session, task_id: int):

    task = get_task_by_id_repository(db, task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    delete_task_repository(db, task)

    return {
        "message": "Task deleted successfully"
    }