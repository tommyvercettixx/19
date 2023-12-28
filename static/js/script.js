
document.addEventListener("DOMContentLoaded", function () {
    const searchForm = document.getElementById("searchForm");
    const searchInput = document.getElementById("searchInput");
    const resultsContainer = document.getElementById("resultsContainer");
  
    searchForm.addEventListener("submit", function (e) {
      e.preventDefault();
      const searchTerm = searchInput.value;
  
      fetch("/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ search:  searchTerm}),
      })
        .then((response) => response.json())
        .then((data) => displayResults(data))
        .catch((error) => console.error("Error:", error));
  
        searchInput.placeholder = searchInput.value;
    });
  
    function displayResults(results) {
      resultsContainer.innerHTML = "";
  
      if (results.length === 0) {
        resultsContainer.innerHTML = `<p class='fs-1 text-center mt-5' >User <span class="text-decoration-underline text-warning">${searchInput.value}</span> not found.<br>Try again.</p>`;
      } else {
        results.forEach((user) => {
          resultsContainer.innerHTML += `
                <div class="card m-3 col-md-6" style="width: 30rem;">
                  <img src="${user.photo}" class='card-img-top' alt="${user.name}">
                  <div class="card-body">
                    <p class="card-title fs-3">Name: ${user.name}</p>
                    <p class="card-title fs-3">Age: ${user.age} </p>
                    <p class="card-title fs-3">City: ${user.city}</p>
                  </div>
                </div>`;
        });
      }
      searchInput.value = "";
    }
  });
  