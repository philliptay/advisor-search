let request = null;

function setup(){
    $('#searchBar').focus();
    $('#searchBar').on('input', getResults);
    getFavorited('None');
}
let faveHeight = 0;
function handleResponse(response)
{
  if (response == "")
     $('#searchResults').html("(None)");
  else
     $('#searchResults').html(response);
  faveHeight = $('#fav-content').height();
  $('#resultsWrapper').css("max-height", $('#resultsWrapper').height()-faveHeight+"px");
}

function getResults()
{
let inputs = $("#searchBar").val();
let inputsURI = encodeURIComponent(inputs);
let url = '/searchresults?inputs=' + inputsURI;
if (request != null)
  request.abort();
request = $.ajax({
  type: "GET",
  url: url,
  success: handleResponse
  }
);
var property1 = document.getElementById('CBbut');
var property2 = document.getElementById('CAbut');
var property3 = document.getElementById('ECbut');
var property4 = document.getElementById('Gbut');
var property5 = document.getElementById('Vbut');
var property6 = document.getElementById('MLbut');
var property7 = document.getElementById('AIbut');
var property8 = document.getElementById('NLPbut');
var property9 = document.getElementById('POLbut');
var property10 = document.getElementById('PLCbut');
var property11 = document.getElementById('SPbut');
var property12 = document.getElementById('SYSbut');
var property13 = document.getElementById('THEbut');
var compBio = false;
if (inputs.includes("Computational Biology") || inputs.includes("All")){
  compBio = true;
}
var compArch = false;
if (inputs.includes("Computer Architecture") || inputs.includes("All")){
  compArch = true;
}
var econComp = false;
if (inputs.includes("Economics/Computation") || inputs.includes("All")){
  econComp = true;
}
var graph = false;
if (inputs.includes("Graphics") || inputs.includes("All")) {
  graph = true;
}
var vis = false;
if (inputs.includes("Vision") || inputs.includes("All")){
  vis = true;
}
var ml = false;
if (inputs.includes("Machine Learning") || inputs.includes("All")) {
  ml = true;
}
var ai = false;
if (inputs.includes("AI") || inputs.includes("All")) {
  ai = true;
}
var nlp = false;
if (inputs.includes("Natural Language Processing") || inputs.includes("All")) {
  nlp = true;
}
var pol = false;
if (inputs.includes("Policy") || inputs.includes("All")) {
  pol = true;
};
var plc = false;
if (inputs.includes("Programming Languages/Compilers") || inputs.includes("All")) {
  plc = true;
}
var sp = false;
if (inputs.includes("Security & Privacy") || inputs.includes("All")) {
  sp = true;
}
var sys = false;
if (inputs.includes("Systems") || inputs.includes("All")) {
  sys = true;
}
var theory = false;
if (inputs.includes("Theory") || inputs.includes("All")) {
  theory = true;
}
if (compBio) {
  property1.style.backgroundColor = "#e65c00";
}
else {
  property1.style.backgroundColor = "#5bc0de";
}
if (compArch) {
  property2.style.backgroundColor = "#e65c00";
}
else {
  property2.style.backgroundColor = "#5bc0de";
}
if (econComp) {
  property3.style.backgroundColor = "#e65c00";
}
else {
  property3.style.backgroundColor = "#5bc0de";
}
if (graph) {
  property4.style.backgroundColor = "#e65c00";
}
else {
  property4.style.backgroundColor = "#5bc0de";
}
if (vis) {
  property5.style.backgroundColor = "#e65c00";
}
else {
  property5.style.backgroundColor = "#5bc0de";
}
if (ml) {
  property6.style.backgroundColor = "#e65c00";
}
else {
  property6.style.backgroundColor = "#5bc0de";
}
if (ai) {
  property7.style.backgroundColor = "#e65c00";
}
else {
  property7.style.backgroundColor = "#5bc0de";
}
if (nlp) {
  property8.style.backgroundColor = "#e65c00";
}
else {
  property8.style.backgroundColor = "#5bc0de";
}
if (pol) {
  property9.style.backgroundColor = "#e65c00";
}
else {
  property9.style.backgroundColor = "#5bc0de";
}
if (plc) {
  property10.style.backgroundColor = "#e65c00";
}
else {
  property10.style.backgroundColor = "#5bc0de";
}
if (sp) {
  property11.style.backgroundColor = "#e65c00";
}
else {
  property11.style.backgroundColor = "#5bc0de";
}
if (sys) {
  property12.style.backgroundColor = "#e65c00";
}
else {
  property12.style.backgroundColor = "#5bc0de";
}
if (theory) {
  property13.style.backgroundColor = "#e65c00";
}
else {
  property13.style.backgroundColor = "#5bc0de";
}
}

