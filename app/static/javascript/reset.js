async function resetFormHandler(event) {
    event.preventDefault();
  
    //Get the password from the user's input.
    const password = document.querySelector('#reset-password').value.trim();
    const confirmPassword = document.querySelector('#confirm-password').value.trim();
  
    //If two passwords match, submit form.
    if (password === confirmPassword) {
      //RESET WITH TOKEN
      const response = await fetch(`${window.location.pathname}`, {
        method: 'post',
        body: JSON.stringify({
          password
        }),
        headers: { 'Content-Type': 'application/json' }
      });
  
      //Then, notify user of success or failure of password change.
      if (response.ok) {
        console.log(response);
        alert(`Password successfully changed`);
      } else {
        alert(`Something went wrong when changing passwords.`);
      }
    } else {
        alert("Passwords do not match.");
    }
}
  
//Add these handlers to the login/sign up forms
document.querySelector('.reset-form').addEventListener('submit', resetFormHandler);
  