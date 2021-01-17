async function deleteFormHandler(event) {
  event.preventDefault();

  //Get the ID of the post to be deleted.
  const id = window.location.toString().split('/')[
    window.location.toString().split('/').length - 1
  ];
  const response = await fetch(`/api/posts/${id}`, {
    method: 'DELETE'
  });

  //Then, redirect to the dashboard or notify of error.
  if (response.ok) {
    document.location.replace('/dashboard/');
  } else {
    alert(response.statusText);
  }
}

//Add this handler to the delete post button.
document.querySelector('.delete-post-btn').addEventListener('click', deleteFormHandler);
