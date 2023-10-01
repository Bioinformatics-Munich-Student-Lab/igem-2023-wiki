document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        hideLoadingOverlay();
    }, 2000);
});

function hideLoadingOverlay() {
    const loadingOverlay = document.querySelector(".loading-overlay");
    loadingOverlay.style.display = "none";
}
