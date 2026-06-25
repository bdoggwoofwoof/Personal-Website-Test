// Accordion
document.querySelectorAll('.accordion-trigger').forEach(trigger => {
  trigger.addEventListener('click', () => {
    const item = trigger.closest('.accordion-item');
    const content = item.querySelector('.accordion-content');
    const body = item.querySelector('.accordion-body');
    const isOpen = item.classList.contains('open');

    document.querySelectorAll('.accordion-item.open').forEach(openItem => {
      openItem.classList.remove('open');
      openItem.querySelector('.accordion-content').style.maxHeight = '0';
    });

    if (!isOpen) {
      item.classList.add('open');
      content.style.maxHeight = body.scrollHeight + 'px';
    }
  });
});

// Mark active nav link
const currentPage = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav-links a').forEach(link => {
  const href = link.getAttribute('href');
  if (href === currentPage || (currentPage === '' && href === 'index.html')) {
    link.classList.add('active');
  }
});
