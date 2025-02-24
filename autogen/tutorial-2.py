# %% [markdown]
"""
# Advanced Example 1: Multi-Agent Collaborative Gunpla Design with Memory & Iterative Feedback

In this demonstration, multiple agents collaborate in a custom Gunpla design project:
- **GroupChatManager:** Coordinates a design discussion.
- **Role-based Delegation:** Agents assume roles such as Concept Designer and Structural Engineer.
- **Function Calling:** Agents simulate external API integration for part compatibility.
- **Memory & Iterative Feedback:** A memory-enabled agent captures feedback to refine the design.
"""

# %%
from autogen import GroupChatManager, DesignAgent, CompatibilityAgent, MemoryEnabledAgent

# Initialize advanced design agents with memory for iterative improvements
concept_designer = DesignAgent(name='ConceptDesigner', role='Concept Art')
structural_engineer = DesignAgent(name='StructuralEngineer', role='Structural Analysis')
compatibility_checker = CompatibilityAgent(name='PartChecker')
design_manager = MemoryEnabledAgent(name='DesignManager', memory_enabled=True)

# Set up multi-agent collaboration
group_chat = GroupChatManager()
group_chat.add_agent(concept_designer)
group_chat.add_agent(structural_engineer)
group_chat.add_agent(compatibility_checker)
group_chat.add_agent(design_manager)

# Start the initial design discussion
initial_prompt = "Design a custom Gunpla model that combines the agility of the RX-78-2 with modern aesthetics."
discussion = group_chat.start_discussion(topic=initial_prompt)
print("Initial Group Discussion Output:")
print(discussion)

# Simulate function calling: Check compatibility between parts
part1 = "RX-78-2 Gundam torso"
part2 = "Zaku II arm"
compatibility_result = compatibility_checker.check_compatibility(part1, part2)
print(f"\nCompatibility Check between '{part1}' and '{part2}':")
print(compatibility_result)

# Iterative improvement using memory
iteration_feedback = design_manager.remember("Based on the compatibility check, consider reinforcing joint areas for durability.")
print("\nDesign Manager Iteration Feedback:")
print(iteration_feedback)

# Continue discussion incorporating feedback
refined_prompt = "Integrate feedback to reinforce joint areas and improve overall durability in the custom Gunpla design."
refined_discussion = group_chat.continue_discussion(topic=refined_prompt)
print("\nRefined Group Discussion Output:")
print(refined_discussion)

# %% [markdown]
"""
# Advanced Example 2: Asynchronous Agent Communication and Scheduling

In this example, we simulate asynchronous communication between agents using Python's asyncio. The agents concurrently perform tasks such as data collection, design generation, and compatibility checking.
"""

# %%
import asyncio
from autogen import AsyncDesignAgent, AsyncCompatibilityAgent, AsyncDataAgent

async def async_collect_data(topic):
    data_agent = AsyncDataAgent(name='AsyncDataCollector')
    return await data_agent.collect_data_async(topic)

async def async_generate_design():
    design_agent = AsyncDesignAgent(name='AsyncDesigner', role='Concept')
    return await design_agent.generate_design_async("Design a futuristic Gunpla model.")

async def async_check_compatibility():
    compat_agent = AsyncCompatibilityAgent(name='AsyncPartChecker')
    return await compat_agent.check_compatibility_async("RX-78-2 Gundam head", "Zaku II sensor")

async def main_async():
    tasks = [
        async_collect_data("Latest Gunpla parts trends"),
        async_generate_design(),
        async_check_compatibility()
    ]
    data, design, compatibility = await asyncio.gather(*tasks)
    
    print("\nAsynchronous Data Collection Output:")
    print(data)
    print("\nAsynchronous Design Generation Output:")
    print(design)
    print("\nAsynchronous Compatibility Check Output:")
    print(compatibility)

asyncio.run(main_async())

# %% [markdown]
"""
# Advanced Example 3: Integration with External APIs for Real-Time Part Information

This example simulates integration with an external Gunpla parts API. The agent retrieves real-time part pricing and availability, then uses Autogen to verify compatibility and suggest kitbashing options.
"""

# %%
import requests
from autogen import APIIntegrationAgent

def fetch_part_info(part_name):
    # Simulated API call to a Gunpla parts database (replace with a real API call as needed)
    api_url = f"https://api.gunpla-parts.example.com/info?part={part_name}"
    # response = requests.get(api_url)
    # For demonstration, we simulate a response:
    response = {"part": part_name, "price": "$29.99", "availability": "In Stock"}
    return response

