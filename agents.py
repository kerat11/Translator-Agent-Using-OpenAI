# agents.py

class Agent:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions


class AsyncOpenAI:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url


class OpenAIChatCompletionsModel:
    def __init__(self, model, openai_client):
        self.model = model
        self.openai_client = openai_client


class RunConfig:
    def __init__(self, model, model_provider, tracing_disabled=True):
        self.model = model
        self.model_provider = model_provider
        self.tracing_disabled = tracing_disabled


class Runner:
    @staticmethod
    async def run(agent, input, run_config):
        # Dummy translation logic for testing
        class Result:
            final_output = f"[Translated] ➡️ {input}"
        return Result()
