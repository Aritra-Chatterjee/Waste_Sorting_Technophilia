$(".grin").click(function(){
  $(".thank-you").removeClass("hidden");
  $("footer").css("position","static");
  $(".ratings-container").addClass("hidden");
});
$(".meh").click(function(){
  $(".feedback-form").removeClass("hidden");
  $("footer").css("position","static");
  $(".ratings-container").hide();
  $(".pic1").removeClass("hidden");
});
$(".sad").click(function(){
  $(".feedback-form").removeClass("hidden");
  $("footer").css("position","static");
  $(".ratings-container").addClass("hidden");
  $(".pic1").removeClass("hidden");
});