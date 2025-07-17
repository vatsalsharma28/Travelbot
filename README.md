# 🚌 TravelBot AI - Smart Bus Booking Assistant

A powerful AI-powered travel bot that helps you find buses between any two destinations with direct booking links.

## ✨ Features

- **Smart Destination Detection**: Automatically extracts source and destination from natural language queries
- **Multi-Platform Search**: Searches across multiple bus booking platforms (RedBus, MakeMyTrip, Goibibo, etc.)
- **Direct Booking Links**: Provides clickable links to book tickets directly
- **Price Comparison**: Shows prices when available for easy comparison
- **Beautiful UI**: Modern, responsive interface with intuitive design
- **Real-time Search**: Live search with loading indicators

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Environment Variables

Create a `.env` file in the `lang` directory with your API keys:

```env
SERPER_API_KEY=your_serper_api_key_here
```

### 3. Run the Application

```bash
streamlit run main.py
```

## 🎯 How to Use

### Simple Interface

1. **Enter your destinations**:
   - From: Your starting point (e.g., "Jaipur")
   - To: Your destination (e.g., "Delhi")
2. **Select travel date** (optional)
3. **Click "Search Buses"** to find available options

### Natural Language Queries

You can also use natural language queries like:
- "bus from Mumbai to Pune"
- "travel from Bangalore to Chennai"
- "bus booking from Jaipur to Delhi"
- "bus tickets from Hyderabad to Bangalore"

### Example Queries

The app includes pre-built example queries that you can click to test:
- Mumbai to Pune
- Bangalore to Chennai
- Jaipur to Delhi
- Hyderabad to Bangalore

## 🔧 Technical Architecture

### Core Components

1. **`main.py`**: Streamlit web interface with travel-focused design
2. **`travel_module.py`**: Handles bus search and result formatting
3. **`langgraph_flow.py`**: Orchestrates the conversation flow
4. **`serper_module.py`**: Web search functionality

### Flow Diagram

```
User Input → Destination Extraction → API Search → Result Formatting → Display Results
```

## 🎨 UI Features

- **Responsive Design**: Works on desktop and mobile
- **Clean Interface**: Focused travel interface without distractions
- **Real-time Search**: Live search with loading indicators
- **Formatted Results**: Clean, readable bus options with direct links
- **Error Handling**: User-friendly error messages
- **Example Queries**: Quick access to common searches

## 🔍 Search Capabilities

The travel bot searches across multiple platforms:

### Booking Websites
- RedBus
- MakeMyTrip
- Goibibo
- Other major bus booking platforms

### Information Provided
- Bus operator names
- Direct booking links
- Price information (when available)
- Route details
- Booking tips and recommendations

## 🛠️ Customization

### Adding New Search Platforms

To add new bus booking platforms, modify the `search_queries` list in `travel_module.py`:

```python
search_queries = [
    f"bus booking {from_destination} to {to_destination} redbus",
    f"bus tickets {from_destination} to {to_destination} makemytrip",
    f"bus schedule {from_destination} to {to_destination} goibibo",
    # Add your new platform here
    f"bus booking {from_destination} to {to_destination} your_platform"
]
```

### Modifying Result Format

Edit the `format_bus_results` function in `travel_module.py` to customize how results are displayed.

## 🔐 API Requirements

### Required APIs

1. **Serper API**: For web search functionality
   - Sign up at: https://serper.dev
   - Used for finding bus booking websites

## 🚨 Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure your Serper API key is correctly set in `.env`
2. **No Results**: Check internet connection and API key validity
3. **Import Errors**: Make sure all dependencies are installed

### Debug Mode

To enable debug logging, add this to your `.env`:

```env
DEBUG=true
```

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For support or questions, please open an issue on the repository.

---

**Happy Traveling! 🚌✈️**
