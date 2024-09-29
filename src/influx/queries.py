from influxdb_client.client.flux_table import FluxRecord

from src.influx import constants
from src.influx.constants import query_api, ORG


class Queries:
    @staticmethod
    def get_set(field: str, location: str, measurement: str = "esp32", timeframe: int = 3600, mean: int = 0) -> list[FluxRecord]:
        if mean == 0:
            mean = 30

        query = (f'from(bucket: "{constants.BUCKET}") '
                 f'|> range(start: -{timeframe}s) '
                 f'|> filter(fn:(r) => r._measurement == "{measurement}") '
                 f'|> filter(fn:(r) => r.location == "{location}") '
                 f'|> filter(fn:(r) => r._field == "{field}")'
                 f'|> aggregateWindow(every: {mean}s, fn: mean)')

        result = query_api.query(org=ORG, query=query)

        if len(result) == 0:
            raise ValueError("No data found")

        return result[0].records
