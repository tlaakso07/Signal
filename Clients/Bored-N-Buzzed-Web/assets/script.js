document.addEventListener('DOMContentLoaded', () => {

    /* --- Day Highlighting Logic --- */
    const todayJS = new Date().getDay();
    const dealCards = document.querySelectorAll('.deal-card');

    if (todayJS >= 1 && todayJS <= 5) {
        dealCards.forEach(card => {
            if(card.getAttribute('data-day') == todayJS) {
                card.classList.add('active-day');
                const pill = card.querySelector('.pill-badge');
                if(pill && !pill.classList.contains('yellow-badge')) {
                    pill.textContent = "TODAY'S DROP";
                    pill.classList.add('yellow-badge');
                }
            }
        });
    } else {
        const weekendCard = document.querySelector('.highlight-card');
        if(weekendCard) {
            weekendCard.classList.add('active-day');
            const pill = weekendCard.querySelector('.pill-badge');
            if(pill) pill.textContent = "LIVE NOW";
        }
    }

    /* --- Scroll Reveal (Intersection Observer) --- */
    // Trigger reveals slightly before they come into screen
    const revealOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, revealOptions);

    document.querySelectorAll('.js-reveal').forEach(el => {
        revealObserver.observe(el);
    });

    // Remove pre-load state instantly so observer handles the rest
    setTimeout(() => {
         document.body.classList.remove('is-loading');
    }, 100);

    /* --- Advanced Mouse/Performance Check --- */
    const isTouchDevice = (('ontouchstart' in window) || (navigator.maxTouchPoints > 0));
    
    if (!isTouchDevice) {
        /* --- Setup Mouse Tracking Variables --- */
        const cursorDot = document.querySelector('.cursor-dot');
        const cursorRing = document.querySelector('.cursor-ring');
        const bgGlow = document.querySelector('.bg-glow');
        const parallaxWrap = document.querySelector('.parallax-wrap');
        const typography = document.querySelector('.massive-typography');

        let mouseX = window.innerWidth / 2;
        let mouseY = window.innerHeight / 2;
        
        // Smoothed positions for lag effect
        let ringX = mouseX;
        let ringY = mouseY;
        let glowX = mouseX;
        let glowY = mouseY;

        // Listen for mouse movement
        window.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
            
            // Instantly move the dot
            if(cursorDot) {
                cursorDot.style.transform = `translate(${mouseX}px, ${mouseY}px)`;
            }

            // Calculate parallax for Massive Typography
            // It will move slightly opposite to the mouse
            if(typography) {
                const speed = parseFloat(typography.getAttribute('data-parallax-speed')) || 0.05;
                const xOffset = (window.innerWidth / 2 - mouseX) * speed;
                const yOffset = (window.innerHeight / 2 - mouseY) * speed;
                typography.style.transform = `translate(${xOffset}px, ${yOffset}px)`;
            }
        });

        // Loop for smoothing cursor ring and bg glow
        function renderLoop() {
            // LERP for ring
            ringX += (mouseX - ringX) * 0.2;
            ringY += (mouseY - ringY) * 0.2;
            if(cursorRing) cursorRing.style.transform = `translate(${ringX}px, ${ringY}px)`;

            // LERP for glow (slightly slower)
            glowX += (mouseX - glowX) * 0.08;
            glowY += (mouseY - glowY) * 0.08;
            if(bgGlow) bgGlow.style.transform = `translate(${glowX - window.innerWidth/2}px, ${glowY - window.innerHeight/2}px)`;

            requestAnimationFrame(renderLoop);
        }
        renderLoop();

        /* --- Magnetic Hover States --- */
        const magnetics = document.querySelectorAll('.js-magnetic, a, button');
        
        magnetics.forEach(el => {
            el.addEventListener('mouseenter', () => {
                if(cursorRing) cursorRing.classList.add('cursor-hover');
            });
            el.addEventListener('mouseleave', () => {
                if(cursorRing) cursorRing.classList.remove('cursor-hover');
                // Reset any transform if we applied magnetic pull
                el.style.transform = '';
            });

            // Optional: true physics magnetic pull on elements
            el.addEventListener('mousemove', (e) => {
                if(!el.classList.contains('deal-card')) {
                    // Only apply physical pull to smaller items like CTAs
                    const rect = el.getBoundingClientRect();
                    const elCenterX = rect.left + rect.width / 2;
                    const elCenterY = rect.top + rect.height / 2;
                    
                    const pullX = (e.clientX - elCenterX) * 0.15;
                    const pullY = (e.clientY - elCenterY) * 0.15;
                    
                    el.style.transform = `translate(${pullX}px, ${pullY}px)`;
                }
            });
        });
    }
});
