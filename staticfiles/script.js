document.addEventListener("DOMContentLoaded", () => {
    /* 1. Fade-In Animation */
    const fadeElements = document.querySelectorAll('.fade-in');
    const isProjectPage = document.body.classList.contains("project-page");

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show');
                if (isProjectPage) observer.unobserve(entry.target);
            } else if (!isProjectPage) {
                entry.target.classList.remove('show');
            }
        });
    }, { threshold: 0.2 });
    fadeElements.forEach(el => observer.observe(el));

    /* 2. Desktop Carousel */
    const track = document.getElementById('sliderTrack');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');

    if (track && prevBtn && nextBtn) {
        const images = Array.from(track.querySelectorAll('.slider-img'));
        let currentIdx = images.findIndex(img => img.classList.contains('active'));
        if (currentIdx === -1) currentIdx = 0;

        function updateSlider() {
            images.forEach((img, i) => img.classList.toggle('active', i === currentIdx));
            const viewportWidth = track.parentElement.offsetWidth;
            const activeImage = images[currentIdx];
            const offset = (viewportWidth / 2) - (activeImage.offsetLeft + activeImage.offsetWidth / 2);
            track.style.transform = `translateX(${offset}px)`;
        }

        prevBtn.addEventListener('click', () => {
            currentIdx = currentIdx > 0 ? currentIdx - 1 : images.length - 1;
            updateSlider();
        });

        nextBtn.addEventListener('click', () => {
            currentIdx = currentIdx < images.length - 1 ? currentIdx + 1 : 0;
            updateSlider();
        });

        images.forEach((img, i) => img.addEventListener('click', () => {
            currentIdx = i;
            updateSlider();
        }));

        window.addEventListener('load', updateSlider);
        window.addEventListener('resize', updateSlider);
        updateSlider();
    }

    /* 3. Mobile Carousel (FIXED LOGIC) */
    const mobileTrack = document.getElementById('mobileTrack');
    const mobilePrev = document.getElementById('mobilePrev');
    const mobileNext = document.getElementById('mobileNext');
    const mobileCounter = document.getElementById('mobileCounter');

    if (mobileTrack && mobilePrev && mobileNext) {
        const slides = Array.from(mobileTrack.querySelectorAll('.mobile-slide'));
        let mobileIdx = 0;

        function updateMobile() {
            // Using 100% is better than pixels for responsiveness
            mobileTrack.style.transform = `translateX(-${mobileIdx * 100}%)`;
            if (mobileCounter) {
                mobileCounter.textContent = `${mobileIdx + 1} / ${slides.length}`;
            }
        }

        mobilePrev.addEventListener('click', () => {
            mobileIdx = (mobileIdx > 0) ? mobileIdx - 1 : slides.length - 1;
            updateMobile();
        });

        mobileNext.addEventListener('click', () => {
            mobileIdx = (mobileIdx < slides.length - 1) ? mobileIdx + 1 : 0;
            updateMobile();
        });

        // Optional: Swipe support
        let startX = 0;
        mobileTrack.addEventListener('touchstart', e => startX = e.touches[0].clientX);
        mobileTrack.addEventListener('touchend', e => {
            let endX = e.changedTouches[0].clientX;
            if (startX - endX > 50) mobileNext.click();
            if (endX - startX > 50) mobilePrev.click();
        });

        updateMobile();
        window.addEventListener('resize', updateMobile);
    }

    /* 4. Typing Effect */
    const typingElement = document.getElementById("typing");
    if (typingElement) {
        const texts = ["Hi, I am Prem", "A Passionate Python Developer"];
        let textIdx = 0, charIdx = 0, isDeleting = false;

        function typeEffect() {
            const currentText = texts[textIdx];
            typingElement.innerHTML = isDeleting
                ? currentText.substring(0, charIdx--)
                : currentText.substring(0, charIdx++);

            let speed = isDeleting ? 50 : 100;
            if (!isDeleting && charIdx === currentText.length + 1) {
                isDeleting = true; speed = 1500;
            } else if (isDeleting && charIdx === 0) {
                isDeleting = false;
                textIdx = (textIdx + 1) % texts.length;
                speed = 300;
            }
            setTimeout(typeEffect, speed);
        }
        typeEffect();
    }

    /* 5. Mobile Menu */
    const menuBtn = document.getElementById("menu-btn");
    const mobileMenu = document.getElementById("mobile-menu");
    if (menuBtn) {
        menuBtn.addEventListener("click", () => {
            mobileMenu.classList.toggle("active");
            menuBtn.classList.toggle("fa-bars");
            menuBtn.classList.toggle("fa-times");
        });
    }

    /* 6. Nav scroll effect */
    window.addEventListener("scroll", () => {
        const nav = document.querySelector("nav");
        if (nav) {
            nav.classList.toggle("scrolled", window.scrollY > 80);
        }
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function getTechIcon(tech) {
    switch (tech) {
        case "Python": return `<li><i class="devicon-python-plain"></i> Python</li>`;
        case "Django": return `<li><i class="devicon-django-plain"></i> Django</li>`;
        case "HTML5": return `<li><i class="devicon-html5-plain"></i> HTML5</li>`;
        case "CSS3": return `<li><i class="devicon-css3-plain"></i> CSS3</li>`;
        case "JavaScript": return `<li><i class="devicon-javascript-plain"></i> JavaScript</li>`;
        case "Flask": return `<li><i class="devicon-flask-original"></i> Flask</li>`;
        case "React": return `<li><i class="devicon-react-original"></i> React</li>`;
        case "Git": return `<li><i class="devicon-git-plain"></i> Git</li>`;
        case "DBMS": return `<li><i class="devicon-mysql-plain"></i> DBMS</li>`;
        case "AIML": return `<li><i class="fas fa-brain"></i> AIML</li>`;
        case "Twilio": return `<li><i class="fab fa-twilio"></i> Twilio</li>`;
        default: return `<li>${tech}</li>`;
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".filter-btn");

    buttons.forEach(btn => {
        btn.addEventListener("click", (e) => {
            e.preventDefault();

            // remove active from all <li>
            document.querySelectorAll(".domain-filters li")
                .forEach(li => li.classList.remove("active"));

            // add active to clicked button's parent <li>
            btn.parentElement.classList.add("active");

            fetchProjects(); // 🔥 now works correctly
        });
    });

    // initial load
    fetchProjects();
});

async function fetchProjects() {
    const selectedBtn = document.querySelector(".domain-filters li.active .filter-btn");

    if (!selectedBtn) {
        console.error("No active filter found");
        return;
    }

    const selectedDomain = selectedBtn.dataset.domain;
    try {
        const response = await fetch('/filter-projects/', {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify({ domain: selectedDomain })
        });

        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }

        const data = await response.json();
        console.log("Response data:", data);

        const container = document.querySelector(".projects-container");

        // ✅ EMPTY STATE HANDLING
        if (!Array.isArray(data) || data.length === 0) {
            container.innerHTML = `
                <div class="no-projects">
                    <h3>🚧 More projects coming soon!</h3>
                    <p>I’m actively working on new ideas. Stay tuned 👀</p>
                </div>
            `;
            return;
        }

        let html = "";

        data.forEach(project => {
            let techHTML = "";

            if (project.tech_stack) {
                project.tech_stack.forEach(tech => {
                    techHTML += getTechIcon(tech);
                });
            }

            html += `
                <div class="project-card">
                    <div class="project-image" style="background-image: url('${project.image}');"></div>

                    <div class="project-info">
                        <h3>${project.title}</h3>
                        <p>${project.short_description || ""}</p>

                        <ul class="project-tech">
                            ${techHTML}
                        </ul>

                        <div class="view-project">
                            <a class="btn" href="${project.github}" target="_blank">GitHub</a>
                            <a class="btn" href="/project/${project.id}/">View Details</a>
                        </div>
                    </div>
                </div>
            `;
        });

        container.innerHTML = html;

    } catch (error) {
        console.error("🔥 FETCH ERROR:", error);
    }
}