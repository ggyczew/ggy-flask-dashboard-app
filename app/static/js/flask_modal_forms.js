
/*
django-bootstrap-modal-forms
version : 2.2.0
Copyright (c) 2021 Uros Trstenjak
https://github.com/trco/django-bootstrap-modal-forms
*/

/* 
Modified and Simplified version for use with Flask
version 1.0.0
Copyright (c) 2021 Grzegorz GYczew
*/ 

/*

Updated to ES6
- arrow functions
- ajax .done .fail

*/

(function ($) {

    // Open modal & load the form at formURL to the modalContent element
    var modalForm = function (settings) {
    
        $(settings.modalID)
        .find(settings.modalBody)
        .load(settings.formURL, (data, textStatus, xhr) => {
            $(settings.modalID).modal("show");
            if (textStatus == 'error'){
                $(settings.modalID).find(settings.modalTitle).text('Error !!!');
                $(settings.modalID).find(settings.modalBody).text(xhr.responseText);
            } else {
                $(settings.modalForm).attr("action", settings.formURL);
                if (settings.selectedRowsIds){
                    $(settings.modalID).find("#selected_rows").val(settings.selectedRowsIds)
                }
                addEventHandlers(settings);
            }
        });
        $(settings.modalID).find(settings.modalTitle).text(settings.title);
    };

    var addEventHandlers = function (settings) {
        $(settings.modalForm).on("submit", function (event) {
            if (event.originalEvent !== undefined && settings.isDeleteForm === false) {
                event.preventDefault();
                isFormValid(settings);
                return false;
            }
        });
        // Modal close handler
        $(settings.modalID).on("hidden.bs.modal", function (event) {
            $(settings.modalForm).remove();
        });
    };

    

    // Check if form.is_valid() & either show errors or submit it via callback
    const isFormValid = (settings) => {
        $.ajax({
            type: $(settings.modalForm).attr("method"),
            url: $(settings.modalForm).attr("action"),
            data: new FormData($(settings.modalForm)[0]),
            contentType: false,
            processData: false,
            beforeSend: () => $(settings.submitBtn).prop("disabled", true)
        }).done((data, textStatus, xhr) => {
            if ($(data).find(settings.errorClass).length > 0) {
                // Form is not valid, update it with errors
                $(settings.modalID).find(settings.modalBody).html(data);
                $(settings.modalForm).attr("action", settings.formURL);
                // Reinstantiate handlers
                addEventHandlers(settings);
            } else {
                // Form is valid, submit it
                $(settings.modalForm).submit();
                $(settings.modalID).modal("hide");
                window.location.reload();
            }
        }).fail((xhr, textStatus, errorThrown) => {
            // alert(request.responseText);
            $(settings.modalID).find(settings.modalTitle).text('Error !!!');
            $(settings.modalID).find(settings.modalContent).html(xhr.responseText);
            $(settings.modalForm).attr("action", settings.formURL);
        });
    };



    $.fn.modalForm = function (options) {
        // Default settings
        var defaults = {
            modalID: "#modal",
            modalTitle: ".modal-title",
            modalBody: ".modal-body",
            modalForm: ".modal-body form",
            formURL: null,
            title: "Modal Title",
            isDeleteForm: false,
            errorClass: ".is-invalid",
            table: null,
            selectedRowsIds: null
        };

        // Extend default settings with provided options
        var settings = $.extend(defaults, options);

        this.each(function () {
            // Add click event handler to the element with attached modalForm
            $(this).click(function (event) {
                
                if (settings.table !== null) {
                    let selectedRows = settings.table.rows({ selected: true })
                    if (selectedRows.count() == 0){
                        console.log('No table rows selected!!!')
                        return;
                    } else {
                        let selectedRowsIds = []
                        selectedRows.data().each(row => selectedRowsIds.push(parseInt(row[1])));
                        settings.selectedRowsIds = JSON.stringify(selectedRowsIds)    
                    }
                } 
                modalForm(settings);
                
                
                
            });
        });

        return this;
    };

}(jQuery));