function apagarImovel(id) {
    const confirmar = confirm("Tem certeza que deseja apagar esse registro?");
  
    if (confirmar === true) {
      window.location.href = `/imoveis/apagar/${id}`;
    }
  }