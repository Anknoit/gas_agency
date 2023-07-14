//Toggle View Panel
$(".click_dashboard").click(function () {
  $("div#display_dashboard").show("slow");

  $("div#display_prescription").hide("slow");
  $("div#display_registered_customer").hide("slow");
  $("div#display_report").hide("slow");
  $("div#display_customer").hide("slow");
});
$(".click_prescription").click(function () {
  $("div#display_prescription").show("slow");

  $("div#display_dashboard").hide("slow");
  $("div#display_registered_customer").hide("slow");
  $("div#display_report").hide("slow");
  $("div#display_customer").hide("slow");
});
$(".click_registered_customer").click(function () {
  $("div#display_registered_customer").show("slow");

  $("div#display_dashboard").hide("slow");
  $("div#display_prescription").hide("slow");
  $("div#display_report").hide("slow");
  $("div#display_customer").hide("slow");
});
$(".click_report").click(function () {
  $("div#display_report").show("slow");

  $("div#display_dashboard").hide("slow");
  $("div#display_prescription").hide("slow");
  $("div#display_registered_customer").hide("slow");
  $("div#display_customer").hide("slow");
});
$(".click_customer").click(function () {
  $("div#display_customer").show("slow");

  $("div#display_dashboard").hide("slow");
  $("div#display_prescription").hide("slow");
  $("div#display_registered_customer").hide("slow");
  $("div#display_report").hide("slow");
});
