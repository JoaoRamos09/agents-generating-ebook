from pydantic import BaseModel, Field
from typing_extensions import Optional
from graph.models.responses.Chapter import ChapterResponse

class ChaptersResponse(BaseModel):
  chapters: Optional[list[ChapterResponse]] = (Field(description="Os capítulos do ebook"))
