from typing import TypedDict, Annotated
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from travel_module import search_buses, format_bus_results
import re

# Define input/output schema
class TravelState(TypedDict):
    from_destination: str
    to_destination: str
    final: str

def extract_destinations(query: str):
    """
    Extract source and destination from travel query
    """
    # Common patterns for travel queries
    patterns = [
        r"from\s+([^to]+?)\s+to\s+([^\s]+)",
        r"([^to]+?)\s+to\s+([^\s]+)",
        r"bus\s+from\s+([^to]+?)\s+to\s+([^\s]+)",
        r"travel\s+from\s+([^to]+?)\s+to\s+([^\s]+)"
    ]
    
    for pattern in patterns:
        match = re.search(pattern, query, re.IGNORECASE)
        if match:
            from_dest = match.group(1).strip()
            to_dest = match.group(2).strip()
            return from_dest, to_dest
    
    return None, None

def run_conversation(user_input: str):
    """
    Main conversation handler for travel queries
    """
    # Extract destinations from the query
    from_dest, to_dest = extract_destinations(user_input)
    
    if from_dest and to_dest:
        return run_travel_conversation(from_dest, to_dest)
    else:
        return "❌ Please provide both source and destination in the format: 'from [source] to [destination]' or '[source] to [destination]'"

def run_travel_conversation(from_destination: str, to_destination: str):
    """
    Handle travel/bus booking queries
    """
    # Step 1 - Search for buses
    def step_one(state: TravelState) -> TravelState:
        results = search_buses(state["from_destination"], state["to_destination"])
        formatted_results = format_bus_results(state["from_destination"], state["to_destination"], results)
        return {
            "from_destination": state["from_destination"],
            "to_destination": state["to_destination"],
            "final": formatted_results
        }

    # Build LangGraph flow for travel
    builder = StateGraph(TravelState)
    builder.add_node("step_one", step_one)
    builder.set_entry_point("step_one")
    builder.set_finish_point("step_one")

    graph = builder.compile()
    result = graph.invoke({
        "from_destination": from_destination,
        "to_destination": to_destination
    })
    return result["final"]