async function upvoteClickHandler(event) {
  event.preventDefault();

  //Get the ID of the post to upvote.
  const id = window.location.toString().split('/')[
    window.location.toString().split('/').length - 1
  ];
  //Send over the post ID via request body.
  const response = await fetch('/api/posts/upvote', {
    method: 'PUT',
    body: JSON.stringify({
      post_id: id
    }),
    headers: {
      'Content-Type': 'application/json'
    }
  });

  //Then, reload or alert error.
  if (response.ok) {
    document.location.reload();
  } else {
    alert(response.statusText);
  }
}

//Add this handler to the button to upvote.
document.querySelector('.upvote-btn').addEventListener('click', upvoteClickHandler);
