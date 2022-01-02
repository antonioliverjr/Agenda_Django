$(function(){
    var tempo = 10000
    function barProgress(){
        var percent = 100
        var sleep = tempo / (percent+15)
        var bar = $(".progress-bar-striped")
        var bar_pixel = bar.width()
        var pixel_percent = bar_pixel / percent

        function run(bar_pixel, pixel_percent){
            if (bar_pixel >= 0){
                bar.width(Math.round(bar_pixel, 2));
                bar_pixel = Math.round(bar_pixel-pixel_percent);
                setTimeout(function(){
                    run(bar_pixel, pixel_percent);    
                }, sleep);
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

    var erro_form = $("ul.errorlist").detach()
    $("#erros_forms").html(erro_form).show()
    $("ul.errorlist").addClass("list-group")
    $("ul.errorlist li").addClass("list-group-item list-group-item-danger")
});