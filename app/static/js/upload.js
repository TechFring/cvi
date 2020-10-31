const capa = document.getElementById("capa");
const alertCapa = document.getElementById("alert-capa");
const salvarFoto = document.getElementById("salvar_foto");
const modalFoto = document.getElementById("modalFoto");

capa.addEventListener("change", function () {
  alertCapa.innerHTML = "";

  // verifica se possui algum arquivo no input
  if (!this.files || !this.files[0]) {
    salvarFoto.setAttribute("disabled", "disabled");
    return;
  }

  // recupera o tamanho do arquivo e converte para kB
  const size = this.files[0].size / 1000;

  if (size > 2048) {
    alertCapa.innerHTML = "Tamanho máximo 2MB";
    salvarFoto.setAttribute("disabled", "disabled");
    return;
  }

  salvarFoto.removeAttribute("disabled");
});

// abrir modal
$("#modalFoto").on("shown.bs.modal", function () {
  if (capa.files[0]) handlePhoto(capa);
});

// carrega a foto no modal
function handlePhoto(input) {
  let reader = new FileReader();
  const photo = document.getElementById("photo");

  reader.onload = function (event) {
    photo.setAttribute("src", event.target.result);
  };

  reader.readAsDataURL(input.files[0]);
}
