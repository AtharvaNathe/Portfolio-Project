// theme toggle + header shadow + contact AJAX + small reveal animations
(function(){
  // theme toggle (light/dark stored in localStorage)
  const themeBtn = document.getElementById('themeToggle');
  const body = document.body;
  const saved = localStorage.getItem('theme');
  if(saved === 'light') body.classList.remove('dark'); else body.classList.add('dark');
  if(themeBtn){
    themeBtn.addEventListener('click', () => {
      const isDark = body.classList.toggle('dark');
      localStorage.setItem('theme', isDark ? 'dark' : 'light');
      themeBtn.textContent = isDark ? '☀️' : '🌙';
    });
  }

  // header shadow on scroll
  const header = document.getElementById('siteHeader');
  window.addEventListener('scroll', ()=> {
    if(window.scrollY > 20) header.classList.add('scrolled'); else header.classList.remove('scrolled');
  });

  // small reveal on scroll
  function reveal(){
    document.querySelectorAll('.exp, .project-card, .skill, .glass').forEach(el=>{
      const rect = el.getBoundingClientRect();
      if(rect.top < window.innerHeight - 60) el.style.opacity = 1;
    });
  }
  window.addEventListener('load', reveal);
  window.addEventListener('scroll', reveal);

  // AJAX contact submission (uses form with csrf token)
  const form = document.getElementById('contactForm');
  const status = document.getElementById('contactStatus');
  if(form){
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const data = new FormData(form);
      try {
        const resp = await fetch(form.action, {
          method: 'POST',
          body: data,
          headers: {'X-Requested-With': 'XMLHttpRequest'}
        });
        const json = await resp.json();
        if(json.ok){
          status.textContent = 'Message sent — thank you!';
          status.style.color = '#7ef6c3';
          form.reset();
        } else {
          status.textContent = json.error || 'Unable to send. Try again.';
          status.style.color = '#ff8a8a';
        }
      } catch(err){
        status.textContent = 'Network error. Try later.';
        status.style.color = '#ff8a8a';
      }
    });
  }
})();
