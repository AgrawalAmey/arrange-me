from flask import Flask, request, redirect, url_for, jsonify, render_template
import json
from multiprocessing import Process, Queue

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')


@app.route('/proccess_bookmarks', methods=['POST'])
def proccess_bookmarks():
    content = request.get_json(silent=True)
    print content
    return "hello"
    # queue = Queue()
    # p = Process(target=get_segments_fork, args=(queue, img_url, './static/'))
    # p.start()
    # p.join()
    # pictures = queue.get()


app.run(debug=True)