function handleFavoritedResponse(response)
{
$('#favorited').html(response);

if ($('#fav-toggle').hasClass('fa-minus')) {

  if (faveHeight < $('#fav-content').height())
    $('#resultsWrapper').css("max-height", $('#resultsWrapper').height()-($('#fav-content').height()-faveHeight)+"px");

  else if (faveHeight > $('#fav-content').height())
    $('#resultsWrapper').css("max-height", $('#resultsWrapper').height()+(faveHeight-$('#fav-content').height())+"px");

}
faveHeight = $('#fav-content').height();



}


function getFavorited(profid)
{
$($('.prof'+profid).find('i')).toggleClass("active");
let toggled = 'true';
if ($('#fav-toggle').hasClass('fa-plus')) {
  toggled = 'false';
}
let url = '/favoritedProf?profid=' + profid + '&toggled='+toggled;
if (request != null)
  request.abort();
request = $.ajax({
  type: "GET",
  url: url,
  success: handleFavoritedResponse
  }
);
}
function getAll(){
  $('#searchBar').val('All');
  $('#searchBar').trigger('input');
  var property1 = document.getElementById('CBbut');
  property1.style.backgroundColor = "#e65c00";
  var property2 = document.getElementById('CAbut');
  property2.style.backgroundColor = "#e65c00";
  var property3 = document.getElementById('ECbut');
  property3.style.backgroundColor = "#e65c00";
  var property4 = document.getElementById('Gbut');
  property4.style.backgroundColor = "#e65c00";
  var property5 = document.getElementById('Vbut');
  property5.style.backgroundColor = "#e65c00";
  var property6 = document.getElementById('MLbut');
  property6.style.backgroundColor = "#e65c00";
  var property7 = document.getElementById('AIbut');
  property7.style.backgroundColor = "#e65c00";
  var property8 = document.getElementById('NLPbut');
  property8.style.backgroundColor = "#e65c00";
  var property9 = document.getElementById('POLbut');
  property9.style.backgroundColor = "#e65c00";
  var property10 = document.getElementById('PLCbut');
  property10.style.backgroundColor = "#e65c00";
  var property11 = document.getElementById('SPbut');
  property11.style.backgroundColor = "#e65c00";
  var property12 = document.getElementById('SYSbut');
  property12.style.backgroundColor = "#e65c00";
  var property13 = document.getElementById('THEbut');
  property13.style.backgroundColor = "#e65c00";
}

function handleProfResponse(response)
{
$('#profSection').html(response);
}

function getProfResults(profid)
{
if(!$(event.target).is("i")) {
  let url = '/profresults?profid=' + profid;
  if (request != null)
    request.abort();
  request = $.ajax({
    type: "GET",
    url: url,
    success: handleProfResponse
    }
  );
  }
}

function toggleFavs() {
  if($('#fav-content').css("max-height") != "0px") {
    $('#fav-content').css("max-height", "0vh");
    $('#fav-toggle').removeClass("fa-minus").addClass("fa-plus");
    $('#resultsWrapper').css("max-height", "68vh");
  }
  else {
    $('#fav-content').css("max-height", "30vh");
    $('#fav-toggle').removeClass("fa-plus").addClass("fa-minus");
    $("#fav-content").on('transitionend webkitTransitionEnd',
function(event) {
   if(event.target.id == 'fav-content'){
      $('#resultsWrapper').css("max-height", ($('#resultsWrapper').height()-$('#fav-content').height())/$(window).height()*100+"vh");
      faveHeight = $('#fav-content').height();
   }
});

  }
}

function clearAll(){
  $('#searchBar').val(null).trigger('input');
}

function addArea(area)
{
  let inputs = $("#searchBar").val();
  if (inputs.includes(area)){
    if (inputs.charAt(inputs.indexOf(area)+area.length) == ',' && inputs.indexOf(area)+area.length+1 != inputs.length) {
      inputs = inputs.replace(area+', ', '');
    }
    else {
      inputs = inputs.replace(area, '');
    }

    if (inputs.charAt(inputs.length-2) == ',') {
      inputs = inputs.slice(0, -2);
    }
  }
  else {
    if (inputs == '') {
      inputs+=area;
    }
    else {
      inputs+=', '+area;
    }
  }
  $('#searchBar').val(inputs);
  $('#searchBar').trigger('input');
}

$(document).ready(setup);
