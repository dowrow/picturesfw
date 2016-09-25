/*global console, $, localStorage */
$(function () {
    'use strict';

    $('#agree').click(function () {
        localStorage.setItem('agreed', 'true');
    });

    var agreed = localStorage.getItem('agreed');

    if (agreed !== 'true') {
        $('#disclaimerModal').modal({
            backdrop: 'static',
            keyboard: false
        });
    }

});
