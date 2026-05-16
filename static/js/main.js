document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.side-navbar .nav-link');
    const sections = document.querySelectorAll('.section');

    function updateActiveSection() {
        let currentSectionId = '';
        const scrollPosition = window.scrollY + 200; // Offset for detection

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                currentSectionId = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active-section');
            if (link.getAttribute('href') === `#${currentSectionId}`) {
                link.classList.add('active-section');
            }
        });
    }

    window.addEventListener('scroll', updateActiveSection);
    updateActiveSection(); // Initial check
});
