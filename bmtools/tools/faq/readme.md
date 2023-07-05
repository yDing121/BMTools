# Dummy FAQ Tool for testing Chinese FAQs

Contributor: [Lance Ding](https://github.com/yDing121)

# Weather Info Tool

This is a dummy tool for testing Chinese FAQs as a "tool" to employ tool learning on

## Setup

The tool is initialized with the following parameters:

- **name_for_model**: "FAQ Info"
- **description_for_model**: "Plugin for retrieving FAQ information"
- **logo_url**: ""
- **contact_email**: "hello@contact.com"
- **legal_info_url**: "hello@legal.com"

## API Key

The tool does not require an API key

## Endpoint

The tool provides the following endpoints:

- **/get_answer**: Get the answer to the given FAQ if there is an exact match and returns "Not found" if there is no match

## Function Descriptions

- **/get_answer(question: str) -> str
- **get_weather_today(location: str) -> str**: This function gets today's weather for a given location. The location should be a string. The function returns a string with the weather information.
- **forecast_weather(location: str, days: int) -> str**: This function forecasts the weather for a given location in the upcoming days. The location should be a string and days should be an integer. The function returns a string with the weather forecast.