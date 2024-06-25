fetch("https://apidragonball.vercel.app/dragonballz")
  .then(response => {
    if (!response.ok) {
      throw new Error('La respuesta de la red no fue válida');
    }
    return response.json();
  })
  .then(data => {
    console.log(data.id); // Aquí puedes manejar los datos de la respuesta
  })
  .catch(error => {
    console.error('Error:', error);
  });