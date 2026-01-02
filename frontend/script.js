async function loadProjects() {
  const response = await fetch("https://api.pratikkabra.dev/projects"); // Production API endpoint (CloudForge backend)
  const data = await response.json();

  document.getElementById("output").textContent =
    JSON.stringify(data, null, 2);
}
