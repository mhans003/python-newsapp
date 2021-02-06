async function deleteFormHandler(event) {
  event.preventDefault();

  //Get the ID of the post to be deleted.
  const id = window.location.toString().split('/')[
    window.location.toString().split('/').length - 1
  ];
  await fetch(`/api/posts/${id}`, {
    method: 'DELETE'
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

//Add this handler to the delete post button.
document.querySelector('.delete-post-btn').addEventListener('click', deleteFormHandler);
