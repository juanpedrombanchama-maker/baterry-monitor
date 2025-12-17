
function actualizarFavicon(estado) {
    let favicon = 'favicon_full.png';
    if (estado === 'none') {
        favicon = 'favicon_none.png';
    } else if (estado < 20) {
        favicon = 'favicon_low.png';
    } else if (estado < 60) {
        favicon = 'favicon_medium.png';
    }

    const link = document.querySelector("link[rel~='icon']");
      if (link) {
        link.href = `/static/images/${favicon}?v=${Date.now()}`;
    }
}

function actualizar() {
    fetch('/nivel')
        .then(res => res.json())
        .then(data => {
            const contenedor = document.getElementById('contenedor-baterias');
            contenedor.innerHTML = '';

            const ids = Object.keys(data);
            if (ids.length === 0) {
                contenedor.innerHTML = '<p style="font-size: 20px; color: #666;">⚠️ No hay baterías conectadas</p>';
                actualizarFavicon("none");
                return;
          }

        let porcentajeMinimo = 100;

        for (const [id, datos] of Object.entries(data)) {
        const porcentaje = parseFloat(datos.porcentaje.toFixed(1));
        const voltaje = datos.voltaje.toFixed(2);

            if (porcentaje < porcentajeMinimo) {
              porcentajeMinimo = porcentaje;
            }

            const color = porcentaje > 75 ? '#4caf50' :
                          porcentaje > 40 ? '#ffeb3b' : '#f44336';

            const fondo = voltaje < 3.3 || voltaje > 4.2 ? '#ffe6e6' : '#f0f0f0';
            const alerta = porcentaje < 20 ? '<p style="color:#f44336;">⚠️ Batería baja</p>' : '';

            const bateriaHTML = `
              <div class="bateria-container" style="background-color: ${fondo};">
                <div class="bateria-nivel" style="width: ${porcentaje}%; background-color: ${color};"></div>
                <div class="bateria-tapita"></div>
              </div>
              <div class="texto" style="color: ${porcentaje < 20 ? '#f44336' : '#333'};">
                <strong>${id}</strong>: ${porcentaje}% (${voltaje} V)
                ${alerta}
              </div>
            `;

            contenedor.innerHTML += bateriaHTML;
          }

          actualizarFavicon(porcentajeMinimo);
        })
        .catch(err => {
          document.getElementById('contenedor-baterias').innerHTML = '<p>Error al obtener datos</p>';
          actualizarFavicon("none");
        });
    }

setInterval(actualizar, 1000);
function toggleMenu() {
    document.getElementById("miboton").classList.toggle("show");
  }

  // Cerrar el menú si se hace clic fuera
  window.onclick = function(event) {
    if (!event.target.matches('.boton')) {
      let dropdowns = document.getElementsByClassName("contenido");
      for (let i = 0; i < dropdowns.length; i++) {
        let openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }