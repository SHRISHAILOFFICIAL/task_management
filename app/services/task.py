from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate
from app.repositories.task import create_task as create_task_repository

from app.repositories.task import (
    create_task as create_task_repository,
    get_all_tasks as get_all_tasks_repository
)

def create_task(db: Session, task_data: TaskCreate):

    new_task = Task(
        title=task_data.title,
        description=task_data.description
    )

    return create_task_repository(db, new_task)

def get_all_tasks(db: Session):

    return get_all_tasks_repository(db)