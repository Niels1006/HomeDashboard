import os

from influxdb_client.client import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

BUCKET = os.getenv("BUCKET")
ORG = os.getenv("ORG")

client = influxdb_client.InfluxDBClient(url=os.getenv("INFLUX_URL"), token=os.getenv("INFLUX_HOUSE_KEY"), org=ORG)
write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()
