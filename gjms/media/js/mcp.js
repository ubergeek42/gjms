$(function() {
    in_canvas = false;

    $(".gjms-offcanvas-trigger").click(function() {
        if (!in_canvas) {
            $(".gjms-offcanvas-bar").animate({
                left: "250"
            }, 750);
            $(".gjms-offcanvas-nav").animate({
                left: "0"
            }, 750);
            in_canvas = true;
        } else {
            $(".gjms-offcanvas-bar").animate({
                left: "0"
            }, 750);
            $(".gjms-offcanvas-nav").animate({
                left: "-250"
            }, 750);
            in_canvas = false;
        }

        $(this).toggleClass("fa-angle-right");
        $(this).toggleClass("fa-angle-left");
    });
});