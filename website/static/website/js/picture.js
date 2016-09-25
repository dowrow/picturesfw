(function ($) {

    var pictureId = 0;

    $(function onLoad() {

        // Ratings
        $('.laughing-link').click(function () {
            var pictureId = $(this).data('picture-id');
            var endpoint = '/laughing/';
            var data = {
                'picture': pictureId
            };
            $.post(endpoint, data);
            var count = parseInt($(this).find('.count').text(), 10);
            $(this).find('.count').text(count + 1);
        });

        $('.fearful-link').click(function () {
            var pictureId = $(this).data('picture-id');
            var endpoint = '/fearful/';
            var data = {
                'picture': pictureId
            };
            $.post(endpoint, data);
            var count = parseInt($(this).find('.count').text(), 10);
            $(this).find('.count').text(count + 1);
        });

        $('.banana-link').click(function () {
            var pictureId = $(this).data('picture-id');
            var endpoint = '/banana/';
            var data = {
                'picture': pictureId
            };
            $.post(endpoint, data);
            var count = parseInt($(this).find('.count').text(), 10);
            $(this).find('.count').text(count + 1);
        });


        // Report
        $('.report-link').click(function () {
            pictureId = $(this).data('picture-id');
            $('#reportModal').modal();
        });
        
        $('#report').click(function () {
            var endpoint = '/report/';
            var data = {
                'picture': pictureId
            };
            $.post(endpoint, data);
        });
    });
})($ || jQuery);