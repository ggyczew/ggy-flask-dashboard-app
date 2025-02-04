$(function() {

    // show the alert
    setTimeout(function() {
            $(".alert").fadeOut(500, function(){
                $(this).remove(); 
            });
        }, 5000);

    $(".modal-edit").each(function () {
        $(this).modalForm({
            formURL: $(this).data("form-url"),
            title: $(this).data("form-title"),
        });
    });

    $(".modal-action").each(function () {
        $(this).modalForm({
            formURL: $(this).data("form-url"),
            title: $(this).data("form-title"),
        });
    });

    $('#main_table').DataTable({
        "scrollX": true
    });
    

    

});