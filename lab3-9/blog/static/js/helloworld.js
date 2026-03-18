$(document).ready(function () {
    $('.fold-button').on('click', function () {
        var button = $(this);
        var post = button.parents('.one-post');

        if (post.hasClass('folded')) {
            post.removeClass('folded');
            button.text('свернуть');
        } else {
            post.addClass('folded');
            button.text('развернуть');
        }
    });

    $('.one-post').hover(
        function (event) {
            $(event.currentTarget)
                .css({
                    boxShadow: '0 0 25px rgba(22, 160, 133, 0.45)',
                    transform: 'translateY(-2px)'
                })
                .find('.one-post-shadow')
                .stop(true)
                .animate({ opacity: '0.08' }, 300);
        },
        function (event) {
            $(event.currentTarget)
                .css({
                    boxShadow: 'none',
                    transform: 'translateY(0)'
                })
                .find('.one-post-shadow')
                .stop(true)
                .animate({ opacity: '0' }, 300);
        }
    );

    $('.header img').hover(
        function () {
            $(this).stop(true).animate({ width: '338px' }, 300);
        },
        function () {
            $(this).stop(true).animate({ width: '318px' }, 300);
        }
    );
});