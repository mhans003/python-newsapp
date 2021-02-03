async function forgotFormhandler(event) {
    event.preventDefault();
  
    //Get the email from the user's input.
    const email = document.querySelector('#forgot-email').value.trim();
  
    //If there is an email entered, send the credentials.
    if (email) {
      const response = await fetch('/email/forgot', {
        method: 'post',
        body: JSON.stringify({
          email
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
    }
}
  
//Add these handlers to the login/sign up forms
document.querySelector('.forgot-form').addEventListener('submit', forgotFormhandler);
  