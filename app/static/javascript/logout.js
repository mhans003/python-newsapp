async function logout() {
  const response = await fetch('/api/users/logout', {
    method: 'post',
    headers: { 'Content-Type': 'application/json' }
  });

  //If the logout was successful, redirect to main page. Otherwise, notify of error.
  if (response.ok) {
    document.location.replace('/');
  } else {
    alert(response.statusText);
  }
}

//Add the logout function to the logout button.
document.querySelector('#logout').addEventListener('click', logout);
