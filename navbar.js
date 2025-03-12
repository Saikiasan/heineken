const navbarItems = [{
    link: "/heineken/",
    text: "Home"
  },
  {
    link: "/heineken/stone/",
    text: "Vedantu"
  },
  {
    link: "/heineken/pwc/",
    text: "PWC"
  },
];


document.addEventListener("DOMContentLoaded", function () {
  const navbar = document.getElementById("navbar");

  if (navbar) {
    let navItemsHTML = navbarItems.map(item => `
      <li class="nav-item">
        <a class="nav-link" href="${item.link}">
          <span style="display: inline-block;width: 10px;height: 10px;background-color: red;border-radius: 50%;"></span> 
          ${item.text}
        </a>
      </li>
    `).join("");

    navbar.innerHTML = `
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container">
          <a class="navbar-brand" href="#">My Brand</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                  aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
              ${navItemsHTML}
            </ul>
          </div>
        </div>
      </nav>
    `;
  }
});