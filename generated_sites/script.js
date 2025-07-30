
// Modern JavaScript enhancements
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Add loading animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in-up');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    document.querySelectorAll('section, .card, .feature').forEach(el => {
        observer.observe(el);
    });
    
    // Add hover effects to interactive elements
    document.querySelectorAll('.btn, .card, .hover-effect').forEach(element => {
        element.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        element.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
});



// Smooth scrolling for all internal navigation links (anchors)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault(); // Prevent default jump behavior

        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);

        if (targetElement) {
            // Scroll smoothly to the target element
            targetElement.scrollIntoView({
                behavior: 'smooth'
            });
        }

        // Close mobile navigation menu if it's open after clicking a link
        const nav = document.querySelector('.nav');
        const navToggle = document.getElementById('nav-toggle');
        if (nav.classList.contains('active')) {
            nav.classList.remove('active');
            navToggle.setAttribute('aria-expanded', 'false'); // Update ARIA attribute
        }
    });
});

// Header scroll effect: Add 'scrolled' class when scrolled down
const header = document.querySelector('.header');
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) { // If scrolled more than 50px from top
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});

// Mobile navigation toggle (hamburger menu functionality)
const navToggle = document.getElementById('nav-toggle');
const nav = document.querySelector('.nav');

navToggle.addEventListener('click', () => {
    // Toggle 'active' class on nav for styling (e.g., max-height for opening/closing)
    nav.classList.toggle('active');

    // Update ARIA-expanded attribute for accessibility
    const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
    navToggle.setAttribute('aria-expanded', String(!isExpanded));
});

// Intersection Observer for fade-in animations on scroll
// Select all elements that have an animation class
const animateOnScrollElements = document.querySelectorAll('.animated-fade-in-up, .animated-fade-in-left, .animated-fade-in-right');

// Configure the Intersection Observer options
const observerOptions = {
    root: null, // 'null' means the viewport is the root
    rootMargin: '0px',
    threshold: 0.1 // When 10% of the element is visible, trigger the callback
};

// Create a new Intersection Observer instance
const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            // If the element enters the viewport, allow its animation to play
            entry.target.style.animationPlayState = 'running';
            entry.target.classList.add('visible'); // Optional: Add a class for persistent visibility if needed
            observer.unobserve(entry.target); // Stop observing once the animation has played
        }
    });
}, observerOptions);

// Observe each element that should animate on scroll
animateOnScrollElements.forEach(el => {
    el.style.animationPlayState = 'paused'; // Pause animations by default so they don't play on load
    observer.observe(el);
});

// Active navigation link highlighting based on scroll position
// This enhances user experience by showing which section is currently in view
const sections = document.querySelectorAll('section[id]'); // Get all sections with an ID

window.addEventListener('scroll', () => {
    let currentActiveSectionId = ''; // Variable to hold the ID of the currently active section
    const scrollY = window.pageYOffset; // Current scroll position
    const headerHeight = header.offsetHeight; // Get height of fixed header for offset calculation

    sections.forEach(section => {
        // Calculate section's top and bottom boundaries, accounting for fixed header
        const sectionTop = section.offsetTop - headerHeight - 1; // -1 to ensure it triggers slightly before top
        const sectionHeight = section.clientHeight;

        // Check if the current scroll position is within this section's boundaries
        if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
            currentActiveSectionId = section.getAttribute('id');
        }
    });

    // Loop through all navigation links and apply/remove 'active' class
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active'); // Remove 'active' from all links first
        // If the link's href matches the current active section ID, add 'active' class
        if (link.getAttribute('href').includes(currentActiveSectionId)) {
            link.classList.add('active');
        }
    });
});

// Set the initial active state for the 'Home' link on page load
document.addEventListener('DOMContentLoaded', () => {
    const heroLink = document.querySelector('a[href="#hero"]');
    if (heroLink) {
        heroLink.classList.add('active');
    }
});