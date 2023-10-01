const scrollingImage = document.getElementById('scrolling-image');
const stopPoint = 500; // Adjust this value to set the stopping point

window.addEventListener('scroll', () => {
    const imageRect = scrollingImage.getBoundingClientRect();
    const windowHeight = window.innerHeight;

    // Check if the image is in the viewport
    if (imageRect.bottom > 0 && imageRect.top < windowHeight) {
        // Calculate the new position for the image
        const scrollPosition = window.scrollY;
        let newPosition = scrollPosition * 0.15; // Adjust the speed of the scroll effect

        // Ensure the image stops moving after reaching the stopPoint
        if (newPosition > stopPoint) {
            newPosition = stopPoint;
        }

        // Apply the new position to the image
        scrollingImage.style.top = newPosition + 'px';
    }
});
