function loadEmployees() {
  fetch("/api/employees")
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById("list");
      list.innerHTML = "";
      data.forEach(e => {
        list.innerHTML += `<li>${e.name} - ${e.role}</li>`;
      });
    });
}
