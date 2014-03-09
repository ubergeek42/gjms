$(function() {
    in_progress = false;

    $(".gjms-menu-entry").hover(
        function() {
            if (!in_progress) {
            var label = $(this).data("name");
                in_progress = true
                $(".gjms-menu-label").text(label);
                $(".gjms-menu-label").animate({
                    top: "50"
                }, 250, function() {
                    in_progress = false;
                });
            }
        },

        function() {
            $(".gjms-menu-label").animate({
                top: "0"
            }, 250);
        }
    );
});