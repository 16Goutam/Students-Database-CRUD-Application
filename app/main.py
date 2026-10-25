import os
from fastapi import FastAPI, Depends, HTTPException, Query, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List, Optional

from app import models, schemas, crud
from app.database import engine, get_db
from app.ai_service import ask_student_assistant

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Records CRUD API",
    version="1.0.0",
    description="A FastAPI & SQLite REST API for managing student profiles."
)

# Root route serving the web UI
@app.get("/", response_class=FileResponse)
def read_root():
    html_path = os.path.join(os.path.dirname(__file__), "index.html")
    return html_path

@app.post("/students", response_model=schemas.StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    if crud.get_student_by_email(db, email=student.email):
        raise HTTPException(status_code=400, detail="A student with this email already exists.")
    return crud.create_student(db=db, student=student)

@app.get("/students", response_model=List[schemas.StudentResponse])
def read_students(
    skip: int = 0,
    limit: int = 100,
    course: Optional[str] = Query(None, description="Filter by course name"),
    db: Session = Depends(get_db)
):
    return crud.get_students(db, skip=skip, limit=limit, course=course)

@app.get("/students/{student_id}", response_model=schemas.StudentResponse)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found.")
    return db_student

@app.put("/students/{student_id}", response_model=schemas.StudentResponse)
@app.patch("/students/{student_id}", response_model=schemas.StudentResponse)
def update_student(student_id: int, student: schemas.StudentUpdate, db: Session = Depends(get_db)):
    updated_student = crud.update_student(db, student_id=student_id, student_update=student)
    if not updated_student:
        raise HTTPException(status_code=404, detail="Student not found.")
    return updated_student

@app.delete("/students/{student_id}", status_code=status.HTTP_200_OK)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_student(db, student_id=student_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found.")
    return {"message": f"Student with ID {student_id} successfully deleted."}

@app.post("/students/ai-query")
async def ai_query(payload: schemas.AIQueryRequest, db: Session = Depends(get_db)):
    records = crud.get_students(db, limit=200)
    answer = await ask_student_assistant(payload.question, records)
    return {"question": payload.question, "answer": answer}