import requests

def fetch_book_content(book_id):
    content_url = f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt"
    response = requests.get(content_url)

    if response.status_code == 200:
        return response.text  # Return the raw content
    else:
        raise Exception('Unable to fetch book content')  # Raise an exception to handle errors in routes

def fetch_book_metadata(book_id):
    metadata_url = f"https://www.gutenberg.org/ebooks/{book_id}"
    response = requests.get(metadata_url)

    if response.status_code == 200:
        return response.text  # Return the raw metadata
    else:
        raise Exception('Unable to fetch book metadata')