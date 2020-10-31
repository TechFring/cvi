const modal = document.getElementById("modalMap");
const inputLatitude = document.getElementById("latitude");
const inputLongitude = document.getElementById("longitude");
const endereco = document.getElementById("endereco");
const currentMarkers = [];

mapboxgl.accessToken =
  "pk.eyJ1IjoidGVjaGZyaW5nIiwiYSI6ImNrZ3V4b3prazAyNTEyc21vdXIyeWV2YTQifQ.aPhqON2EHBSlqf3tYxKTOA";

let map = new mapboxgl.Map({
  container: "map",
  style: "mapbox://styles/mapbox/streets-v11",
  center: [coordenadas.longitude, coordenadas.latitude],
  zoom: (coordenadas.defined) ? 13 : 8,
});

// adiciona opções de zoom no mapa
map.addControl(new mapboxgl.NavigationControl());

// caso as coordenadas já tenham sido definidas, adiciona o marcador
(function () {
  if (coordenadas.defined) {
    const marker = new mapboxgl.Marker()
      .setLngLat([coordenadas.longitude, coordenadas.latitude])
      .addTo(map);

    currentMarkers.push(marker);
  }
})();

// evento para adicionar marcador
map.on("click", function (event) {
  currentMarkers.forEach((item) => {
    item.remove();
  });

  coordenadas.longitude = event.lngLat.lng;
  coordenadas.latitude = event.lngLat.lat;

  const marker = new mapboxgl.Marker()
    .setLngLat([event.lngLat.lng, event.lngLat.lat])
    .addTo(map);

  currentMarkers.push(marker);
});

// abrir modal
$("#modalMap").on("shown.bs.modal", function () {
  map.resize();
});

async function preencherLatLng() {
  if (!coordenadas) return;

  const response = await fetch(
    `https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${coordenadas.latitude}&longitude=${coordenadas.longitude}&localityLanguage=pt`
  );

  const json = await response.json();

  endereco.value = json.locality + " - " + json.principalSubdivision;
  inputLatitude.value = coordenadas.latitude;
  inputLongitude.value = coordenadas.longitude;

  // ativando input
  endereco.focus();
  inputLatitude.focus();
  inputLongitude.focus();
}
