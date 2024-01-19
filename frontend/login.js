let register_btn = document.querySelector(".Register-btn");
let login_btn = document.querySelector(".Login-btn");
let form = document.querySelector(".Form-box");
register_btn.addEventListener("click", () => {
  form.classList.add("change-form");
});
login_btn.addEventListener("click", () => {
  form.classList.remove("change-form");
});
function auth(){
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  if(email=="admin@gmail.com" && password=="admin123"){
    window.location.assign("index2.html");
    alert("login Successfully: ");

  }
  else{
    alert("incorrect information");
    return;
  }
}