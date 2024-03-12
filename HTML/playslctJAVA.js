// JavaScript to change card colors gradually
const cards = document.querySelectorAll('.card');

cards.forEach((card, index) => {
    const circle1 = card.querySelector('.circle:nth-child(1)');
    const circle2 = card.querySelector('.circle:nth-child(2)');
    
    // Random initial colors
    let color1 = getRandomColor();
    let color2 = getRandomColor();

    // Set initial colors
    circle1.style.background = color1;
    circle2.style.background = color2;

    // Update colors gradually
    setInterval(() => {
        color1 = getRandomColor();
        color2 = getRandomColor();
        circle1.style.background = color1;
        circle2.style.background = color2;
    }, 2000); // Change colors every 2 seconds
});

// Function to generate random color
function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

window.addEventListener('DOMContentLoaded', function() {
    const body = document.body;
    const footer = document.querySelector('footer');

    function checkScroll() {
        if (body.offsetHeight <= window.innerHeight) {
            footer.style.display = 'block';
        } else {
            footer.style.display = 'none';
        }
    }

    window.addEventListener('resize', checkScroll);
    window.addEventListener('scroll', checkScroll);

    checkScroll(); // Check on page load
});
