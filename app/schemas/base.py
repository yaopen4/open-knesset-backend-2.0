from pydantic import BaseModel


class BaseSchema(BaseModel):
    """Base schema with common configurations."""
    
    class Config:
        orm_mode = True

