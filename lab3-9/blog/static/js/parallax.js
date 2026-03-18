$(document).ready(function () {
    var $parallaxElements = $('.parallax-icon-first, .parallax-icon-second, .parallax-icon-third');

    $(window).on('scroll', function () {
        var scrollTop = $(window).scrollTop();

        $('.parallax-icons-first').css('transform', 'translateY(' + (scrollTop * 0.35) + 'px)');
        $('.parallax-icons-second').css('transform', 'translateY(' + (scrollTop * 0.2) + 'px)');
        $('.parallax-icons-third').css('transform', 'translateY(' + (scrollTop * 0.1) + 'px)');
    });
});