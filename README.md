This repos contains three assignments done during the couerse INTRO-TO-AI. All of the assignments done in the python language and touches the following topics.<br/>
(You invited to review each assignment requirements in its pdf file):<br/>
Assignment1 - This assignment touches state-space search and heuristic planning: modeling a problem as states + goal + operators (cube spin and sub-tower flip with unit cost),<br/>
implementing A* search with OPEN/CLOSED sets and duplicate detection, <br/>
and designing/optimizing admissible heuristics (a base heuristic based on adjacent-cube color-pair compatibility with the goal, <br/>
plus an improved “advanced” heuristic that keeps optimality while improving runtime).<br/>

Assignment5 - This assignment covers reinforcement learning and MDPs by implementing Q-Learning (Bellman Q-table update, ε-greedy action selection, episode training)<br/>
to solve Gymnasium’s Cliff Walking environment, (See more - https://gymnasium.farama.org/environments/toy_text/cliff_walking/)<br/>
and implementing Value Iteration (computing Q-values, iterating to convergence) to solve a modified Gambler’s problem with two-dice outcome probabilities,<br/>
producing the optimal value function and policy and validating via the provided experiment scripts/plots.<br/>

Agentic-AI-work - This notebook covers agentic AI with a local LLM (Ollama + Llama 3.2) using LangChain/LangGraph, defines MCP/FastMCP tools,<br/>
wraps an A* heuristic search solver as a callable tool, builds a tool-using agent graph, and runs a comparison test of “agent with tools vs. without tools” on a color-blocks search problem.

