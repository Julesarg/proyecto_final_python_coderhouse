let variable;
function executeLoader() {
  variable = setTimeout(showPage,4000);
  let boot = "run"
  console.log(boot)
}
function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("myDiv").style.display = "flex";
}