from pydantic import BaseModel, Field
from typing_extensions import Optional
from graph.models.responses.SearchChapter import SearchChapterResponse
class StructuringWebSearchChapterResponse(BaseModel):
    web_search_chapters: Optional[list[SearchChapterResponse]] = (Field(description="A lista das buscas na internet, baseadas nos capítulos do ebook"))
  