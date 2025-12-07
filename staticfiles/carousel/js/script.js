var swiper = new Swiper('.swiper-container', {
    loop: true,
    autoplay: {
        delay: 5000,
        disableOnInteraction: false,
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true
    },
    on: {
        slideChangeTransitionEnd: function() {
            var theme = $('.swiper-slide-active').data('theme')
            $('#banner').attr('class', theme)
        }
    },
    lazy: {
        loadPrevNext: true
    }
})

swiper.el.onmouseover = function(){
    swiper.autoplay.stop()
}

swiper.el.onmouseout = function(){
    swiper.autoplay.start()
}
