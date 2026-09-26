from sqlalchemy.orm import Session

from app.models.task import Task


def get_all_tasks(db: Session):
    return db.query(Task).all()

def create_task(db: Session, task: Task):
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


