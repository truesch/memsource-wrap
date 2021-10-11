from pydantic import BaseModel
import iso8601


class BaseSchema(BaseModel):

    def _iso8601_to_datetime(self, source):
        return iso8601.parse_date(source)
