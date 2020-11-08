const pathname = window.location.pathname.split("/");

if (pathname[2] && pathname[2] === "editar") {
  const dia = document.getElementById("dia");

  (function () {
    let optionsDate = {
      day: "2-digit",
      month: "2-digit",
      year: "numeric",
    };

    let optionsHour = {
      hour: "2-digit",
      minute: "2-digit",
    };

    const date = new Date().toLocaleDateString("fr-CA", optionsDate);
    const time = new Date().toLocaleTimeString("pt-BR", optionsHour);

    dia.value = date + "T" + time;

    $("#telefone_cliente").mask("(99) 99999-9999");
  })();
}

function apagarVisita(id) {
  const confirmar = confirm("Tem certeza que deseja apagar esse registro?");

  if (confirmar === true) {
    window.location.href = `/visitas/apagar/${id}`;
  }
}
