from googlesearch import search

def collect_urls(query, num_results=10):
    try:
        return list(search(query, num_results=num_results))
    except Exception as e:
        print(f"❌ Error during Google search: {e}")
        return []
