from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq  # Groq requires a free API key from groq.com
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv


load_dotenv()

@tool
def calculator(a:float, b:float) -> str:
    '''Useful for performing basic arithmetric calculations.'''
    return f"the sum of {a} and {b} is {a + b}"

def main():
    model = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

    tools = [calculator]
  
    agent_executor = create_react_agent(model,tools)
    print("\nWelcome! i am your Ai assistant. type 'quit' to exit.")
    print("\nyou can chat with me about anything you like or ask me to perform calculations for you.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'quit':
            print("\nGoodbye!")
            break
        
        print("\nAsistant: ", end="")
        for chunk in agent_executor.stream(
           {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")

        print()


if __name__ == "__main__":
    main()                    
           