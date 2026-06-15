
def aqi_category(aqi_value):
    if aqi_value <= 50:
        return "Good"
    elif aqi_value <= 100:
        return "Moderate"
    elif aqi_value <= 150:
        return "Unhealthy for Sensitive Groups"
    elif aqi_value <= 200:
        return "Unhealthy"
    elif aqi_value <= 300:
        return "Very Unhealthy"
    return "Hazardous"

def aqi_description(category):
    descriptions = {
        "Good": "Air quality is satisfactory and safe for most people.",
        "Moderate": "Air quality is acceptable; sensitive people may experience minor symptoms.",
        "Unhealthy for Sensitive Groups": "Sensitive groups should limit outdoor activity.",
        "Unhealthy": "Everyone may experience health effects.",
        "Very Unhealthy": "Health warnings of emergency conditions.",
        "Hazardous": "Health alert: avoid exposure."
    }
    return descriptions.get(category, "")
