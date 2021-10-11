import iso8601


class BaseModel(dict):
    def __getattr__(self, key):
        return self[key]

    def _iso8601_to_datetime(self, source):
        return iso8601.parse_date(source)


class User(BaseModel):
    ...


class Authentication(BaseModel):
    ...


class Client(BaseModel):
    ...


class Domain(BaseModel):
    ...


class Language(BaseModel):
    ...


class Project(BaseModel):
    @property
    def date_created(self):
        return self._iso8601_to_datetime(self.dateCreated)


class Job(BaseModel):
    ...


class JobPart(BaseModel):
    ...


class TranslationMemory(BaseModel):
    ...


class AsynchronousRequest(BaseModel):
    """
    You can know progress when hit api.Asynchronous.getAsyncRequest with id of this class instance.
    """
    ...


class AsynchronousResponse(BaseModel):
    def __init__(self, source):
        super(AsynchronousResponse, self).__init__({} if source is None else source)

    def is_complete(self):
        return 'error' in self

    def has_error(self):
        return self.is_complete() and self.error is not None


class Segment(BaseModel):
    ...


class SegmentSearchResult(BaseModel):
    """
    Sometime segment has more data. It is for it. Give me a good name for this class.
    http://wiki.memsource.com/wiki/Job_API_v7#Get_Segments is for Segment.
    http://wiki.memsource.com/wiki/Translation_Memory_API_v4#Search_Segment_By_Task is for this.
    """
    pass


class Analysis(BaseModel):
    ...


class MxliffUnit(BaseModel):
    ...


class TermBase(BaseModel):
    ...
