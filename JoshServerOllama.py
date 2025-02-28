from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from dotenv import load_dotenv
from langsmith import traceable
import os

load_dotenv()

class JoshServerOllama:
    def __init__(self, model="llama3.2:1b"):
        self.model = model
        self.llm = OllamaLLM(model=model, base_url=os.environ.get("OLLAMA_BASE_URL"))

    @traceable
    def chat(self, prompt: str, print_response=True, stream=True) -> str:
        if stream:
            return self._stream_response(prompt, print_response)
        else:
            response = self.llm.invoke(prompt)
            
            if print_response:
                self._print_response(response)
            
            return response

    @traceable
    def prompt_template(self, template_prompt: str, template_values: dict, print_response=True, stream=True) -> str:
        prompt_template = PromptTemplate.from_template(template_prompt)
        formatted_prompt = prompt_template.format(**template_values)
        
        if stream:
            return self._stream_response(formatted_prompt, print_response)
        else:
            response = self.llm.invoke(formatted_prompt)
            
            if print_response:
                self._print_response(response)
            
            return response

    @traceable
    def chat_prompt_template(self, system_prompt: str, template_prompt: str, template_values: dict, print_response=True, stream=True) -> str:
        prompt_template = ChatPromptTemplate([
            ("system", system_prompt),
            ("user", template_prompt),
        ])
        formatted_prompt = prompt_template.format(**template_values)
        
        if stream:
            return self._stream_response(formatted_prompt, print_response)
        else:
            response = self.llm.invoke(formatted_prompt)
            
            if print_response:
                self._print_response(response)
            
            return response

    def _stream_response(self, prompt: str, print_response=True) -> str:
        response_stream = self.llm.stream(prompt)
        
        full_response = ""

        for chunk in response_stream:
            if print_response:
                print(chunk, end="", flush=True)
            
            full_response += chunk
        
        if print_response:
            print("\n")  # Add a newline at the end
            
        return full_response

    def _print_response(self, response: str) -> None:
        print("JoshServerOllama:")
        print(response)