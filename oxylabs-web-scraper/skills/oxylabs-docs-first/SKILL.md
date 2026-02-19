---
name: oxylabs-docs-first
description: Prioritize repository docs as the primary source for Oxylabs API answers. Use when working in this repo on Oxylabs API questions, endpoint usage, parameters, request/response examples, scraper setup, or feature behavior. Trigger on requests that mention Oxylabs, API usage, or any file under docs/.
---

# Oxylabs Docs First

Use `docs/` as the source of truth for Oxylabs API behavior in this repository.
Resolve answers from `docs/` before relying on memory or generic external assumptions.

## Workflow

1. Identify relevant documentation files with:
```bash
rg --files docs
```

2. Narrow to likely matches with:
```bash
rg -n "<keyword|endpoint|parameter>" docs
```

3. Read the most relevant markdown files in `docs/` and synthesize the answer from those files.

4. Cite concrete file paths when answering, for example:
- `docs/oxylabs.getting.started.md`
- `docs/amazon.search.md`

5. If `docs/` does not contain the needed detail, state that explicitly and then provide the best inference.

## Guardrails

- Do not invent endpoint names, request fields, or pricing details.
- Prefer exact terminology from `docs/`.
- Keep answers scoped to repository docs when the question is about Oxylabs API usage in this repo.

## Coverage Hints

- Start with `docs/oxylabs.getting.started.md` for general setup and auth.
- Use `docs/amazon.*.md` files for Amazon-specific source endpoints and parameters.
