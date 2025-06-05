from julep import Client
import yaml
import time
import os

# Initialize Julep client
client = Client(api_key=os.getenv("JULEP_API_KEY"))

OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
BRAVE_API_KEY = os.getenv("BRAVE_API_KEY")

# Create the agent
agent = client.agents.create(
    name="Foodie Tour Expert",
    model="claude-3.5-sonnet",
    about="An expert culinary guide specializing in weather-informed dining experiences"
)

# Load and create the task
with open('foodie_tour_workflow.yaml', 'r', encoding='utf-8') as file:
    task_definition = yaml.safe_load(file)

task = client.tasks.create(
    agent_id=agent.id,
    **task_definition
)

# Execute the workflow
execution = client.executions.create(
    task_id=task.id,
    input={
        "cities": ["Patna", "Mumbai", "Delhi", "Kolkata", "Chennai"],
        "preferences": {
            "dietary_restrictions": ["vegetarian"],
            "budget_preference": "mid-range"
        }
    }
)



# Monitor execution progress
while (result := client.executions.get(execution.id)).status not in ['succeeded', 'failed']:
    print(f"Status: {result.status}")
    time.sleep(2)

# Display results
if result.status == "succeeded":
    print("Foodie Tour Generated Successfully!")
    # Write results to output.txt
    with open('sample_output.txt', 'w', encoding='utf-8') as f:
        f.write(str(result.output['complete_tours']))
else:
    print(f"Execution failed: {result.error}")
