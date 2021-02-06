async function newFormHandler(event) {
  event.preventDefault();

  //Get the information to be sent over to create the new post.
  const title = document.querySelector('input[name="post-title"]').value;
  const post_url = document.querySelector('input[name="post-url"]').value;

  //Using data, send request to post.
  await fetch(`/api/posts`, {
    method: 'POST',
    body: JSON.stringify({
      title,
      post_url
    }),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => {
    if (response.ok) {
      document.location.replace('/dashboard');
    } else {
      //If the response is not OK, reload in order to view flash error message.
      document.location.reload();
    }
    return response.text();
  })
  .then(text => {
    console.log(JSON.parse(text));
  })
  .catch(error => {
    console.log(error);
  });
}

//Add this function to the new post form.
document.querySelector('.new-post-form').addEventListener('submit', newFormHandler);
