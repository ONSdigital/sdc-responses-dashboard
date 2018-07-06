/*jshint esversion: 6 */
function callAPI(collexID = $("#collex-id").data("collex"), enableTimeout = true) {
    const reportingURL = $("#collex-id").data("reporting-url");
    const reportingRefreshCycle = $("#collex-id").data("reporting-refresh-cycle");

    $.ajax({
        dataType: "json",
        url: reportingURL + "reporting-api/v1/response-dashboard/collection_exercise/" + collexID
    }).done((result) => {
        const downloads = result.report.downloads;
        const uploads = result.report.uploads;
        const accountsEnrolled = result.report.accountsEnrolled;
        const sampleSize = result.report.sampleSize;
        const timeUpdated = moment.unix(result.metadata.timeUpdated).calendar(); // eslint-disable-line
        const progress = (uploads / sampleSize * 100).toFixed(2);

        $('#error-reporting').hide();
        $('.content').show();

        $("#downloads-counter").text(downloads).effect("bounce", "slow");
        $("#uploads-counter").text(uploads).effect("bounce", "slow");
        $("#accounts-enrolled-counter").text(accountsEnrolled).effect("bounce", "slow");
        $("#sample-size-counter").text(sampleSize).effect("bounce", "slow");
        $("#time-updated").text(timeUpdated);
        $("#progress-uploaded").text(uploads);
        $("#progress-size").text(sampleSize);
        $("#collex-progress").text(progress + "%").css("width", progress + "%");

        if (enableTimeout) {
            setTimeout(callAPI, reportingRefreshCycle);
        }
    }).fail((result) => {
        $('#error-reporting').show();
        $('.content').hide();

        if (enableTimeout) {
            setTimeout(callAPI, reportingRefreshCycle);
        }
    });
}

function initiliseDataTables() {

    /* eslint-disable */
    const surveyTable = $("#survey-datatable").DataTable({
        paging: true,
        lengthChange: false,
        searching: true,
        ordering: true,
        info: true,
        autoWidth: false,
        autoHeight: false,
        scrollY: "30vh",
        scrollCollapse: true,
        scroller: {
            loadingIndicator: false
        }
    });
    /* eslint-enable */

    $("#survey-search").keyup(function() {
        surveyTable.search($(this).val()).draw();
    });

    /* eslint-disable */
    const collexTable = $("#collex-datatable").DataTable({
        paging: true,
        lengthChange: false,
        searching: true,
        ordering: true,
        info: true,
        autoWidth: false,
        autoHeight: false,
        scrollY: "30vh",
        scrollCollapse: true,
        scroller: {
            loadingIndicator: false
        },
        data: [],
        columns: [{
            "data": "userDescription",
            "title": "Collection Exercise Period",
            "width": "600px"
        }],
        rowId: 'collectionExerciseId'
    });
    /* eslint-enable */

    $("#collex-search").keyup(function() {
        collexTable.search($(this).val()).draw();
    });

    $("#survey-datatable tbody").on("click", "tr", function() {
        const id = surveyTable.row(this).id();

        if (typeof id !== "undefined") {
            const surveyShortName = $(this).data("survey-short-name");

            $("#chosen-survey").text(surveyShortName);
			$("#modal-survey").modal("toggle");
			
            loadCollexTableData(collexTable, id);
        }

    });

}

function loadCollexTableData(collexTable, id) {
    const surveys = JSON.parse($('#collex-id').data('surveys'));

    collexTable.clear().draw();
    collexTable.rows.add(get_collex_from_survey_id(surveys, id)).draw();

    $("#modal-collex").modal("toggle");
    $("#collex-datatable tbody").on("click", "tr", function() {
        const id = collexTable.row(this).id();

        if (typeof id !== "undefined") {
            window.location.href = id;
        }
    });
}

function get_collex_from_survey_id(surveys, survey_id) {

    for (let i = 0; i < surveys.length; i++) {
        if (surveys[i].surveyId === survey_id) {
            collection_exercises = surveys[i].collectionExercises;
            return collection_exercises;
        }
    }
}

$(document).ready(function() {
    callAPI();
    initiliseDataTables();
});
