let form = document.querySelector(".block__send");
let input = document.querySelector(".text__send");
let list = document.querySelector(".list");

form.onsubmit = function (evt) {
    evt.preventDefault();
    let NewMessage = document.createElement("li");
    let NewText = document.createElement("p");
    let icon = document.createElement("i");
    icon.classList.add("fa");
    icon.classList.add("fa-user");
    NewText.textContent = input.value;
    NewMessage.append(NewText);
    NewMessage.append(icon);
    list.append(NewMessage);
    input.value = "";
};

let toggle = document.querySelector(".toggle");
toggle.onclick = function () {
    toggle.classList.toggle("toggle-on");
}