// JavaScript for smooth scrolling to sections
document.querySelectorAll('.nav-link').forEach(link => {
  link.addEventListener('click', (event) => {
    event.preventDefault();

    // Get the target page from data-page attribute
    const targetPage = event.target.getAttribute('data-page');

    // Check if the section exists and scroll to it smoothly
    const section = document.getElementById(targetPage);
    if (section) {
      section.scrollIntoView({ behavior: 'smooth' });

      // Highlight the current section in the navbar
      document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active-link'); // Remove active class from all links
      });
      event.target.classList.add('active-link'); // Add active class to the clicked link
    }
  });
});
