    // Mostrar el slide inicial
    showSlide(currentSlide);

    // Menú móvil
    const menuToggle = document.querySelector('.mobile-menu-toggle');
    const mainMenu = document.querySelector('.main-menu');

    if (menuToggle && mainMenu) {
        menuToggle.addEventListener('click', function () {
            const isActive = mainMenu.classList.toggle('active');
            menuToggle.textContent = isActive ? '✖' : '☰';
        });

        window.addEventListener('resize', function () {
            if (window.innerWidth > 768) {
                mainMenu.classList.remove('active');
                mainMenu.style.display = 'flex';
            } else {
                mainMenu.style.display = 'none';
            }
        });
    }

    // Scroll suave
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Animaciones en scroll
    const revealElements = document.querySelectorAll('.model-card, .about-content, .client-logo');

    function checkReveal() {
        const triggerBottom = window.innerHeight * 0.8;

        revealElements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            if (elementTop < triggerBottom) {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }
        });
    }

    revealElements.forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(20px)';
        element.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    });

    window.addEventListener('scroll', checkReveal);
    checkReveal(); // mostrar elementos visibles al cargar;
    
