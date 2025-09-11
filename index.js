const overlay = document.getElementById("previewOverlay");
const previewImg = document.getElementById("previewImg");
const closeBtn = document.querySelector(".close");

document.querySelectorAll(".card").forEach(card => {
    card.addEventListener("click", () => {
        previewImg.src = card.src;
        overlay.style.display = "flex";
    });
});

closeBtn.addEventListener("click", () => {
    overlay.style.display = "none";
});

overlay.addEventListener("click", (e) => {
    if (e.target === overlay) {
      overlay.style.display = "none";
    }
});