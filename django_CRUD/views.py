""" 
    -*- coding: utf-8 -*-
    @Author  : Lethe
    @FileName: views.py
"""
from django.shortcuts import render,redirect

from app01.models import Student
from bson.objectid import ObjectId


def gotoIndex(request):
    return render(request, "index.html")

def gotoCreate(request):

    return render(request, "create.html")

def createData(request):
    if request.POST:
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        address = request.POST.get("address")
        data = Student(name=name,gender=int(gender),age=int(age),
                       address=address)
        data.save()
        return redirect("/retrieve/")
    return redirect("/create/")


def gotoRetrieve(request):
    data = Student.objects.all()
    return render(request, "retrieve.html", {"data":data})


def gotoUpdate(request, id):
    student = Student.objects(id=ObjectId(id))
    if request.POST:
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        address = request.POST.get("address")
        student.update(name=name, gender=int(gender), age=int(age), address=address)
        return redirect("/retrieve/")
    return render(request, "update.html", {"stu": student[0]})


def gotoDelete(request, id):
    student = Student.objects(id=ObjectId(id))
    student.delete()
    return redirect("/retrieve/")