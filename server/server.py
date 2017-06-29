from flask import Flask, request, redirect, url_for, jsonify, render_template
from multiprocessing import Process, Queue
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup
from urllib2 import urlopen
import json

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')


@app.route('/proccess_bookmarks', methods=['POST'])
def recieve_bookmarks():
    bookmark_tree = request.get_json(silent=True)
    queue = Queue()
    p = Process(target=process_bookmarks, args=(queue, bookmark_tree))
    p.start()
    p.join()
    pictures = queue.get()
    return "Hello"

def process_bookmarks(server_queue, bookmark_tree):
    urls = []
    get_urls(bookmark_tree, urls)
    pages = fetch_pages(urls)
    print urls
    print pages

def get_urls(bookmark_tree, urls):
    for bookmark in bookmark_tree:
        if 'url' in bookmark:
            urls.append(bookmark['url'])

        if 'children' in bookmark:
            get_urls(bookmark['children'], urls)

def fetch_pages(urls):
    results = ThreadPool(20).imap_unordered(fetch_page, urls)
    return results

def fetch_page(url):
    try:
        response = urlopen(url)
        return {'url': url, 'page': response.read(), 'error': None}
    except Exception as e:
        return {'url': url, 'page': None, 'error': e}




app.run(debug=True)
