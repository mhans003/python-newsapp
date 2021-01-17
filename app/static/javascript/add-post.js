async function newFormHandler(event) {
  event.preventDefault();

  //Get the information to be sent over to create the new post.
  const title = document.querySelector('input[name="post-title"]').value;
  const post_url = document.querySelector('input[name="post-url"]').value;

  //Using data, send request to post.
  const response = await fetch(`/api/posts`, {
    method: 'POST',
    body: JSON.stringify({
      title,
      post_url
    }),
    headers: {
      'Content-Type': 'application/json'
    }
  });

  //Then, redirect to the dashobard, or notify of error.
  if (response.ok) {
    document.location.replace('/dashboard');
  } else {
    alert(response.statusText);
  }
}

//Add this function to the new post form.
document.querySelector('.new-post-form').addEventListener('submit', newFormHandler);
