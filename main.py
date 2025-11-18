from fastapi import FastAPI
from app.routes import auth, products
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product CRUD API")

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(products.router, prefix="/products", tags=["Products"])

@app.get("/")
def root():
    return {"message": "Product CRUD API"}