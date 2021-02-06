async function resetFormHandler(event) {
    event.preventDefault();
  
    //Get the password from the user's input.
    const password = document.querySelector('#reset-password').value.trim();
    const confirmPassword = document.querySelector('#confirm-password').value.trim();
  
    //If two passwords match, submit form.
    if (password === confirmPassword) {
      //RESET WITH TOKEN
      await fetch(`${window.location.pathname}`, {
        method: 'post',
        body: JSON.stringify({
          password
        }),
        headers: { 'Content-Type': 'application/json' }
      })
      .then(response => {
        if (response.ok) {
          document.location.replace('/');
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
    } else {
      alert('Those passwords do not match.');
    }
}
  
//Add these handlers to the login/sign up forms
document.querySelector('.reset-form').addEventListener('submit', resetFormHandler);
