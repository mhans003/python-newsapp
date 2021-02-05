async function resetFormHandler(event) {
    event.preventDefault();
  
    //Get the password from the user's input.
    const password = document.querySelector('#reset-password').value.trim();
    const confirmPassword = document.querySelector('#confirm-password').value.trim();
  
    //If two passwords match, submit form.
    if (password === confirmPassword) {

      //RESET WITH TOKEN
      const response = await fetch('/reset', {
        method: 'post',
        body: JSON.stringify({
          password
        }),
        headers: { 'Content-Type': 'application/json' }
      });
  
      //Then, redirect to the user's dashboard or notify of error.
      if (response.ok) {
        //document.location.replace('/dashboard/');
        alert(`Email sent to ${email}. Check your inbox.`);
      } else {
        alert("Email not found. Try refreshing the page or entering another email address.");
      }
    } else {
        alert("Passwords do not match.");
    }
}
  
//Add these handlers to the login/sign up forms
document.querySelector('.reset-form').addEventListener('submit', resetFormHandler);
  