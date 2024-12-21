from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from .schema import DUMMY_DATA
from .tasks import send_notification
from .utils import get_expiry_details
from .models import DummyData
from .serializers import DummyDataSerializer
from drf_spectacular.utils import extend_schema, OpenApiExample



#Task 3.0 - create new column as Date and convert datetime 
class DummyDataView(APIView):

    ''' Enpoint to get Data : task 3.0 '''
    def get(self, request):
        return Response(DUMMY_DATA)




#Task 3.1 - Perform CRUD operations 
#DummyDataAPIView

class DummyDataListAPIView(APIView):
    serializer_class = DummyDataSerializer


    ''' Endpoint to perform CRUD operations on Data'''

    def get(self, request):
        record_id = request.query_params.get('record_id')
        expiry_details = get_expiry_details(request)
        if record_id:
            print(record_id)
            filtered_data = [item for item in DUMMY_DATA if item['id'] == int(record_id)]
            return Response({'data':filtered_data,**expiry_details}, status=status.HTTP_200_OK)
        return Response({'data':DUMMY_DATA,**expiry_details}, status=status.HTTP_200_OK)    

    @extend_schema(
        request=DummyDataSerializer,
        responses=DummyDataSerializer,
        examples=[
            OpenApiExample(
                name="Custom ISO",
                description="Showing the datetime in ISO format.",
                value={
                    "ten_min_std_deviation": "15",
                    "time": "2.46",
                    "datetime": "2024-12-19T12:34:56",
                    "ten_min_sampled_avg": "24.8"
                },
            ),
        ],
    )
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


class DummyDataDetailAPIView(APIView):
    serializer_class = DummyDataSerializer

    def get(self, request, pk):
        record = next((item for item in DUMMY_DATA if item['id'] == pk), None) 
        if not record:
            return Response({'error': 'Record not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(record, status=status.HTTP_200_OK)

    @extend_schema(
        request=DummyDataSerializer,
        responses=DummyDataSerializer,
        examples=[
            OpenApiExample(
                name="Custom ISO",
                description="Showing the datetime in ISO format.",
                value={
                    "ten_min_std_deviation": "15",
                    "time": "2.46",
                    "datetime": "2024-12-19T12:34:56",
                    "ten_min_sampled_avg": "24.8"
                },
            ),
        ],
    )
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
