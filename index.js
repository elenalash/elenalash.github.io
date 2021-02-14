var Index = function() {

    var navBarShow = function(){
                $("#navbar").hide().delay(2000).fadeIn(1000); 
            }    


    var init = function(){
        navBarShow();
    };

    // Public API
    return {
        init: init
    };
}();