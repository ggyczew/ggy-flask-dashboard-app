$(document).ready(function() {
  
    $('#flexSwitchUpdateTasks').mousedown(function(){
        var switch_state = (this.checked ? 'pause' : 'resume');
        returnVal = confirm(switch_state + ' task updating?');
        if (returnVal) {
        $.ajax({
            context: this,
            url: '/rpt/admin/job',
            data: { job_id: 'task_update_job', action: switch_state }
        }).done(function(data) {
            $(this).attr('checked', !this.checked);
            $('#UpdateTasksStatus').html(data);
        }).fail(function() {
            alert('error');
        });
        }
    });

    $('#flexSwitchRunTasks').mousedown(function(){
        var switch_state = (this.checked ? 'pause' : 'resume');
        returnVal = confirm(switch_state + ' task running?');
        if (returnVal) {
        $.ajax({
            context: this,
            url: '/rpt/admin/job',
            data: { job_id: 'task_run_job', action: switch_state }
        }).done(function(data) {
            $(this).attr('checked', !this.checked);
            $('#RunTasksStatus').html(data);
        }).fail(function() {
            alert('error');
        });
        }
    });
    
})