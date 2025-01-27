#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from ai1.crew import Ai1

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        "name": "Thomas Sulkiewicz",
        "email": "thomas@thomas.fm",
        "phone": "0498991000",
        "personal_writeup": """
        With over 20 years of experience in Information Technology I have worked
        in almost every facet of the industry, including solutions architecture
        and design, Microsoft/Linux systems engineering, software
        engineering/development, business process engineering, and
        people/process management. I particularly enjoy workshopping a new
        infrastructure solution and then keeping watch over it as its being
        built.

        My strengths and key technologies are:

        -   Overseeing the architecture/high-level design and implementation of
            infrastructure projects.

        -   Developing infrastructure solutions, specialising network
            infrastructure.

        -   A technical understanding of how infrastructure technologies work
            and how to best put them to use.

        -   Understanding design principles and best practices around network
            infrastructure and systems development

        -   Troubleshooting technical issues related to new and existing
            infrastructure solutions

        My current goals are to continue to provide technical leadership,
        guidance and oversight to infrastructure delivery projects.
        """,
    "job_posting_url": "https://www.seek.com.au/job/81525135?ref=search-standalone&type=standard&origin=jobTitle#sol=cab886ddb0c1d7f330e6314ce37dcfaadd12eb97"
    }
    
    try:
        Ai1().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "job_posting_url": "https://www.seek.com.au/job/81525135?ref=search-standalone&type=standard&origin=jobTitle#sol=cab886ddb0c1d7f330e6314ce37dcfaadd12eb97"
    }
    try:
        Ai1().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Ai1().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Ai1().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
