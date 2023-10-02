document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        hideLoadingOverlay();
    }, 2000);
});

function hideLoadingOverlay() {
    const loadingOverlay = document.querySelector(".loading-overlay");
    loadingOverlay.style.display = "none";
}

const scrollDisableDiv = document.querySelector('.scroll-disable');

scrollDisableDiv.addEventListener('mouseenter', () => {
    // Disable scrolling on hover
    document.body.style.overflow = 'hidden';
});

scrollDisableDiv.addEventListener('mouseleave', () => {
    // Re-enable scrolling when hover ends
    document.body.style.overflow = 'auto';
});