api_agent = APIIntegrationAgent(name='GunplaAPIIntegrator')
part_name = "RX-78-2 Gundam torso"
part_info = fetch_part_info(part_name)
print("External API Part Info:")
print(part_info)

from autogen import CompatibilityAgent
compat_agent = CompatibilityAgent(name='PartCompatibilityAgent')
other_part = "Zaku II arm"
compatibility = compat_agent.check_compatibility(part_name, other_part)
print(f"\nCompatibility between '{part_name}' and '{other_part}':")
print(compatibility)

# %% [markdown]
"""
# Advanced Example 4: Advanced Debugging and Self-Correction with Agent Introspection

This example shows an agent that reviews its own output and suggests corrections. It simulates a self-reflection mechanism to identify potential design flaws and adjust its output.
"""

# %%
from autogen import SelfReviewAgent

review_agent = SelfReviewAgent(name='DesignReviewer')
initial_design = "The Gunpla model features a sleek design with standard joints, but lacks reinforced armor details."
print("Initial Design Output:")
print(initial_design)

correction = review_agent.self_review(initial_design)
print("\nAgent Correction and Self-Improvement Suggestion:")
print(correction)

# %% [markdown]
"""
# Advanced Example 5: Automated Pipeline – Data Collection, Analysis, and Report Generation

In this pipeline, agents work together to:
1. Collect data on Gunpla trends.
2. Analyze the data.
3. Generate a comprehensive report with insights and recommendations.
"""

# %%
from autogen import DataAgent, AnalysisAgent, ReportAgent

data_agent = DataAgent(name='PipelineDataCollector')
analysis_agent = AnalysisAgent(name='DataAnalyzer')
report_agent = ReportAgent(name='FinalReportCompiler')

# Step 1: Data Collection
data = data_agent.collect_data(topic="Emerging Gunpla trends in 2025")
print("Collected Data:")
print(data)

# Step 2: Data Analysis
analysis = analysis_agent.analyze(data)
print("\nData Analysis Output:")
print(analysis)

# Step 3: Report Generation
report = report_agent.compile_report(analysis)
print("\nFinal Report:")
print(report)

# %% [markdown]
"""
# Advanced Example 6: Dynamic Role Assignment and Adaptive Agent Behavior

This example demonstrates how an agent can dynamically change roles during a conversation. The agent starts with one role, then adapts its behavior based on new task requirements.
"""

# %%
from autogen import AdaptiveAgent

adaptive_agent = AdaptiveAgent(name='FlexibleAgent', role='Initial Research')
initial_task = "Collect information on high-durability Gunpla materials."
result_initial = adaptive_agent.perform_task(initial_task)
print("Initial Task Result:")
print(result_initial)

adaptive_agent.change_role('Material Analysis')
new_task = "Analyze the durability data and suggest improvements."
result_new = adaptive_agent.perform_task(new_task)
print("\nAfter Role Change, New Task Result:")
print(result_new)

# %% [markdown]
"""
# Advanced Example 7: Multi-Step Conversation with Context Preservation

This example shows how an agent maintains context over a multi-step conversation, refining its output with each new input while preserving previous context.
"""

# %%
from autogen import ContextualAgent

context_agent = ContextualAgent(name='ContextKeeper', memory_enabled=True)

conversation = context_agent.start_conversation("What are some innovative Gunpla assembly techniques?")
print("Conversation Step 1:")
print(conversation)

conversation = context_agent.continue_conversation("Can you provide details on using micro-soldering techniques in assembly?")
print("\nConversation Step 2:")
print(conversation)

conversation = context_agent.continue_conversation("How can these techniques be applied to improve joint durability?")
print("\nConversation Step 3:")
print(conversation)

# %% [markdown]
"""
# Advanced Example 8: Simulated Agent Negotiation for Resource Allocation

This example simulates a negotiation between agents to allocate limited resources (e.g., rare Gunpla parts) among competing design proposals.
"""

# %%
from autogen import NegotiationAgent, ResourceAllocator

agent_A = NegotiationAgent(name='DesignProposalA')
agent_B = NegotiationAgent(name='DesignProposalB')
allocator = ResourceAllocator(name='ResourceManager')

resources = {"RarePartX": 5, "LimitedEditionPartY": 3}

proposal_A = agent_A.propose_resource_allocation(request={"RarePartX": 3, "LimitedEditionPartY": 2})
proposal_B = agent_B.propose_resource_allocation(request={"RarePartX": 2, "LimitedEditionPartY": 2})

allocation = allocator.allocate(resources, [proposal_A, proposal_B])
print("Resource Allocation Outcome:")
print(allocation)
