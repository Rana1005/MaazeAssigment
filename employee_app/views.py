from django.shortcuts import render
from rest_framework.views import APIView
from .models import EmployeeDetailsModel,ExperianceModel
# Create your views here.
from rest_framework.response import Response
from django.db import connection

def execute_raw_sql_query(raw_sql_query):
    with connection.cursor() as cursor:
        cursor.execute(raw_sql_query)
        result = cursor.fetchall()

    return result
class AllempView(APIView):
    def get(self, request):
        result_dict = []
        query ="""select * from employee_app_employeedetailsmodel;"""
        db_result = execute_raw_sql_query(query)
        print(db_result)
        for data in db_result:
            result_dict.append({
                "name":data[0],
                "age":data[1],
                "experiance":data[1],
                "emp_id": data[3]
            })
        return Response(result_dict)

class SearchEmp(APIView):
    def get(self, request):
        result_dict = []
        data = int(request.GET.get("id"))
        query =f"""select * from employee_app_employeedetailsmodel where id = {data};"""
        db_result = execute_raw_sql_query(query)
        for data in db_result:
            result_dict.append({
                    "name":data[0],
                    "age":data[1],
                    "experiance":data[1],
                    "emp_id": data[3]
                })
        return Response(result_dict)
        # return Response(db_result)
        


    