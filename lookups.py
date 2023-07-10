from enum import Enum


class LLM_MODEL_TYPE(Enum):
    DAVINCI = "text-davinci-003"
    FINE_TUNED_MODEL = "davinci:ft-personal-2023-06-21-14-33-02"
    GPT = "gpt-3.5-turbo"


