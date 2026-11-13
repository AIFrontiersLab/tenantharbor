# Trade-offs

## Pre-Retrieval Filtering (Chosen)

- **Pros:** ['High security: Unauthorized docs never leave the DB.', 'Lower latency: Fewer documents to process in context assembly.', 'Cost-effective: Reduced token usage in LLM.']
- **Cons:** ['Requires vector DB to support efficient metadata filtering.', 'Complexity in mapping RBAC/ACLs to DB filters.']

## Post-Retrieval Filtering (Rejected)

- **Pros:** ['Easier to implement initially.', 'Works with any vector DB regardless of filter support.']
- **Cons:** ['Security risk: Unauthorized docs are retrieved and must be scrubbed.', 'Higher latency: Retrieving more docs than needed.', 'Higher cost: Wasted LLM tokens on filtered-out content.']

## Built-in vs learned scoring

The lexical reference scorer is deterministic and dependency-free; learned scorers improve relevance at the cost of latency, cost, and reproducibility.

## Degrade vs fail

Non-critical stages degrade to protect availability; policy and answer assembly fail to protect correctness.
