document.addEventListener('DOMContentLoaded', function () {
    chrome.bookmarks.getTree(process_bookmark);
});

function process_bookmark(bookmarks) {
    console.log(bookmarks);
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:5000/proccess_bookmarks',
        data: JSON.stringify(bookmarks),
        success: function (data) {
            alert('data: ' + data);
        },
        contentType: "application/json",
        dataType: 'json'
    });
}