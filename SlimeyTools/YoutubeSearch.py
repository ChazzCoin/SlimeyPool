from youtubesearchpython import VideosSearch

TITLE_FILTER = "Official Video"

def search_youtube(searchTerm, limit=10):
    results = VideosSearch(searchTerm, limit=limit).result()
    results_list = results['result']
    search_results = []
    for r in results_list:
        temp = {
            'title': r['title'],
            'duration': r['duration'],
            'viewCount': r['viewCount']['text'],
            'link': r['link']
        }
        search_results.append(temp)
    return search_results
