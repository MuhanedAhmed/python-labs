from django.shortcuts import render
from django.http import HttpResponse

fetched_students = [
  {"id" : 1, "name" : "Mohaned", "age" : 27, "department" : "Electronics"},
  {"id" : 2, "name" : "Ahmed", "age" : 20, "department" : "Civil"},
  {"id" : 3, "name" : "Ali", "age" : 22, "department" : "Electrical"},
  {"id" : 4, "name" : "Hagar", "age" : 24, "department" : "Mechanics"},
  {"id" : 5, "name" : "Nayra", "age" : 25, "department" : "Computer Science"}
]
context = {
  "Students_data" : fetched_students
}

# Create your views here.
def get_all_students(req):
  return render(req, "Student/index.html", context)

def get_single_student(req, id):
  print(fetched_students[id - 1])
  context = {"Student_data" : fetched_students[id - 1]}
  return render(req, "Student/Student.html", context) 