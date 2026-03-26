// login page js code
let messageEl = document.querySelector(".message");
let addInfoEl = document.querySelector(".add-info");
let newUserInfo = document.querySelector(".new-user-info");

setTimeout(() => {
  if (messageEl) {
    messageEl.style.display = "none";
    messageEl.style.transition = "opacity 1s";
  }
}, 5000);

// end of login js code
setTimeout(() => {
  if (addInfoEl) {
    addInfoEl.style.display = "none";
    addInfoEl.style.transition = "opacity 1s";
  }
}, 5000);

setTimeout(() => {
  if (newUserInfo) {
    newUserInfo.style.display = "none";
    newUserInfo.style.transition = "opacity 1s";
  }
}, 5000);
