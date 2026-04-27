# llamaindex-comparedge

Feeds SaaS pricing data into LlamaIndex from the ComparEdge API. SaaS pricing data — plans, features, ratings. No auth, no setup.

## Install

```bash
pip install llama-index-core requests
```

## Usage

```python
from comparedge_reader import ComparEdgeReader

# All products
reader = ComparEdgeReader()
docs = reader.load_data()

# Single category
reader = ComparEdgeReader(category="crm")
docs = reader.load_data()
```

## What you get

Each `Document` maps to one SaaS product:

| Field | Content |
|---|---|
| `text` | Name, description, pricing plans (plain text) |
| `metadata.slug` | URL-safe product identifier |
| `metadata.category` | Category slug (e.g. `project-management`) |
| `metadata.g2_rating` | G2 crowd rating (float or `None`) |
| `metadata.has_free_tier` | `True` / `False` |
| `metadata.url` | Canonical product page on comparedge.com |

## Categories

Categories available. Pass any slug to `category=`:

`accounting` · `ai-agents` · `ai-assistants` · `ai-coding` · `ai-image`
`ai-productivity` · `ai-video` · `ai-voice` · `ai-writing` · `cloud-hosting`
`crm` · `crypto-analytics` · `crypto-exchanges` · `crypto-portfolio-trackers`
`crypto-tax` · `crypto-telegram-bots` · `crypto-trading-bots` · `crypto-wallets`
`defi-tools` · `design-tools` · `dex` · `email-marketing` · `llm`
`password-managers` · `project-management` · `video-conferencing` · `vpn`
`website-builders`

## LlamaIndex integration

```python
from llama_index.core import VectorStoreIndex
from comparedge_reader import ComparEdgeReader

docs = ComparEdgeReader().load_data()
index = VectorStoreIndex.from_documents(docs)
query_engine = index.as_query_engine()

response = query_engine.query("Which CRM tools have a free tier under $50/month?")
print(response)
```

## API

No API key required. Data source: [ComparEdge API](https://comparedge-api.up.railway.app/api/v1)

Rate limits are generous for normal use. Batch all your products in one call rather than looping per product.

## License

MIT
