from pydantic import BaseModel, Field
from typing import Union, Literal

class BaseToolArgs(BaseModel):
    tool: str = Field(..., title="Tool name", description="Name of the tool to be executed")
    
class SendMessage(BaseToolArgs):
    tool: Literal["send_message"]
    content: str = Field(..., title="Message content", description="Content of the message to be sent")
    
class CheckWeather(BaseToolArgs):
    tool: Literal["check_weather"]
    location: str = Field(..., title="Location", description="City name to check the weather for")
    
ToolArgs = Union[
    SendMessage,
    CheckWeather
]

class ResponseModel(BaseModel):
    reasoning: str = Field(..., title="Reasoning", description="Your reasoning for the user query and tool execution")
    tool_args: ToolArgs = Field(..., title="Tool arguments", description="Arguments for the tool to be executed according to the reasoning")
    chain: bool = Field(False, title="Tool chain", description="Whether to chain the tool execution, set to `true` to use another tool after this one")