function loadEmployees() {
  fetch("http://backend:5000/employees")
    .then(response => {
      if (!response.ok) {
        throw new Error("Failed to fetch employees");
      }
      return response.json();
    })
    .then(data => {
      const list = document.getElementById("list");
      list.innerHTML = "";

      data.forEach(emp => {
        const li = document.createElement("li");
        li.textContent = `${emp.id} - ${emp.name} (${emp.role})`;
        list.appendChild(li);
      });
    })
    .catch(error => {
      console.error("Error:", error);
      alert("Could not load employees");
    });
}
