from pydantic import BaseModel, EmailStr, Field, NaiveDatetime
from enum import Enum

# ====================== ENUM ======================

class Gender(Enum):
    M = "M"
    F = "F"

# ====================== GOAL ======================

class GoalCreate(BaseModel):
    weight: int = Field(ge=1, description="몸무게는 1kg 이상이어야 합니다.")
    date: NaiveDatetime

class GoalResponse(BaseModel):
    weight: int
    date: NaiveDatetime

# ====================== USER ======================

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str
    gender: Gender
    height: int = Field(ge=1, description="키는 1cm 이상이어야 합니다.")
    weight: int = Field(ge=1, description="몸무게는 1kg 이상이어야 합니다.")
    age: int = Field(ge=1, description="나이는 1세 이상이어야 합니다.")
    allergies: str = None  # ✅ 알레르기 필드 추가
    goal: GoalCreate

    class Config:
        use_enum_values = True

class UserResponse(BaseModel):
    name: str
    gender: Gender
    height: int
    weight: int
    allergies: str = None
    goal: GoalResponse

    class Config:
        use_enum_values = True

# ====================== 인증 응답 ======================

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

# ====================== 음식 ======================

class FoodCreate(BaseModel):
    name: str
    unit: int
    calories_per_unit: int
    protein_per_unit: int
    carbs_per_unit: int
    fat_per_unit: int
    allergens: str = None

# ====================== 재고 ======================

class InventoryBase(BaseModel):
    food_id: int
    quantity: int

# ====================== 식사 기록 ======================

class MealCreate(BaseModel):
    food_id: int
    quantity: int
