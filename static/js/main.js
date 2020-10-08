$(function (){

    var header1 = $("#header1"),
    introH = $("#intro").innerHeight(),
    remont = $("#remont").innerHeight(),
    scrollOffset = 0;
    //scrollOffset = $(window).scrollTop;

    //checkScroll1(scrollOffset); //aтут работает
    //checkScroll2(scrollOffset);
    //checkScroll(scrollOffset);

    $(window).on("scroll", function () {
        scrollOffset = $(this).scrollTop();

        /*sif(scrollOffset >= introH){
            header1.addClass("fixed");
        }
        else{
            header1.removeClass("fixed");
        }*/

        header1.addClass("fixed");
        //checkScroll1(scrollOffset);
        //checkScroll2(scrollOffset);
    });

    /*function checkScroll(scrollOffset){
        header1.addClass("fixed");
    }*/

    /*function checkScroll1(scrollOffset){
        if(scrollOffset >= introH){
            header1.addClass("fixed1");
        }
        else{
            header1.removeClass("fixed1");
        }
    }*/

    /*function checkScroll2(scrollOffset){
        if(scrollOffset >= remont){
            header1.addClass("fixed");
        }
        else{
            header1.removeClass("fixed");
        }
    }*/

    $("#nav_togle").on("click", function(event){
        event.preventDefault();

        $("#navbar1").toggleClass("active");
        $("#nav_togle").toggleClass("active1");
    });




});

