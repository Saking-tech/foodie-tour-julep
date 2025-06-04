# Foodie Tour Generator

A smart culinary tour generator that creates personalized food experiences based on weather conditions and user preferences. This application uses AI to generate detailed food tours for multiple cities, taking into account local dishes, restaurant recommendations, and current weather conditions.

## Features

- 🌍 Multi-city tour generation
- 🌤️ Weather-informed dining recommendations
- 🍽️ Local dish suggestions
- 🏪 Restaurant recommendations
- 🥗 Dietary restriction support
- 💰 Budget preference consideration

## Prerequisites

- Python 3.8+
- Julep AI API key
- OpenWeatherMap API key
- Brave Search API key

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install julep yaml
```

## Configuration

The application requires the following API keys to be set up:

1. Julep AI API key (already configured in the code)
2. OpenWeatherMap API key (configured in `foodie_tour_workflow.yaml`)
3. Brave Search API key (configured in `foodie_tour_workflow.yaml`)

## Usage

1. Ensure all API keys are properly configured
2. Run the main script:
```bash
python foodie_tour_workflow.py
```

The script will:
1. Create a Foodie Tour Expert agent
2. Load the workflow configuration
3. Generate personalized food tours for the specified cities
4. Monitor the execution progress
5. Display the final results

## Input Parameters

The workflow accepts the following input parameters:

```python
{
    "cities": ["Tokyo", "Paris", "Barcelona", "Bangkok", "New York"],  # List of cities to generate tours for
    "preferences": {
        "dietary_restrictions": ["vegetarian"],  # Optional dietary restrictions
        "budget_preference": "mid-range"         # Budget preference (e.g., "budget", "mid-range", "luxury")
    }
}
```

## Output

The workflow generates detailed food tours for each city, including:
- Weather-appropriate dining recommendations
- Iconic local dishes
- Restaurant suggestions
- Meal timing and logistics
- Engaging narratives for each dining experience

## Workflow Process

1. Collects weather data for each city
2. Researches local dishes and traditional foods
3. Finds top-rated restaurants with those local dishes
4. Combines all data sources
5. Generates personalized food tours
6. Formats and presents the final results


