import os
from dotenv import load_dotenv
import google.generativeai as genai

# Import LangChain components
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor

# Import tools from tools.py
from tools import search_tool, wiki_tool, save_tool

# Load environment variables (ensure .env contains GOOGLE_API_KEY)
load_dotenv()

# Configure the language model and generative AI.
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define a prompt template that instructs the agent to produce a rich narrative response.
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            (
                "You are a knowledgeable and creative research assistant. "
                "Based on the user's query, generate a comprehensive, narrative research report "
                "in plain text. Use clear headings, bullet points, and engaging language to present the findings. "
                "Avoid formatting your output as JSON or code blocks. For example, your output might look like:\n\n"
                "It's fascinating to explore the vast world of food! Here's a glimpse into the diverse and delicious cuisines found across the globe:\n\n"
                "Key Aspects of World Cuisines:\n\n"
                "Regional Diversity:\n"
                "- Food is deeply rooted in local culture, geography, and history. Variations occur even within a single country. For example, Indian cuisine varies dramatically from north to south.\n"
                "- Climate and available ingredients heavily influence dietary choices.\n\n"
                "Staple Foods:\n"
                "- Many cultures rely on staples like rice, wheat, corn, and potatoes.\n\n"
                "Flavor Profiles:\n"
                "- Each cuisine boasts its unique flavor profile, achieved through specific spices, herbs, and techniques.\n"
                "  (Think of the spiciness of Thai food, the savory richness of French cuisine, or the umami of Japanese dishes.)\n\n"
                "Cultural Significance:\n"
                "- Food plays a vital role in social gatherings and traditions.\n\n"
                "Examples of Iconic World Cuisines:\n"
                "• Italian: Known for its pasta, pizza, and fresh ingredients like tomatoes and basil.\n"
                "• Mexican: Featuring tacos, enchiladas, and a vibrant use of chili peppers and spices.\n"
                "• Indian: Rich in curries and flavorful spices, with diverse vegetarian and meat dishes.\n"
                "• Japanese: Emphasizes fresh, seasonal ingredients and precise techniques (e.g., sushi, ramen).\n"
                "• French: Renowned for elegant sauces and pastries.\n"
                "• Thai: Celebrated for its balance of sweet, sour, salty, and spicy flavors.\n\n"
                "Where to find more information:\n"
                "- TasteAtlas, Wikipedia, and various travel/food blogs.\n\n"
                "If the user's query includes instructions to save the output, remember to automatically invoke the file-saving tool as well.\n\n"
                "Now, generate the research report for the query."
            )
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

# List all tools available to the agent.
tools = [search_tool, wiki_tool, save_tool]

# Create a tool-calling agent using the LLM, prompt, and tools.
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

# Initialize the AgentExecutor with verbose logging enabled.
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Get user input.
query = input("What can I help you research today? ")
raw_response = agent_executor.invoke({"query": query})

# Print the raw narrative response.
print("\nAgent's Narrative Response:")
print(raw_response.get("output"))

# OPTIONAL: If the agent's output indicates a save action, we can trigger the save function manually.
if "save_text_to_file" in raw_response.get("output").lower():
    # For demonstration, we pass the entire narrative text to the save function.
    result = save_tool.func(raw_response.get("output"))
    print("\nSave Tool Result:")
    print(result)
