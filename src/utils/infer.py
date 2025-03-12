from ollama import AsyncClient
from src.utils.models import ResponseModel
from typing import List, Dict, AsyncGenerator

import json

class OllamaInfer:
    def __init__(self, host: str, model: str, num_ctx: int):
        self.client = AsyncClient(host=host)
        self.model = model
        self.num_ctx = num_ctx
        
    async def infer(self, messages: List[Dict[str, str]]) -> AsyncGenerator[ResponseModel, None]:
        while True:
            result = await self.client.chat(
                messages=messages,
                model=self.model,
                format=ResponseModel.model_json_schema(),
                options={
                    "num_ctx": self.num_ctx
                }
            )
            result = ResponseModel.model_validate_json(result.message.content)
            
            messages.append(json.dumps(result.model_dump(), indent=4))
            yield result
            
            if not result.chain:
                break