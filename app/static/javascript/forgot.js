async function forgotFormHandler(event) {
    event.preventDefault();
  
    //Get the password from the user's input.
    const email = document.querySelector('#forgot-email').value.trim();
  
    //If there is an email entered, send the credentials.
    if (email) {
      await fetch('/forgot', {
        method: 'post',
        body: JSON.stringify({
          email
        }),
        headers: { 'Content-Type': 'application/json' }
      })
      .then(response => {
        //Reload in order to view flash message.
        document.location.reload();
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
document.querySelector('.forgot-form').addEventListener('submit', forgotFormHandler);