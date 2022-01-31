$(".login-btn").click(function(){
  $(".signup").addClass("hidden");
  $(".login").removeClass("hidden");
  $(".login-btn").addClass("btn");
  $(".signup-btn").removeClass("btn");
  $("title").text("Log In");
});
$(".signup-btn").click(function(){
  $(".login").addClass("hidden");
  $(".signup").removeClass("hidden");
  $(".signup-btn").addClass("btn");
  $(".login-btn").removeClass("btn");
  $("title").text("Sign Up");
});
