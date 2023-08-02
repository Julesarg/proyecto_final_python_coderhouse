function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("myDiv").style.display = "flex";
}

let variable;
function executeLoader() {
  variable = setTimeout(showPage,4500);
}
//gallery loader//
let variable2;
function executeLoader_gallery() {
  variable2 = setTimeout(showPage,3000);
}
//profile & about loader//
let variable3;
function executeLoader_short() {
  variable3 = setTimeout(showPage,2000);
}