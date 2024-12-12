from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection details
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'python',
    'port': 3306
}

# Database URL
# DATABASE_URL = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
# Using string formatting to directly access dictionary values
# Simplified connection string
# DATABASE_URL = f"mysql+pymysql://root:root@localhost:3306/python"
DATABASE_URL = ('mysql+pymysql://{user}:{password}@'
                '{host}:{port}/{database}').format(
    **DB_CONFIG)

# Create engine and session
engine = create_engine(DATABASE_URL, echo=True)  # Set echo=False to disable SQL logging
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Define the model
class Student(Base):
    __tablename__ = 'students'  # Table name in MySQL database
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', age={self.age})>"

# Create the table
Base.metadata.create_all(engine)

# Function to create a student
def create_student(name, age):
    new_student = Student(name=name, age=age)
    session.add(new_student)
    session.commit()
    print(f"Student {name} added with ID {new_student.id}")

# Function to read all students
def read_students():
    students = session.query(Student).all()
    print("All Students:")
    for student in students:
        print(student)

# Function to update a student
def update_student(student_id, new_name=None, new_age=None):
    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        print("Student not found!")
        return
    if new_name:
        student.name = new_name
    if new_age:
        student.age = new_age
    session.commit()
    print(f"Student ID {student_id} updated successfully")

# Function to delete a student
def delete_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        print("Student not found!")
        return
    session.delete(student)
    session.commit()
    print(f"Student ID {student_id} deleted successfully")

# Main program to test CRUD operations
if __name__ == "__main__":
    # CREATE
    create_student(name="Alice", age=20)
    create_student(name="Bob", age=22)
    #
    # # READ
    # read_students()
    #
    # # UPDATE
    # update_student(student_id=1, new_name="Alice Smith", new_age=21)
    #
    # # DELETE
    # delete_student(student_id=2)
    #
    # # Final Read to Verify Changes
    # read_students()

    read_students()

