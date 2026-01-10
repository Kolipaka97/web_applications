function loadEmployees() {
  fetch("http://localhost:5000/employees")
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById("list");
      list.innerHTML = "";
      data.forEach(e => {
        list.innerHTML += `<li>${e.name} - ${e.department || ""}</li>`;
      });
    });
}
