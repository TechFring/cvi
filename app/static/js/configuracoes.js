const switchPassword = document.getElementById("switchPassword");
const inputSenha = document.getElementById("senha");
const groupSenha = document.getElementById("groupSenha");

switchPassword.addEventListener("change", function () {
  if (this.checked) {
    inputSenha.setAttribute("required", "required");
    groupSenha.classList.remove("d-none");
  } else {
    inputSenha.removeAttribute("required");
    groupSenha.classList.add("d-none");
    inputSenha.value = "";
  }
});
