import os
import requests
from dotenv import load_dotenv
load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")

def search_buses(from_destination: str, to_destination: str):
    """
    Search for buses between two destinations
    """
    # Create search queries for different bus booking platforms
    search_queries = [
        f"bus booking {from_destination} to {to_destination} redbus",
        f"bus tickets {from_destination} to {to_destination} makemytrip",
        f"bus schedule {from_destination} to {to_destination} goibibo",
        f"bus routes {from_destination} to {to_destination} bus booking"
    ]
    
    all_results = []
    
    for query in search_queries:
        try:
            results = fetch_bus_search_results(query)
            all_results.extend(results)
        except Exception as e:
            print(f"Error searching for query '{query}': {e}")
    
    return all_results

def fetch_bus_search_results(query: str):
    """
    Fetch bus search results using Serper API
    """
    url = "https://google.serper.dev/search"
    headers = {"X-API-KEY": SERPER_API_KEY}
    body = {"q": query}
    
    response = requests.post(url, json=body, headers=headers)
    data = response.json()
    
    # Extract relevant bus booking results
    organic_results = data.get("organic", [])
    shopping_results = data.get("shopping", [])
    
    results = []
    
    # Process organic results
    for result in organic_results[:5]:  # Top 5 results
        if any(keyword in result.get("title", "").lower() for keyword in ["bus", "booking", "ticket", "travel"]):
            results.append({
                "title": result.get("title", ""),
                "link": result.get("link", ""),
                "snippet": result.get("snippet", ""),
                "type": "organic"
            })
    
    # Process shopping results (if any)
    for result in shopping_results[:3]:
        results.append({
            "title": result.get("title", ""),
            "link": result.get("link", ""),
            "price": result.get("price", ""),
            "type": "shopping"
        })
    
    return results

def format_bus_results(from_dest: str, to_dest: str, results: list):
    """
    Format bus search results into a readable format
    """
    if not results:
        return f"No bus booking options found for {from_dest} to {to_dest}"
    
    formatted_result = f"🚌 **Bus Options from {from_dest} to {to_dest}**\n\n"
    
    # Group results by type
    organic_results = [r for r in results if r.get("type") == "organic"]
    shopping_results = [r for r in results if r.get("type") == "shopping"]
    
    if organic_results:
        formatted_result += "**📋 Booking Websites:**\n"
        for i, result in enumerate(organic_results[:5], 1):
            formatted_result += f"{i}. **{result['title']}**\n"
            formatted_result += f"   🔗 [Book Now]({result['link']})\n"
            if result.get("snippet"):
                formatted_result += f"   📝 {result['snippet'][:100]}...\n"
            formatted_result += "\n"
    
    if shopping_results:
        formatted_result += "**🛒 Direct Booking Options:**\n"
        for i, result in enumerate(shopping_results[:3], 1):
            formatted_result += f"{i}. **{result['title']}**\n"
            formatted_result += f"   🔗 [Book Now]({result['link']})\n"
            if result.get("price"):
                formatted_result += f"   💰 {result['price']}\n"
            formatted_result += "\n"
    
    formatted_result += "\n**💡 Tips:**\n"
    formatted_result += "• Click on the links above to book your bus tickets\n"
    formatted_result += "• Compare prices across different platforms\n"
    formatted_result += "• Book in advance for better deals\n"
    formatted_result += "• Check bus schedules and duration before booking"
    
    return formatted_result 