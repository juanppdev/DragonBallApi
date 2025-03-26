fetch("https://dragonballapp.vercel.app/dragonballz").then(response=>{if(!response.ok){throw new Error('La respuesta de la red no fue válida')}return response.json()}).then(data=>{console.log(data);const contenedor=document.querySelector("#contenedor");data.forEach((dato)=>{const div=document.createElement("div");div.className="max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700";div.innerHTML=`
    <div class="bg-white">
        <a href="https://dragonballapp.vercel.app/dragonballz/${dato.id }">
            <img class="rounded-t-lg" src="${dato.image }" alt="" />
        </a>
    </div>
    <div class="p-5">
        <a href="https://dragonballapp.vercel.app/dragonballz/${dato.id }">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">${dato.name }</h5>
        </a>
        <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
            Genero: ${dato.genre }
        </p>
        <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
            Raza: ${dato.race }
        </p>
        <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
            Planeta: ${dato.planet }
        </p>
    </div>
`;contenedor.appendChild(div)})}).catch(error=>{console.error('Error:',error)});