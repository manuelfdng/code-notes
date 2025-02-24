# %% [markdown]
"""
# Notebook 1: Introduction to Autogen with Gunpla Chatbot

In this section, we introduce the Autogen framework and build a simple Gunpla-themed Q&A chatbot. We will set up a `UserProxyAgent` and an `AssistantAgent` to answer Gunpla-related questions.
"""

# %%
# Import necessary modules from Autogen (ensure the autogen library is installed)
from autogen import UserProxyAgent, AssistantAgent

# Initialize agents
user_agent = UserProxyAgent(name='GunplaFan')
assistant_agent = AssistantAgent(name='GunplaExpert')

# Simulate a simple Q&A interaction
question = 'What are the best Gunpla kits for beginners?'
response = assistant_agent.answer(question)  # This method returns a Gunpla-related answer

print('User:', question)
print('Assistant:', response)

# %% [markdown]
"""
# Notebook 2: Multi-Agent Collaboration - Gunpla Research Team

In this section, we simulate a Gunpla research team. One agent will collect data on Gunpla kits while another compiles that data into a concise report.
"""

# %%
# Import the research and report agents from Autogen
from autogen import ResearchAgent, ReportAgent

# Initialize the agents
data_agent = ResearchAgent(name='DataCollector')
report_agent = ReportAgent(name='ReportCompiler')

# Simulate data collection on Gunpla kits
collected_data = data_agent.collect_data(topic='Gunpla kits for beginners')

# Compile the collected data into a report
report = report_agent.compile_report(collected_data)

print('Gunpla Research Report:')
print(report)

# %% [markdown]
"""
# Notebook 3: Gunpla Assembly Guide Generator

This section uses an AI assistant to generate step-by-step assembly guides for Gunpla models.
"""

# %%
# Import the GuideAgent from Autogen
from autogen import GuideAgent

# Initialize the guide agent
guide_agent = GuideAgent(name='AssemblyGuide')

# Specify the Gunpla model for which to generate an assembly guide
model = 'RX-78-2 Gundam'
guide = guide_agent.generate_assembly_guide(model)

print(f'Assembly guide for {model}:')
print(guide)

# %% [markdown]
"""
# Notebook 4: Debugging & Troubleshooting Gunpla Assembly

In this section, we build an AI troubleshooting assistant that can help diagnose common Gunpla assembly issues. The agent leverages conversation memory to track issues and suggest fixes.
"""

# %%
# Import the DebugAgent from Autogen
from autogen import DebugAgent

# Initialize the debug agent with memory enabled
debug_agent = DebugAgent(name='Troubleshooter', memory_enabled=True)

# Define a common issue for a Gunpla model
issue = 'Loose joint on RX-78-2 Gundam'
solution = debug_agent.troubleshoot(issue)

print('Troubleshooting Issue:')
print('Issue:', issue)
print('Suggested Solution:', solution)

# %% [markdown]
"""
# Notebook 5: Gunpla Kitbashing & Part Compatibility Checker

This section introduces the function-calling capabilities of Autogen. Build a kitbashing assistant that checks compatibility of different Gunpla parts and suggests customization ideas.
"""

# %%
# Import the CompatibilityAgent from Autogen
from autogen import CompatibilityAgent

# Initialize the kitbashing assistant
compat_agent = CompatibilityAgent(name='KitbashingAssistant')

# Define two Gunpla parts to check for compatibility
part1 = 'RX-78-2 Gundam torso'
part2 = 'Zaku II arm'

# Check compatibility between the parts
compatibility = compat_agent.check_compatibility(part1, part2)

print(f'Compatibility between "{part1}" and "{part2}": {compatibility}')

# %% [markdown]
"""
# Notebook 6: Multi-Agent Gunpla Design Team

In this section, we simulate a Gunpla design team using a `GroupChatManager`. Different agents are assigned specific roles (e.g., Concept Artist, Engineer, Customizer) and collaborate to design a custom Gunpla.
"""

# %%
# Import the necessary classes from Autogen
from autogen import GroupChatManager, DesignAgent

# Initialize the group chat manager and design agents
group_chat = GroupChatManager()

designer1 = DesignAgent(name='ConceptArtist', role='Design')
designer2 = DesignAgent(name='Engineer', role='Structural Analysis')
designer3 = DesignAgent(name='Customizer', role='Kitbashing')

# Add the agents to the group chat
group_chat.add_agent(designer1)
group_chat.add_agent(designer2)
group_chat.add_agent(designer3)

# Simulate a group discussion to design a custom Gunpla
discussion = group_chat.start_discussion(topic='Design a custom Gunpla model')
print('Group Discussion Output:')
print(discussion)

# %% [markdown]
"""
# Notebook 7: Gunpla Build Log Assistant

This section demonstrates how to use Autogen to help track the progress of your Gunpla build. An AI assistant creates and manages a checklist so you can keep track of each build step.
"""

# %%
# Import the TaskTrackerAgent from Autogen
from autogen import TaskTrackerAgent

# Initialize the build log assistant
build_log_agent = TaskTrackerAgent(name='BuildLogAssistant')

# Define a list of build tasks
tasks = [
    'Assemble frame',
    'Attach armor details',
    'Apply panel lining',
    'Paint and weather the model'
]

# Create a checklist using the assistant
build_log_agent.create_checklist(tasks)

print('Current Gunpla Build Checklist:')
print(build_log_agent.get_checklist())

# %% [markdown]
"""
# Notebook 8: Gunpla Maintenance & Repair Assistant

In this section, we build an AI-powered repair assistant that diagnoses issues with your Gunpla (such as misaligned parts or painting errors) and suggests fixes.
"""

# %%
# Import the RepairAgent from Autogen
from autogen import RepairAgent

# Initialize the repair agent
repair_agent = RepairAgent(name='MaintenanceAssistant')

# Define a common maintenance issue
problem = 'Misaligned armor on RX-78-2 Gundam'
repair_suggestion = repair_agent.diagnose_and_repair(problem)

print('Maintenance Issue:')
print('Problem:', problem)
print('Repair Suggestion:', repair_suggestion)

# %% [markdown]
"""
# Notebook 9: Gunpla Storytelling & Diorama Assistant

This section shows how to use Autogen’s creative capabilities. An AI storyteller generates custom lore for Gunpla dioramas and custom builds, enriching your projects with backstories and epic narratives.
"""

# %%
# Import the StoryAgent from Autogen
from autogen import StoryAgent

# Initialize the storytelling agent
story_agent = StoryAgent(name='GunplaStoryteller')

# Define a diorama theme for the narrative
diorama_theme = 'Epic battle in a post-apocalyptic city'
story = story_agent.generate_story(theme=diorama_theme)

print('Generated Gunpla Lore:')
print(story)

# %% [markdown]
"""
# Notebook 10: Deploying Autogen in a Gunpla-Themed Web App

In the final section, we deploy our Gunpla assistant as a web application using FastAPI for the backend and Streamlit for the UI. This demonstrates how to take your AI assistant into production.
"""

# %%
# Import the WebAppAgent from Autogen and Streamlit for the UI
from autogen import WebAppAgent
import streamlit as st

# Initialize the web app agent
web_agent = WebAppAgent(name='GunplaWebAssistant')

def main():
    st.title('Gunpla Assistant Web App')
    st.write('Ask your Gunpla-related questions below:')
    
    # User input
    user_query = st.text_input('Enter your question:')
    
    if user_query:
        # Process the query using the web app agent
        response = web_agent.handle_query(user_query)
        st.write('Response:')
        st.write(response)

if __name__ == '__main__':
    main()
