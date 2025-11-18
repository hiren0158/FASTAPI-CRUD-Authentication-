from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    password: str

class UserLogin(BaseModel):
    name: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class ProductBase(BaseModel):
    name: str
    price: float

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    
    class Config:
        
        from_attributes = True