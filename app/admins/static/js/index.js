const swp = document.querySelector("#toggle-btn");

swp.addEventListener("click", function () {
  document.querySelector("#sidebar").classList.toggle("expand");
});