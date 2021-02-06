async function loginFormHandler(event) {
  event.preventDefault();

  //Get the email and password from the user's input.
  const email = document.querySelector('#email-login').value.trim();
  const password = document.querySelector('#password-login').value.trim();

  //If there is an email and password are entered, send the credentials.
  if (email && password) {
    await fetch('/api/users/login', {
      method: 'post',
      body: JSON.stringify({
        email,
        password
      }),
      headers: { 'Content-Type': 'application/json' }
    })
    .then(response => {
      if(response.ok) {
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
}

async function signupFormHandler(event) {
  event.preventDefault();

  //Get the new credentials from the user.
  const username = document.querySelector('#username-signup').value.trim();
  const email = document.querySelector('#email-signup').value.trim();
  const password = document.querySelector('#password-signup').value.trim();

  //As long as there are values to send, send over the new user's credentials.
  if (username && email && password) {
    await fetch('/api/users', {
      method: 'post',
      body: JSON.stringify({
        username,
        email,
        password
      }),
      headers: { 'Content-Type': 'application/json' }
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
}

//Add these handlers to the login/sign up forms
document.querySelector('.login-form').addEventListener('submit', loginFormHandler);
document.querySelector('.signup-form').addEventListener('submit', signupFormHandler);
