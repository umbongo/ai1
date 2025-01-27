# Ai1 Crew

Welcome to the Ai1 Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/ai1/config/agents.yaml` to define your agents
- Modify `src/ai1/config/tasks.yaml` to define your tasks
- Modify `src/ai1/crew.py` to add your own logic, tools and specific args
- Modify `src/ai1/main.py` to add custom inputs for your agents and tasks

Agents
The following agents are defined in the project:

Researcher: Senior Tech Job Researcher

Goal: Do amazing analysis on job postings to help job applicants
Backstory: As a Job Researcher, your prowess in navigating and extracting critical information from job postings is unmatched.
Profiler: Personal Profiler for Engineers

Goal: Do incredible research on job applicants to help them stand out in the job market.
Backstory: Equipped with analytical prowess, you dissect and synthesize information from diverse sources to craft comprehensive personal and professional profiles.
Resume Strategist: Resume Strategist for Engineers

Goal: Find all the best ways to make a resume stand out in the job market.
Backstory: With a strategic mind and an eye for detail, you excel at refining resumes to highlight the most relevant skills and experiences.
Interview Preparer: Interview Preparer for Engineers

Goal: Create interview questions and talking points based on the resume and job requirements.
Backstory: You prepare candidates for interviews by creating tailored questions and talking points.
Tasks
The following tasks are defined in the project:

Profile Task:

Agent: Profiler
Description: Task for profiling job applicants.
Resume Strategy Task:

Agent: Resume Strategist
Description: Task for developing resume strategies.
Output: tailored_resume.md
Interview Preparation Task:

Agent: Interview Preparer
Description: Task for preparing interview materials.
Output: interview_materials.md
Tools
The project uses the following tools:

crewAI: Framework for creating and managing AI agents and tasks.
UV: Dependency management and package handling tool.
OpenAI API: For leveraging GPT models.
Serper API: For additional data and functionality.

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the ai1 Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The ai1 Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Ai1 Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
