from pydantic import BaseModel, Field


class UserCreate(BaseModel):
  username: str = Field(min_length=3, max_length=50)
  full_name: str = Field(min_length=2, max_length=100)
  password: str =   Field(min_length=8)
  role: str = "user"

class UserInDB(BaseModel):
  id: int
  username: str
  full_name: str
  hashed_password: str
  role: str
  is_active: bool

class UserResponse(BaseModel):
    id: int
    username: str
    full_name: str
    role: str
    is_active: bool