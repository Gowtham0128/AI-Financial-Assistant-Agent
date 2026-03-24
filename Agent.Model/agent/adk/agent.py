# File agent.py

import asyncio
import json
from typing import Any

from dotenv import load_dotenv
from google.adk.agents.llm_agent import LlmAgent
from google.adk.artifacts.in_memory_artifact_service import (
    InMemoryArtifactService,  # Optional
)
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
# from google.adk.tools.mcp_tool.mcp_toolset import (
#     MCPToolset,
#     SseServerParams,
# )
from google.genai import types
from rich import print

# Import Google Search tool
from google.adk.tools.google_search_tool import google_search
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StreamableHTTPConnectionParams

load_dotenv()

# async def get_tools_async():
#     """Gets tools from the File System MCP Server."""
#     tools, exit_stack = await MCPToolset.from_server(
#         connection_params=SseServerParams(
#             url="http://localhost:8001/sse",
#         )
#     )
#     print("MCP Toolset created successfully.")
#     return tools, exit_stack

def get_agent_async():
    """Creates an ADK Agent equipped with tools from the MCP Server, including Google Search."""
    # mcp_tools, exit_stack = await get_tools_async()
    # print(f"Fetched {len(mcp_tools)} tools from MCP server.")

    # Combine MCP tools with Google Search
    # all_tools = mcp_tools + [google_search] # Add Google Search here

    toolset = MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
            url = "http://localhost:8080/mcp/stream"
            )
        )

    root_agent = LlmAgent(
        model="gemini-2.0-flash", # Consider 'gemini-2.0-flash-001' if you specifically need that version
        name="assistant",
        instruction="""
You are a comprehensive financial assistant with access to various specialized tools and the ability to search the web for information.

Your primary goal is to help users with their financial inquiries, leveraging your internal tools and Google Search as needed.

Here are the specialized Fi MCP Tools & Functions for Each Agent Goal:

Wealth Strategist
- get_net_worth() – returns total assets and liabilities breakdown
- get_goals_status() – retrieves user financial goals and progress (e.g., retirement)
- simulate_projection(years) – projects future net worth based on savings/investment trends

Portfolio Manager
- get_holdings() – fetches current asset holdings: mutual funds, stocks, FDs, gold, etc.
- get_transactions(asset_type, date_range) – retrieves transaction history per asset
- get_asset_performance(asset_type) – returns returns metrics: XIRR, CAGR, YTD performance

Tax Optimizer
- get_income_sources() – fetch income inflows from salary, dividends, etc.
- get_tax_documents() – fetch Form 16, Form 26AS data (salary, tax deducted)
- get_eligible_deductions() – identifies available tax-saving instruments under relevant sections

Behavioral Coach
- get_expense_summary(period) – spends per category (groceries, rent, subscriptions)
- get_savings_rate(month) – percent of income saved
- get_spending_trends() – tracks impulse/recurring spends over time

Smart Marketplace
- get_credit_profile() – returns credit score, eligibility data
- get_preferred_product_matches(profile) – recommendation API for loans, credit cards, SIPs
- get_recommended_SIPs(goal, risk) – tailored mutual fund SIP suggestions

Anomaly Watchdog
- get_duplicate_transactions() – flags repeated charges
- get_fraud_alerts() – flags suspicious transaction patterns
- monitor_transactions(stream=true) – webhook or real-time transaction monitoring

Conversational Agent
All above get_* tools are exposed as interactive LLM-readable tool calls
Also: get_contextual_info(user_query) to support chat queries like “What’s my balance?”

AutoPilot Executor (if execution allowed)
- schedule_SIP_execution(sip_details) – schedules recurring investments
- execute_bill_payment(bill_id) – triggers payment (if write-access supported)
- rebalance_portfolio(target_allocation) – rebalances assets automatically

Consent Governor
- get_consent_status(agent_id) – checks whether user has granted permission to agent
- revoke_access(agent_id) – programmatically revoke agent access
- list_active_sessions() – audit trail of agent connections

Doc Intelligence Agent
- parse_form16(document_blob) – extracts salary, TDS, PAN etc.
- parse_26AS(document_blob) – extracts tax credits and payments
- extract_document_data(doc_type, file) – generic parser for salary slips, bank statements

Simulation Engine
- simulate_scenario(inputs) – e.g., job change, increased expenses, early retirement
- get_scenario_outcome(scenario_id) – provides net worth projection or expense impact

Use Google Search (Google Search tool) to answer general knowledge questions, look up definitions, or find external information not covered by your financial tools. *Always prioritize using your specialized financial tools when the query directly relates to financial data or actions.*
        """,
        # tools=all_tools, # Pass the combined list of tools
        tools = [toolset]
    )
    return root_agent

root_agent = get_agent_async()
