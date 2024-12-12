from pydantic import BaseModel, Field
from typing_extensions import Optional

class ChapterResponse(BaseModel):
  content: Optional[str] = (Field(description="O conteúdo do capítulo"))
  number_chapter: Optional[int] = (Field(description="O número do capítulo do ebook"))
  