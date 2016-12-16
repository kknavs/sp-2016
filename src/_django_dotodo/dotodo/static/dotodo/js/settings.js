document.addEventListener("DOMContentLoaded", function() {
    settingsChange();
});

function settingsChange() {
    //document.getElementsByTagName("form").style.display = "none";
    document.getElementById("formNotifications").style.display = "none";
    document.getElementById("formEmail").style.display = "none";
    document.getElementById("formPassword").style.display = "none";
    var x = document.getElementById("settingsChange").value;
    document.getElementById("form"+x).style.display = "block";
}