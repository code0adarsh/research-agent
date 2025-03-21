# Research Agent with LangChain & Google Gemini

This project implements a research agent that leverages LangChain and Google Gemini generative AI to produce detailed, narrative research reports based on user queries. The agent utilizes external tools (such as DuckDuckGo and Wikipedia search) to gather information and can automatically save the final report to a text file.

## Features

- **Natural Language Research Reports:**  
  Generates comprehensive and engaging research papers on any topic in a narrative, human-readable format.

- **Tool Integration:**  
  Uses external search tools (DuckDuckGo, Wikipedia) to fetch real-time data and incorporates those findings into the report.

- **Automatic File Saving:**  
  If the query includes a directive to save, the agent automatically writes the final report to a file (`research_output.txt`).

- **Modular Design:**  
  The code is organized into separate modules for tool definitions and main application logic, making it easy to maintain and extend.

## Prerequisites

- **Python 3.9+**  
- **Pip**

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/research-agent.git
   cd research-agent

2. **Create and Activate a Virtual Environment (optional but recommended):**
    python -m venv venv
### On Windows:
    venv\Scripts\activate
### On macOS/Linux:
    source venv/bin/activate
3. **Install Dependencies:**
    pip install -r requirements.txt
### If you don’t have a requirements.txt, manually install the necessary packages:
    pip install python-dotenv pydantic google-generativeai langchain-google-genai langchain-communit
4. **Configure Environment Variables:**
    GOOGLE_API_KEY=your_google_api_key_here

## Usage
1. **Run the Research Agent:**
  python main.py

2. **Enter Your Query:**
# For example:

    What can I help you research today? foods across the world, save to a file

3. **Review the Output:**
    The agent will generate a narrative research report and display the output in the console. If the query includes a save directive, the report is also saved to research_output.txt in your current directory.

File Structure
**main.py:**
The main application file. It sets up the agent, loads environment variables, and handles user interaction.

**tools.py:**
Contains definitions for all the tools used by the agent (e.g., web search, Wikipedia search, and file-saving functionality).

**.env:**
Contains your environment variables (specifically, the GOOGLE_API_KEY).

#Contributing
Contributions are welcome! Feel free to open issues or submit pull requests if you have ideas to enhance the functionality or improve the code.

#License
This project is licensed under the MIT License.
