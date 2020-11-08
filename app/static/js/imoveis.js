function apagarImovel(id) {
  const confirmar = confirm("Tem certeza que deseja apagar esse registro?");

  if (confirmar === true) {
    window.location.href = `/imoveis/apagar/${id}`;
  }
}

function apagarFotoInterior(idImovel, id) {
  const confirmar = confirm("Tem certeza que deseja apagar essa foto?");

  if (confirmar === true) {
    window.location.href = `/imoveis/informacoes/${idImovel}/foto_interior/apagar/${id}`
  }
}