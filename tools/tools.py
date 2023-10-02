
from langchain.utilities import SerpAPIWrapper
# from langchain.utilities.serpapi_wrapper import SerpAPIWrapper


from langchain.utilities import SerpAPIWrapper


class CustomSerpAPIWrapper(SerpAPIWrapper):
    def __init__(self):
        super(CustomSerpAPIWrapper, self).__init__()

    @staticmethod
    def _process_response(res: dict) -> str:
        """Process response from SerpAPI."""
        if "error" in res.keys():
            raise ValueError(f"Got error from SerpAPI: {res['error']}")
        if "answer_box" in res.keys() and "answer" in res["answer_box"].keys():
            toret = res["answer_box"]["answer"]
        elif "answer_box" in res.keys() and "snippet" in res["answer_box"].keys():
            toret = res["answer_box"]["snippet"]
        elif (
            "answer_box" in res.keys()
            and "snippet_highlighted_words" in res["answer_box"].keys()
        ):
            toret = res["answer_box"]["snippet_highlighted_words"][0]
        elif (
            "sports_results" in res.keys()
            and "game_spotlight" in res["sports_results"].keys()
        ):
            toret = res["sports_results"]["game_spotlight"]
        elif (
            "knowledge_graph" in res.keys()
            and "description" in res["knowledge_graph"].keys()
        ):
            toret = res["knowledge_graph"]["description"]
        elif "snippet" in res["organic_results"][0].keys():
            toret = res["organic_results"][0]["link"]

        else:
            toret = "No good search result found"
        return toret

def get_profile_url(name: str):
  """ Searches for Linkedin profile Page. """
  search = SerpAPIWrapper()
  res = search.run(f"{name}")
  return res
#from serpapi import GoogleSearch
#
#
#def get_profile_url(name: str):
#    """ Searches for Linkedin profile Page. """
#    # Create an instance of GoogleSearchResults
#    serp = GoogleSearchResults()
#
#    # Define the search query (e.g., searching for a LinkedIn profile by name)
#    query = f"LinkedIn {name}"
#
#    # Set search parameters (optional)
#    params = {
#        "q": query,
#        "location": "United States",  # Optional: Specify the location
#    }
#
#    # Execute the search
#    serp.search(query=query, params=params)
#
#    # Get the search results
#    results = serp.get_dict()
#
#    # Process and use the search results as needed
#    # For example, you can return the first search result URL
#    if 'organic_results' in results:
#        first_result = results['organic_results'][0]
#        return first_result.get('link', 'No LinkedIn profile found')
#    else:
#        return 'No LinkedIn profile found'

# Example usage:
linkedin_profile_url = get_profile_url("Edan Marco")
print(linkedin_profile_url)
