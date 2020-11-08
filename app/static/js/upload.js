const docImovel = document.getElementById("doc_imovel");
const docProprietario = document.getElementById("doc_proprietario");
const capa = document.getElementById("capa");
const fotoInterior = document.getElementById("foto_interior");
const modalFoto = document.getElementById("modalFoto");

let pdfImovel = null;
let pdfProprietario = null;

docImovel.addEventListener("change", function () {
  const alert = document.getElementById("alert_doc_imovel");
  const button = document.getElementById("salvar_doc_imovel");
  const buttonView = document.getElementById("visualizar_doc_imovel");

  if (handleUpload(alert, button, buttonView, this)) {
    pdfImovel = this.files[0];
    buttonView.setAttribute("onclick", "visualizarDoc('docImovel')");
    return;
  }

  pdfImovel = null;
  buttonView.removeAttribute("onclick");
});

docProprietario.addEventListener("change", function () {
  const alert = document.getElementById("alert_doc_proprietario");
  const button = document.getElementById("salvar_doc_proprietario");
  const buttonView = document.getElementById("visualizar_doc_proprietario");

  if (handleUpload(alert, button, buttonView, this)) {
    pdfProprietario = this.files[0];
    buttonView.setAttribute("onclick", "visualizarDoc('docProprietario')");
    return;
  }

  pdfProprietario = null;
  buttonView.removeAttribute("onclick");
});

capa.addEventListener("change", function () {
  const alert = document.getElementById("alert_capa");
  const button = document.getElementById("salvar_capa");
  const buttonView = document.getElementById("visualizar_capa");

  handleUpload(alert, button, buttonView, this);
});

fotoInterior.addEventListener("change", function () {
  const alert = document.getElementById("alert_foto_interior");
  const button = document.getElementById("salvar_foto_interior");
  const buttonView = document.getElementById("visualizar_foto_interior");

  handleUpload(alert, button, buttonView, this);
});

function handleUpload(alert, button, buttonView, input) {
  alert.innerHTML = "";

  // verifica se possui algum arquivo no input
  if (!input.files || !input.files[0]) {
    button.setAttribute("disabled", "disabled");
    buttonView.setAttribute("disabled", "disabled");
    return;
  }

  // recupera o tamanho do arquivo e converte para kB
  const size = input.files[0].size / 1000;

  if (size > 2048) {
    alert.innerHTML = "Tamanho máximo 2MB";
    button.setAttribute("disabled", "disabled");
    buttonView.setAttribute("disabled", "disabled");
    return;
  }

  button.removeAttribute("disabled");
  buttonView.removeAttribute("disabled");

  return true;
}

// abre o PDF em nova aba
function visualizarDoc(file = null, filename = null) {
  let pdfURL = null;

  if (file) {
    switch (file) {
      case "docImovel":
        pdfURL = URL.createObjectURL(pdfImovel);
        window.open(pdfURL, "_blank");
        break;
      case "docProprietario":
        pdfURL = URL.createObjectURL(pdfProprietario);
        window.open(pdfURL, "_blank");
        break;
    }
  }

  if (filename) {
    window.open("/static/uploads/docs/" + filename, "_blank");
  }
}

// carrega a foto no modal
function visualizarFoto(idElement = null, path = null) {
  const photo = document.getElementById("photo");

  if (idElement) {
    const input = document.querySelector(idElement);

    let reader = new FileReader();

    reader.onload = function (event) {
      photo.setAttribute("src", event.target.result);
    };
    reader.readAsDataURL(input.files[0]);
  }

  if (path) {
    photo.setAttribute("src", "/static/uploads/" + path);
  }

  $("#modalFoto").modal("show");
}
