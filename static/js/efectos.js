window.sr = ScrollReveal();
sr.reveal('.btn-nombre',{duration:2000, origin:'left',distance:'300px', opacity:0.0});
sr.reveal('.btn-home',{duration:1400, origin:'top',distance:'300px', opacity:0.0});
sr.reveal('.btn-acerca',{duration:1400, origin:'top',distance:'300px', opacity:0.0});
sr.reveal('.btn-tipos',{duration:1400, origin:'top',distance:'300px', opacity:0.0});
sr.reveal('.nombre',{duration:1400, origin:'top',distance:'300px', opacity:0.0, delay:450});
sr.reveal('.eslogan',{duration:1400, origin:'bottom',distance:'300px', opacity:0.0, delay:450});
sr.reveal('.ingresar',{duration:1400, origin:'right',distance:'300px', opacity:0.0, delay:450});
sr.reveal('.btn-registro',{duration:1400, origin:'top',distance:'300px', opacity:0.0});

$(document).ready(function(){
    var acerca_de = $('#acerca_de').offset().top,
    tipos_de_plantas = $('#tipos_de_plantas').offset().top;
    $('#btn_acerca_de').on('click', function(u){
        u.preventDefault(); 
        $('html, body').animate({
            scrollTop:acerca_de
        },700);
    });

    $('#btn_tipos_de_plantas').on('click', function(u){
        u.preventDefault(); 
        $('html, body').animate({
            scrollTop:tipos_de_plantas
        },700);
    });

    $(window).scroll(function(){
        var resolucion = $(window).width();
        if(resolucion>800){
            var posicion = $(window).scrollTop();
            $('header .titulos').css({
                'transform': 'translate(0px,  -'+ 
                posicion/7 +'%)'
            });

            $('.acerca_de article').css({
                'transform': 'translate(0px, -'+ 
                posicion/7 +'%)'
            });
        }
    });

})


