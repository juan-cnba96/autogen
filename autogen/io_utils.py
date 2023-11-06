import asyncio
from typing import Union, Dict
from autogen.agentchat.agent import Agent


class HumanInputHandler:
    def __init__(self):
        self._future = None

    async def _get_human_input(self, prompt: str) -> None:
        """Prompt the user for input and set the result in the future."""
        human_input = await asyncio.to_thread(input, prompt)
        self._future.set_result(human_input)

    async def wait_for_input(self, prompt) -> str:
        """Wait for the user input to be available and return it."""
        self._future = asyncio.Future()
        asyncio.create_task(self._get_human_input(prompt))
        return await self._future

    def get_human_input(self, prompt: str) -> str:
        """Prompt the user for input and return it."""
        return input(prompt)


class OutputHandler:
    def output(self, message: Union[Dict, str], sender: Agent) -> None:
        formatted_message = (
            message if isinstance(message, str) else ", ".join(f"{key}: {value}" for key, value in message.items())
        )
        print(f"From {sender}: {formatted_message}")

    def output_str(self, str_param):
        print(str_param, flush=True)

    async def a_output(self, message: Union[Dict, str], sender: Agent) -> None:
        """Simple call to output, but async"""
        self.output(message, sender)

    async def a_output_str(self, str_param):
        """Simple call to output_str, but async"""
        self.output_str(str_param)
