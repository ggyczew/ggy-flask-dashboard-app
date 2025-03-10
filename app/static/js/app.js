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

    $(".modal-view").each(function () {
        $(this).on("click", function (e) {
            e.preventDefault();
            const modalURL = $(this).data("url");
            const modalTitle = $(this).data("modal-title");
            const modalID = "#modal"; // Change this to your actual modal ID
            const modalBody = $(modalID).find(".modal-body");
    
            // Open the modal
            $(modalID).modal("show");
            $(modalID).find(".modal-title").text(modalTitle);
            
            // Show loading indicator
            modalBody.html('<div class="text-center p-3"><i class="fas fa-spinner fa-spin fa-2x"></i> Loading...</div>');
    
            // Load content via AJAX
            $.ajax({
                url: modalURL,
                method: "GET",
            }).done(function (data) {
                modalBody.html(data);
    
                // Reinitialize DataTable if the content contains a table
                modalBody.find("table").each(function () {
                    if (!$.fn.DataTable.isDataTable(this)) {
                        $(this).DataTable({
                            "scrollX": true
                        });
                    }
                });
            }).fail(function (xhr) {
                modalBody.html('<div class="alert alert-danger">Error loading content. Please try again.</div>');
            });
        });
    });

    // $('#modal').on('shown.bs.modal', function () {
    //     $('#main_table').DataTable({
    //         "scrollX": true,
    //         "retrieve": true  // Prevents re-initialization issues
    //     });
    // });



    // Handles loading JSON chart data into a modal
    $(".modal-chart").each(function () {
        $(this).on("click", function (e) {
            e.preventDefault();
            const modalURL = $(this).data("url")
            const modalTitle = $(this).data("modal-title");
            const modalID = "#modal"; // Change this to your actual modal ID
            const modalBody = $(modalID).find(".modal-body");

            // Open the modal
            $(modalID).modal("show");
            $(modalID).find(".modal-title").text(modalTitle);

            // Show loading indicator
            modalBody.html('<div class="text-center p-3"><i class="fas fa-spinner fa-spin fa-2x"></i> Loading chart...</div>');

            // Load chart JSON data via AJAX
            $.ajax({
                url: modalURL,
                method: "GET",
                dataType: "json",
            }).done(function (chartConfig) {
                modalBody.html('<canvas id="chartCanvas"></canvas>');

                const ctx = document.getElementById("chartCanvas").getContext("2d");

                // Destroy any existing Chart.js instance before creating a new one
                if (window.chartInstance) {
                    window.chartInstance.destroy();
                }

                // Create new Chart.js instance with the received config
                window.chartInstance = new Chart(ctx, chartConfig);
            }).fail(function () {
                modalBody.html('<div class="alert alert-danger">Error loading chart data. Please try again.</div>');
            });
        });
    });


    var popover = new bootstrap.Popover(document.querySelector('.popover-dismiss'), {
        trigger: 'focus'
      })

});