from pydantic import BaseModel, ConfigDict
from typing import Union
from datetime import datetime

class Enrollment(BaseModel):
    id: int
    student_id: int
    course_id: int
    student: Union["Student", None] = None
    course: Union["Course", None] = None

class Manager(BaseModel):
    id: int
    name: str
    email: str

class Teacher(BaseModel):
    id: int
    name: str
    courses: "Course"

class Student(BaseModel):
    id: int
    name: str
    email: str
    courses: Union["Course", Enrollment]
    attendances: "Attendance"

class Course(BaseModel):
    id: int
    name: str
    teacher_id: int
    time_slot: str
    capacity: int
    students: Union["Student", Enrollment]
    teacher: "Teacher"

class Attendance(BaseModel):
    id: int
    student_id: int
    course_id: int
    date: datetime
    status: str
    student: "Student"
    course: "Course"

# Enable forward references
Course.model_rebuild()
Student.model_rebuild()
Teacher.model_rebuild()
Enrollment.model_rebuild()
Attendance.model_rebuild()
