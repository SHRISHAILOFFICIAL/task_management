from sqlalchemy.orm import Session

from app.models.task import Task


def get_all_tasks(db: Session):
    return db.query(Task).all()

def create_task(db: Session, task: Task):
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_task_by_id(db: Session, task_id: int):

    return db.query(Task).filter(Task.id == task_id).first()

def update_task(db: Session, task: Task):

    db.commit()
    db.refresh(task)

    return task

def delete_task(db: Session, task: Task):

    db.delete(task)
    db.commit()
