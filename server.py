import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/twinword/api/keyword-suggestion'

mcp = FastMCP('keyword-suggestion')

@mcp.tool()
def keyword_suggestion(phrase: Annotated[str, Field(description='')],
                       lang: Annotated[Union[str, None], Field(description='Languages available for targeting. Use the corresponding criterion ID for the Language target . ')] = None,
                       loc: Annotated[Union[str, None], Field(description='Two-letter country codes. ')] = None) -> dict: 
    '''Recommend keywords for SEO and SEM scored by relevance.'''
    url = 'https://twinword-keyword-suggestion-v1.p.rapidapi.com/suggest/'
    headers = {'x-rapidapi-host': 'twinword-keyword-suggestion-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'phrase': phrase,
        'lang': lang,
        'loc': loc,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
