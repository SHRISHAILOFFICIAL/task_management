from pydantic import BaseModel,Field

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str | None = None
    priority: int = Field(default=1, ge=1, le=5)

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: str
    priority: int

    model_config = {
        "from_attributes": True
    }


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None
    priority: int | None = Field(default=None, ge=1, le=5)

model_config = {
    "from_attributes": True
}