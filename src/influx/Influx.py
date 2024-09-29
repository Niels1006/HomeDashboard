from src.influx.constants import query_api, write_api, BUCKET, ORG
from influxdb_client import Point


class Influx:
    @staticmethod
    def get(query: str):
        return query_api.query(query)

    @staticmethod
    def write(points: list[Point]):
        write_api.write(bucket=BUCKET, org=ORG, record=points)
