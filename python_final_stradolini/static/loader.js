let variable;
function executeLoader() {
  variable = setTimeout(showPage,4500);
}
function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("myDiv").style.display = "flex";
}