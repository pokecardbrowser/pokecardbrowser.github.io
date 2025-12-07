const overlay = document.getElementById("previewOverlay");
const previewImg = document.getElementById("previewImg");
const closeBtn = document.querySelector(".close");
const themeOpener = document.getElementById("themeOpener");
const downloadSetJson = document.querySelector(".downloadSetJson");
let currentTheme = Cookies.get("currentTheme") || "1";

function setTheme(themeId) {
    document.body.style.backgroundImage = `url('/img/backgrounds/background${themeId}.png')`;
    Cookies.set("currentTheme", themeId, {expires: 365});
};

themeOpener.addEventListener("click", () => {
    window.location.href = "/themes/";
});

try {
    downloadSetJson.addEventListener("click", () => {
        const a = document.createElement("a");
        const setId = window.location.pathname.split('/').filter(Boolean).pop();
        a.href = `./${setId}.json`;
        a.download = `${setId}.json`;
        document.body.appendChild(a);
        a.click();
        a.remove();
    });
} catch {};

try {
    const themeDisplays = document.querySelectorAll(".themeDisplay");
    themeDisplays.forEach(themeDisplay => {
        themeDisplay.addEventListener("click", () => {
            themePath = themeDisplay.src;
            themeId = parseInt(themePath.match(/background(\d+)\.png/)[1], 10);
            setTheme(themeId);
        });
    });
} catch {};

try {
    previewTypes = ["card", "template"];
    previewTypes.forEach(type => {
        document.querySelectorAll(`.${type}`).forEach(item => {
            item.addEventListener("click", () => {
                previewImg.src = item.src;
                overlay.style.display = "flex";
            });
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
} catch {};

if (window.location.pathname == "/") {
    const hideScrollbar = document.createElement("style");
    hideScrollbar.textContent = `
::-webkit-scrollbar {
    display: none;
};
    `;
    document.body.appendChild(hideScrollbar);
};


setTheme(currentTheme);
