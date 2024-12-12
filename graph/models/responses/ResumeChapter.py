from pydantic import BaseModel, Field
from typing_extensions import Optional

class ResumeChapterResponse(BaseModel):
  title: Optional[str] = (Field(description="O título do capítulo"))
  resume: Optional[str] = (Field(description="O resumo do capítulo"))
  number_chapter: Optional[int] = (Field(description="O número do capítulo do ebook"))
  content: Optional[str] = (Field(description="O conteúdo do capítulo"))
  tags: Optional[list[str]] = (Field(description="As palavras chaves do capítulo"))
  