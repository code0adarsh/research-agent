from datetime import datetime
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool

def save_to_txt(data: str, filename: str = "research_output.txt") -> str:
    """
    Saves the research output as plain narrative text.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = (
        "══════════════════════════════════════════════════════════════════════\n"
        "                     Research Output Report\n"
        "══════════════════════════════════════════════════════════════════════\n"
        f"Timestamp: {timestamp}\n\n"
        f"{data}\n\n"
        "══════════════════════════════════════════════════════════════════════\n\n"
    )
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    return f"Data successfully saved to {filename}"

# Create a tool that saves text to a file.
save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves the research output as a narrative text to a file."
)

# Define a web search tool using DuckDuckGo.
duckduckgo_search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=duckduckgo_search.run,
    description="Search the web for information."
)

# Define a Wikipedia search tool.
wiki_api_wrapper = WikipediaAPIWrapper(top_k_results=5, max_summary_length=1000)
wiki_tool = WikipediaQueryRun(api_wrapper=wiki_api_wrapper)
