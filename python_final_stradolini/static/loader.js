let variable;
function executeLoader() {
  variable = setTimeout(showPage,4000);
}
function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("myDiv").style.display = "flex";
}