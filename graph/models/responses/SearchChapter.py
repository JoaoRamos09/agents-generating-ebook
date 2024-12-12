from pydantic import BaseModel, Field
from typing_extensions import Optional

class SearchChapterResponse(BaseModel):
  web_search: Optional[str] = (Field(description="A busca na internet para o capítulo"))
  content: Optional[str] = (Field(description="O conteúdo do capítulo"))
  number_chapter: Optional[int] = (Field(description="O número do capítulo do ebook"))
  