async function commentFormHandler(event) {
  event.preventDefault();

  //Get the new comment text and an ID to be sent over to database.
  const comment_text = document.querySelector('textarea[name="comment-body"]').value.trim();
  const post_id = window.location.toString().split('/')[
    window.location.toString().split('/').length - 1
  ];

  //As long as there is a comment to send, send the request.
  if (comment_text) {
    const response = await fetch('/api/comments', {
      method: 'POST',
      body: JSON.stringify({
        post_id,
        comment_text
      }),
      headers: {
        'Content-Type': 'application/json'
      }
    });

    //Then, reload the page, or alert of error.
    if (response.ok) {
      document.location.reload();
    } else {
      alert(response.statusText);
    }
  }
}

//Add this form handler to the comment form.
document.querySelector('.comment-form').addEventListener('submit', commentFormHandler);
