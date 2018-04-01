/**
 * Created by dark on 31/03/18.
 */
$(function(){
    $('.save-importer').click(function (event) {
        $.ajax({
            url:'/herramienta/importer/save/',
            type:'post',
            data: {rows: $('.selectpicker').selectpicker('val'), file: window.id_file},
            dataType: 'json',
            success: function (data) {

            }
        });
    });
});