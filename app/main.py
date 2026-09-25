from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session


from app.database import Base,engine,SessionLocal
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskResponse

Base.metadata.create_all(bind=engine)

app =FastAPI(
    title="My FastAPI Application",
    version="1.0.0"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {
        "message": "Welcome to my FastAPI application!"
    }

@app.post("/tasks")
def create_task(task: TaskCreate, db:Session = Depends(get_db)):
    new_task = Task(title=task.title, description=task.description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return new_task


@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()

    return tasks

# app.listen(8003);