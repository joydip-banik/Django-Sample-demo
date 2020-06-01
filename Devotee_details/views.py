from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import DevoteeInfo
#from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def add_devotee_details(request):
    if request.method == "POST":
        temple_name = request.POST["temple_name"]
        department_name = request.POST["department_name"]
        legal_name = request.POST["legal_name"]
        initiated_name = request.POST["initiated_name"]
        initiated_place = request.POST["initiated_place"]
        initiated_date = request.POST["initiated_date"]
        counselor = request.POST["counselor"]
        gotra = request.POST["gotra"]
        occupation = request.POST["occupation"]
        address = request.POST["address"]
        qualification = request.POST["qualification"]
        date_of_birth = request.POST["date_of_birth"]
        age = request.POST["age"]
        skill = request.POST["skill"]
        wedding_anniversary = request.POST["wedding_anniversary"]
        mobile_number = request.POST["mobile_number"]
        whats_app_number = request.POST["whats_app_number"]
        email_id = request.POST["email_id"]

        family_other_name = request.POST['family_other_name']
        relationship = request.POST["relationship"]
        family_other_date = request.POST["family_other_date"]
        specialday = request.POST["specialday"]
        family_other_name1 = request.POST["family_other_name1"]
        relationship1 = request.POST["relationship1"]
        family_other_date1 = request.POST["family_other_date1"]
        specialday1 = request.POST["specialday1"]
        family_other_name2 = request.POST["family_other_name2"]
        relationship2 = request.POST["relationship2"]
        family_other_date2 = request.POST["family_other_date2"]
        specialday2 = request.POST["specialday2"]
        family_other_name3 = request.POST["family_other_name3"]
        relationship3 = request.POST["relationship3"]
        family_other_date3 = request.POST["family_other_date3"]
        specialday3 = request.POST["specialday3"]

        data = DevoteeInfo(temple_name=temple_name,department_name=department_name,legal_name=legal_name,initiated_name=initiated_name,initiated_place=initiated_place,initiated_date=initiated_date,counselor=counselor,gotra=gotra,occupation=occupation,address=address,qualification=qualification,date_of_birth=date_of_birth,age=age,skill=skill,wedding_anniversary=wedding_anniversary,mobile_number=mobile_number,whats_app_number=whats_app_number,email_id=email_id,family_other_name=family_other_name, relationship=relationship,family_other_date=family_other_date,specialday=specialday,family_other_name1=family_other_name1,relationship1=relationship1,family_other_date1=family_other_date1,specialday1=specialday1,family_other_name2=family_other_name2,relationship2=relationship2,family_other_date2=family_other_date2,specialday2=specialday2,family_other_name3=family_other_name3,relationship3=relationship3,family_other_date3=family_other_date3,specialday3=specialday3)
        data.save()
        return HttpResponse("<h1>Data save Successfully</h1>")


    return render(request, "index.html")