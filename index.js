var Index = function() {

    var startFadeIn = function(){
                $("#name").hide().delay(2000).fadeIn(1000); 
                $("#profession").hide().delay(3000).fadeIn(1000); 
                $("#navbar").hide().delay(4000).fadeIn(1000); 
            }    


    var init = function(){
        startFadeIn();
    };

    // Public API
    return {
        init: init
    };
}();