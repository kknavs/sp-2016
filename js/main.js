document.addEventListener("DOMContentLoaded", function() {

    document.getElementById("reset").addEventListener("click", resetPassword);

    var password = document.getElementById("password")
        , confirm_password = document.getElementById("repassword");

    function validatePassword(){
        if(password.value != confirm_password.value) {
            confirm_password.setCustomValidity("Passwords don't match.");
        } else {
            confirm_password.setCustomValidity('');
        }
    }

    password.onchange = validatePassword;
    confirm_password.onkeyup = validatePassword;

    function resetPassword(event){
        event.preventDefault();
        // TODO: call to server
        document.getElementById("resetNote").style.visibility = "visible";
    }
});
