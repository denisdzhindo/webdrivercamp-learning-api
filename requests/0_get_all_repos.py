import requests
'''
Send a GET request to 
https://api.github.com/search/repositories?q=webdrivercamp-learning-python 
where parameter q - the search keywords
Print the response status code
Print total_count of found items from response
Return a list of items from response sorted by full_name (the dict key in each item)
'''
def get_repos(url):
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        list_ = data.get('items', [])  # Get the list of repositories under 'items', if there is no 'items' -> []
        list_of_items_sorted = sorted(list_, key=lambda x: x['full_name'].lower())
        return list_of_items_sorted, response.status_code
    else:
        print(f"Error code: {response.status_code}")
        return [], response.status_code  # Return empty list and status code in case of an error


if __name__ == "__main__":

    wlp_url = "https://api.github.com/search/repositories?q=webdrivercamp-learning-python"
    list_of_items, status_code = get_repos(wlp_url)

    print(f"\nResponse status code: {status_code}")
    print(f"Total count of found items: {len(list_of_items)}")
    print()

    for element in list_of_items:
        user = element['owner']['login']  # Get the owner username
        repo = element['name']  # Get the repository name
        print(f"{user:20}", repo)
