from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from .schema import DUMMY_DATA
from .tasks import send_notification
from .utils import get_expiry_details


#Task 3.0 - create new column as Date and convert datetime 
class DummyDataView(APIView):

    ''' Enpoint to get Data : task 3.0 '''
    def get(self, request):
        return Response(DUMMY_DATA)



#Task 3.1 - Perform CRUD operations 
class DummyDataAPIView(APIView):

    ''' Endpoint to perform CRUD operations on Data'''

    def get(self, request):
        record_id = request.query_params.get('record_id')
        expiry_details = get_expiry_details(request)
        if record_id:
            print(record_id)
            filtered_data = [item for item in DUMMY_DATA if item['id'] == int(record_id)]
            return Response({'data':filtered_data,**expiry_details}, status=status.HTTP_200_OK)
        return Response({'data':DUMMY_DATA,**expiry_details}, status=status.HTTP_200_OK)    


    def post(self, request):
        new_record = request.data
        #print(new_record)
        date = request.data.get('date')
        new_record['id'] = len(DUMMY_DATA) + 1  # Auto-generate an ID
        if date:
            DUMMY_DATA.append(new_record)
        else:
            dt = datetime.strptime(new_record["datetime"], "%Y-%m-%dT%H:%M:%S")
            new_record["date"] = dt.strftime("%d-%B-%Y")  # Format: DD-Month-Year
            DUMMY_DATA.append(new_record)


        # task 3.2- send notification for batch job 
        send_notification()

        return Response(new_record, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        record = next((item for item in DUMMY_DATA if item['id'] == pk), None)
        if not record:
            return Response({'error': 'Record not found'}, status=status.HTTP_404_NOT_FOUND)
        record.update(request.data)
        return Response(record, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        global DUMMY_DATA
        DUMMY_DATA = [item for item in DUMMY_DATA if item['id'] != pk]
        return Response({'message': 'Record deleted'}, status=status.HTTP_204_NO_CONTENT)
