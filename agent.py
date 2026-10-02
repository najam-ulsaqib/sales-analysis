"""
Najam Career Agent
Version 0.1

This first version is intentionally simple.
It provides the foundation for future job-search,
application tracking, and professional automation.
"""

from datetime import datetime


OWNER = "Najam Ul Saqib"

TARGET_ROLES = [
    "Junior Data Analyst",
    "Data Analyst",
    "Data Analyst Intern",
    "MIS Analyst",
    "Reporting Analyst",
    "BI Analyst",
    "Junior BI Analyst",
    "Data Associate",
    "Data Executive",
    "Reporting Executive",
]


def show_status():
    """Display the current career-agent status."""

    print("=" * 50)
    print("NAJAM CAREER AGENT")
    print("=" * 50)

    print(f"Owner: {OWNER}")
    print("Current objective: Become job-ready for entry-level Data Analyst roles.")
    print("Career path: Data Analytics → Data Science → ML → Data Engineering → AI")

    print("\nTarget roles:")
    for role in TARGET_ROLES:
        print(f"- {role}")

    print(f"\nAgent started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\nStatus: READY")


if __name__ == "__main__":
    show_status()