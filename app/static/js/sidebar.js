(function () {
  const pathname = window.location.pathname.split("/")[1];
  const sidebarItems = document.getElementsByClassName("side-item");

  switch (pathname) {
    case "corretores":
      sidebarItems[0].classList.add("side-item-active");
      break;
    case "imoveis":
      sidebarItems[1].classList.add("side-item-active");
      break;
    case "visitas":
      sidebarItems[2].classList.add("side-item-active");
      break;
    case "configuracoes":
      sidebarItems[3].classList.add("side-item-active");
      break;
  }
})();