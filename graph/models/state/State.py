from typing import TypedDict
from graph.models.responses.ResumeChapter import ResumeChapterResponse
from graph.models.responses.SearchChapter import SearchChapterResponse

class State(TypedDict):
    title: str
    input_user: str
    subject: str
    max_chapters: int
    resume_chapters: list[ResumeChapterResponse]
    search_chapters: list[SearchChapterResponse]
