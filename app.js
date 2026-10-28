const tugma = document.getElementById("rejim");
const sahifa = document.body;
const sarlavha = document.getElementById("sarlavha");

tugma.addEventListener("click", function () {
    sahifa.classList.toggle("qora-fon");

    // Matnni tekshirib o'zgartiramiz
    if (sahifa.classList.contains("qora-fon")) {
        sarlavha.textContent = "Qora rejimdamiz (Dark Mode)";
        tugma.textContent = "Oq rejimga o'tish";
    } else {
        sarlavha.textContent = "Oq rejimdamiz";
        tugma.textContent = "Qora rejimga o'tish";
    }
});

