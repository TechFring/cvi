const senha = document.getElementById("senha");

function gerarSenha() {
  const senhaAleatoria = Math.random().toString(36).slice(-10);

  senha.value = senhaAleatoria;
  senha.focus();
}

function apagarCorretor(id) {
  const confirmar = confirm("Tem certeza que deseja apagar esse registro?");

  if (confirmar === true) {
    window.location.href = `/corretores/apagar/${id}`;
  }
}
