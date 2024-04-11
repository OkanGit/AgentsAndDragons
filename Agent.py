import pandas as pd
from openai import OpenAI

class Agent:

    def __init__(self, assistant) -> None:
        self.assistant = assistant
        pass