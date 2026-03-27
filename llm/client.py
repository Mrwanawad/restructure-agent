import os
from dotenv import load_dotenv;         load_dotenv()
import google.genai as genai
from google.genai.errors import ClientError
from llm.system_prompt import SYSTEM_PROMPT
from typing import Dict, Any 
from termcolor import colored
import json
from groq import Groq

class LLM :
    
    def __init__(self, api_key: str = ''):
        
        if api_key :
            self.api_key = api_key
            print( colored( f'API Key Set Successfully ! -> {api_key}', color = (0, 255, 128) ) ) 
        
        else :
            print( colored( f'API Key Set failed ! -> {api_key}', color = 'red' ) )
            print( colored( f'---API Key will be accessed from .env file ! -> {api_key}', color = (0, 255, 128) ) )
            self.api_key = os.getenv( 'API_KEY' ) 
        
    def conv_llm_str_to_dict( self, llm_output: str, json_output: bool = False ) -> Dict[ str, Any ] | str :
        llm_output = llm_output.replace( '\n', '' ).\
                                replace( 'true', 'True' ).\
                                replace( 'false', 'False' ).\
                                replace( '?', '' ).\
                                replace( 'null', '"null"' )    
                                
        dict_output = eval(  llm_output)
        if json_output:
            return json.dumps( dict_output, indent= 4 )
        
        else:
            return dict_output        
        
    def call_llm( self, content: str ) -> Dict[ str, Any ] | str :
        self.client = Groq( api_key= self.api_key )

        chat_completion = self.client.chat.completions.create(
            messages=[
        # Set an optional system message. This sets the behavior of the
        # assistant and can be used to provide specific instructions for
        # how it should behave throughout the conversation.
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        # Set a user message for the assistant to respond to.
        {
            "role": "user",
            "content": content,
        }
            ],

            # The language model which will generate the completion.
            model="openai/gpt-oss-120b"
        )
        llm_output = chat_completion.choices[0].message.content
        return self.conv_llm_str_to_dict( llm_output )
