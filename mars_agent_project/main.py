from search_agent import find_resources
from planner_agent import create_plan
from budget_agent import calculate_budget
from communication_agent import send_report
from memory_agent import remember_findings

print("🚀 Starting Mars Mission\n")

find_resources()
create_plan()
calculate_budget()
remember_findings()
send_report()

print("\n✅ Mission Complete")
