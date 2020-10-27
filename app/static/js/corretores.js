function gerarSenha() {
  const senhaAleatoria = Math.random().toString(36).slice(-10);
  const senha = document.getElementById("senha");
  const label = document.querySelector("label[for='senha']");

  label.focus();
  senha.value = senhaAleatoria;
}

function apagarCorretor(id) {
  const confirmar = confirm('Tem certeza que deseja apagar esse registro?')

  if (confirmar === true) {
    window.location.href = `/corretores/apagar/${id}`
  }
}