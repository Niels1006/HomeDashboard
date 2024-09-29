from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_202_ACCEPTED
from rest_framework.views import APIView

from src.influx.queries import Queries


class DataAPI(APIView):
    def get(self, request):
        field = request.GET.get("field")
        location = request.GET.get("location")
        measurement = request.GET.get("measurement")

        timeframe = int(request.GET.get("timeframe"))
        mean = int(request.GET.get("mean", 0))

        points = Queries.get_set(field, location, measurement, timeframe, mean)
        results = [(p.get_time(), p.get_value()) for p in points]

        return Response(results, status=HTTP_202_ACCEPTED)
