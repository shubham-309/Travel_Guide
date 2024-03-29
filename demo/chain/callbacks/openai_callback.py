from typing import Dict, Union, Any, List

from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import AgentAction
from chain.utils import *


# First, define custom callback handler implementations
class CustomOpenAICallback(BaseCallbackHandler):
    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> Any:
        self.print_message(
            f"on_llm_start {serialized['name']} and following are the prompts: {prompts}",
        )

    # def on_llm_new_token(self, token: str, **kwargs: Any) -> Any:
    #     pprint(f"on_new_token {token}")

    def on_llm_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> Any:
        self.print_message(f"on_llm_error {error}")

    def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ) -> Any:
        self.print_message(
            f"on_chain_start {serialized['name']} and inputs are: {inputs}"
        )

    def on_tool_start(
        self, serialized: Dict[str, Any], input_str: str, **kwargs: Any
    ) -> Any:
        self.print_message(
            f"on_tool_start {serialized['name']} and inputs are: {input_str}"
        )

    def on_agent_action(self, action: AgentAction, **kwargs: Any) -> Any:
        self.print_message(f"on_agent_action {action}")

    def print_message(self, message):
        pprint(yellow, "DEBUGDEMO: " + message)
