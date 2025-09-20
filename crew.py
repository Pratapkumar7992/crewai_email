import yaml
from crewai import Agent, Task, Crew, Process
from helper import load_api_key

# Load API Key
api_key = load_api_key()

# Load YAML files
def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

agents_config = load_yaml("config/agents.yaml")
tasks_config = load_yaml("config/tasks.yaml")

# Create agents
drafter = Agent(
    config=agents_config["drafter_agent"],
    verbose=True
)
grammar = Agent(
    config=agents_config["grammar_agent"],
    verbose=True
)
polish = Agent(
    config=agents_config["polish_agent"],
    verbose=True
)
review = Agent(
    config=agents_config["review_agent"],
    verbose=True
)

# Create tasks
draft_task = Task(
    config=tasks_config["draft_task"],
    agent=drafter,
    verbose=True
)
grammar_task = Task(
    config=tasks_config["grammar_task"],
    agent=grammar,
    verbose=True
)
polish_task = Task(
    config=tasks_config["polish_task"],
    agent=polish,
    verbose=True
)
review_task = Task(
    config=tasks_config["review_task"],
    agent=review,
    verbose=True
)

# Create crew
crew = Crew(
    agents=[drafter, grammar, polish, review],
    tasks=[draft_task, grammar_task, polish_task, review_task],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("🚀 Running the Email Writing Crew...")
    result = crew.kickoff(
        inputs={
            "subject": "suffering from fever",
            "context": "i have fever so write an email to manager telling that i am suffered from fever so i am not able to come office today ."
        }
    )
    print("\n✅ Final Reviewed Email:\n")
    print(result)
