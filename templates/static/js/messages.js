$(function(){
    var tempo = 10000
    function barProgress(){
        var percent = 100
        var sleep = tempo / percent
        var bar = $(".progress-bar-striped")
        var bar_pixel = bar.width()
        var pixel_percent = bar_pixel / percent

        function run(bar_pixel, pixel_percent){
            if (bar_pixel >= 0){
                console.log(bar_pixel)
                bar.delay(sleep).width(Math.round(bar_pixel, 0));
                bar_pixel = Math.round(bar_pixel-pixel_percent);
                run(bar_pixel, pixel_percent);
            }
        }
        run(bar_pixel, pixel_percent);
    }
    
    if ($("#message").text()){
        console.log('Iniciou')
        $(".alert").show().delay(tempo, barProgress()).queue(function(){
            $(this).hide();
        });
    }
});