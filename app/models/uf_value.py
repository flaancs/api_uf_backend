from pydantic import BaseModel, Field

class UFValueResponse(BaseModel):
    uf_value: str = Field(..., example="28500.52")
