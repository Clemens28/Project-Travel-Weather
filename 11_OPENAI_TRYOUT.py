import os
import openai
openai.organization = "org-GrucJSGuCzxOh1RGuSZhQP0l"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()