async function editFormHandler(event) {
  event.preventDefault();

  //Get the title and ID of the article to be edited.
  const title = document.querySelector('input[name="post-title"]').value.trim();
  const id = window.location.toString().split('/')[
    window.location.toString().split('/').length - 1
  ];
  //Send the ID via URL params and the title via request body.
  const response = await fetch(`/api/posts/${id}`, {
    method: 'PUT',
    body: JSON.stringify({
      title
    }),
    headers: {
      'Content-Type': 'application/json'
    }
  });

  //Then, redirect to dashboard or notify of error.
  if (response.ok) {
    document.location.replace('/dashboard/');
  } else {
    alert(response.statusText);
  }
}

//Add the form to edit a post to the edit post form.
document.querySelector('.edit-post-form').addEventListener('submit', editFormHandler);
