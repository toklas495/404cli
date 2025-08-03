from datetime import datetime

def format_date(iso_str: str) -> str:
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return dt.strftime("%B %d, %Y at %I:%M %p")  # e.g. July 30, 2025 at 08:45 PM
    except:
        return iso_str  # fallback if format breaks
