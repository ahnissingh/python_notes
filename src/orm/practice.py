from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "python",
    "port": 3306
}
DB_URL = "mysql+pymysql://{user}:{password}@{host}:{port}/{database}".format(**DB_CONFIG)

# Create engine and session
engine = create_engine(DB_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Student (id={self.id} , name ={self.name} , age = {self.age}>"


Base.metadata.create_all(engine)


def create_student(name, age):
    new_student = Student(name=name, age=age)
    session.add(new_student)
    session.commit()
    print(f"Student {name} added with ID {new_student.id}")


def read_students():
    students = session.query(Student).all()
    print("All Students")
    for student in students:
        print(student)


def update_student(student_id, new_name=None, new_age=None):
    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        print("Student not found")
        return
    if new_name:
        student.name = new_name
    if new_age:
        student.age = new_age
    session.commit()
    print(f"Student ID {student_id} updated successfully")


def delete_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        print("No student")
        return
    session.delete(student)
    session.commit()
    print("Student deleted")
