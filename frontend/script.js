async function loadProjects() {
  const response = await fetch("http://127.0.0.1:5000/projects");
  const data = await response.json();

  document.getElementById("output").textContent =
    JSON.stringify(data, null, 2);
}
