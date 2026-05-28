
import os
import re
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")

# Common city-to-IATA mappings for query parsing
CITY_IATA = {
    "tokyo": "TYO", "paris": "CDG", "dubai": "DXB", "bangkok": "BKK",
    "rome": "FCO", "london": "LHR", "new york": "JFK", "los angeles": "LAX",
    "singapore": "SIN", "mumbai": "BOM", "delhi": "DEL", "bali": "DPS",
    "sydney": "SYD", "istanbul": "IST", "seoul": "ICN", "barcelona": "BCN",
    "hong kong": "HKG", "san francisco": "SFO", "chicago": "ORD",
    "kuala lumpur": "KUL", "amsterdam": "AMS", "toronto": "YYZ",
    "beijing": "PEK", "shanghai": "PVG", "osaka": "KIX", "jaipur": "JAI",
    "goa": "GOI", "chennai": "MAA", "kolkata": "CCU", "hyderabad": "HYD",
}


def _extract_destination(query: str) -> str | None:
    """Try to extract a destination city/IATA from the user query."""
    query_lower = query.lower()
    for city, iata in CITY_IATA.items():
        if city in query_lower:
            return iata
    # Check if user typed an IATA code directly (3 uppercase letters)
    match = re.search(r"\b([A-Z]{3})\b", query)
    if match:
        return match.group(1)
    return None


def search_flights(query: str) -> str:
    if not API_KEY:
        return "Error: AVIATIONSTACK_API_KEY is not set."

    url = "http://api.aviationstack.com/v1/flights"

    params = {
        "access_key": API_KEY,
        "limit": 5,
    }

    # Use destination from query if we can parse one
    dest = _extract_destination(query)
    if dest:
        params["arr_iata"] = dest

    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        return f"Error fetching flights: {e}"

    if "error" in data:
        return f"API error: {data['error'].get('message', data['error'])}"

    flights = []
    for flight in data.get("data", [])[:5]:
        airline = flight.get("airline", {}).get("name", "Unknown")
        departure = flight.get("departure", {}).get("airport", "Unknown")
        arrival = flight.get("arrival", {}).get("airport", "Unknown")
        status = flight.get("flight_status", "Unknown")
        flights.append(
            f"Airline: {airline}\n"
            f"Departure: {departure}\n"
            f"Arrival: {arrival}\n"
            f"Status: {status}"
        )

    return "\n\n".join(flights) if flights else "No flight results found."