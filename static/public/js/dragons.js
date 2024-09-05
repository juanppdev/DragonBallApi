fetch("https://www.dragonballapi.com/dragons")
  .then(response => {
    if (!response.ok) {
      throw new Error('La respuesta de la red no fue válida');
    }
    return response.json();
  })
  .then(data => {
    console.log(data); // Aquí puedes manejar los datos de la respuesta


    const content = document.querySelector("#content");

        // Itera sobre los datos y crea elementos HTML
        data.forEach((dato) => {
            const div = document.createElement("div");
            div.className = "max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700";

            // Crea el contenido del elemento
            div.innerHTML = `
                <div class="bg-white">
                    <a href="https://www.dragonballapi.com/dragons/${dato.id}">
                        <img class="rounded-t-lg" src="${dato.image}" alt="" />
                    </a>
                </div>
                <div class="p-5">
                    <a href="https://www.dragonballapi.com/dragons/${dato.id}">
                        <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">${dato.name}</h5>
                    </a>
                </div>
            `;

            // Agrega el elemento al contenedor
            content.appendChild(div);
        });

  })
  .catch(error => {
    console.error('Error:', error);
  });