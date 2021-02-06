async function editFormHandler(event) {
  event.preventDefault();

  //Get the title and ID of the article to be edited.
  const title = document.querySelector('input[name="post-title"]').value.trim();
  const id = window.location.toString().split('/')[
    window.location.toString().split('/').length - 1
  ];
  //Send the ID via URL params and the title via request body.
  await fetch(`/api/posts/${id}`, {
    method: 'PUT',
    body: JSON.stringify({
      title
    }),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => {
    if (response.ok) {
      document.location.replace('/dashboard/');
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

//Add the form to edit a post to the edit post form.
document.querySelector('.edit-post-form').addEventListener('submit', editFormHandler);
