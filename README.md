# AI Debate Simulator (Multi LLM Interaction Experiment)

## Overview

This project explores how different LLM providers behave when placed in a reasoning setting rather than a single prompt Q&A scenario.

I built a small command line debate engine where two models argue opposing sides of a topic, respond to each other across multiple rounds, and a third model judges the winner.

The goal was not to build a chatbot, but to observe:

* reasoning stability across turns
* persuasion vs correctness tradeoffs
* how models react to direct criticism
* how structured prompts influence behavior

The system currently uses:

* OpenAI (gpt-4.1-mini)
* Anthropic (claude-3-haiku)

---

## How It Works

For a given topic:

1. Opening arguments:
   Each model receives the same topic but opposite positions.

2. Rebuttal rounds (2 turns):
   Each model responds directly to the other model’s previous argument.

3. Judgment:
   A neutral judge model evaluates clarity, logic, factuality, and persuasion.

4. Logging:
   The full debate is stored as structured JSON for analysis.

This creates repeated interaction instead of a single generation call.

---

## Example Run

```
python debate/main.py "Should companies move to a 4 day work week?"
```

Output shows the debate live in the terminal and saves a full record to `/runs`.

---

## Installation

### Requirements

Python 3.10+

### Install dependencies

```
pip install -r requirements.txt
```

### Environment variables

Copy `.env.example` to `.env` and fill in your API keys:

```
OPENAI_API_KEY=your_key
ANTHROPIC_API_KEY=your_key
ROUNDS=2
```

---

## Project Structure

```
debate/
  main.py            -> CLI entry
  debate_engine.py   -> debate orchestration
  judge.py           -> winner evaluation
  logger.py          -> JSON logging

  providers/
    openai_provider.py
    anthropic_provider.py

  prompts/
    opening.py
    rebuttal.py
    judge.py
```

---

## Design Decisions

### 1) Provider Abstraction

Instead of hardcoding SDK calls, each model is wrapped behind a common interface.
This allowed me to swap providers without changing debate logic.

### 2) Multi Turn Interaction

Single prompts often hide weaknesses.
Debate forces models to:

* defend claims
* address criticism
* avoid repetition
* maintain internal consistency

This exposes behavioral differences much more clearly.

### 3) Structured Judging

The judge must return strict JSON.
This prevents vague “better answer” outputs and allows comparisons across runs.

### 4) Logging Every Run

Every debate is saved.
This enables later analysis such as:

* win rate
* consistency
* reasoning drift

---

## Running Multiple Topics

Simply run multiple times:

```
python debate/main.py "Should AI replace junior developers?"
python debate/main.py "Is remote work better than office work?"
python debate/main.py "Should college degrees be required for software jobs?"
```

Each run produces a JSON record.

---

## Future Extensions (Not Implemented Yet)

* automatic batch experiments
* cross model judging disagreement
* temperature comparison runs
* debate tournament mode

---

## Purpose of the Project

The intention was to move beyond prompt response testing and instead create an interaction environment where model behavior becomes observable and comparable.

This reveals much more about reliability than asking isolated questions.

---
