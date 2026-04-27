"""Usage examples for ComparEdgeReader."""

from comparedge_reader import ComparEdgeReader


def example_all_products():
    """Load every product in the database."""
    reader = ComparEdgeReader()
    docs = reader.load_data()
    print(f"Loaded {len(docs)} products")

    # Preview first doc
    d = docs[0]
    print("\n--- First document ---")
    print(d.text[:300])
    print("\nMetadata:", d.metadata)


def example_category():
    """Load a single category."""
    reader = ComparEdgeReader(category="project-management")
    docs = reader.load_data()
    print(f"\nProject-management tools: {len(docs)}")
    for d in docs[:10]:
        tier = "✓ free" if d.metadata["has_free_tier"] else "  paid"
        rating = d.metadata["g2_rating"] or "n/a"
        print(f"  {tier}  G2:{str(rating):<4}  {d.metadata['slug']}")


def example_free_tier_filter():
    """Filter to tools with free tiers."""
    reader = ComparEdgeReader()
    docs = reader.load_data()
    free = [d for d in docs if d.metadata["has_free_tier"]]
    print(f"\nProducts with free tier: {len(free)}/{len(docs)}")


def example_vector_index():
    """Build a simple VectorStoreIndex and run a query.

    Requires: pip install llama-index openai
    Set OPENAI_API_KEY before running.
    """
    try:
        from llama_index.core import VectorStoreIndex
    except ImportError:
        print("\nSkipping vector index example — llama-index not installed")
        return

    reader = ComparEdgeReader(category="project-management")
    docs = reader.load_data()
    print(f"\nBuilding index over {len(docs)} project-management tools...")

    index = VectorStoreIndex.from_documents(docs)
    engine = index.as_query_engine()

    q = "Which project management tools support Kanban boards and have a free tier?"
    print(f"Query: {q}")
    response = engine.query(q)
    print(f"Answer: {response}")


if __name__ == "__main__":
    example_all_products()
    example_category()
    example_free_tier_filter()
    example_vector_index()
