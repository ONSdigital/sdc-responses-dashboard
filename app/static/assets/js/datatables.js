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

            if (typeof reporting_url == "undefined") {
                $("#modal-collex").attr('data-backdrop', 'static');
                $("#modal-collex").attr('data-keyboard', 'false');
            }

            loadCollexTableData(collexTable, id);
        }

    });

}

function loadCollexTableData(collexTable, id) {

    const surveys = JSON.parse($('#collex-id').data('surveys'));

    collexTable.clear().draw();
    collexTable.rows.add(getCollexFromSurveyId(surveys, id)).draw();

    $("#modal-collex").modal("toggle");

    $("#collex-datatable tbody").on("click", "tr", function() {
        const id = collexTable.row(this).id();
        collexID = $("#collex-id").data("collex")

        if (typeof id !== "undefined") {
            if (typeof collexID == "undefined") {
                window.location.href = 'collection-exercise/' + id;
            } else {
                window.location.href = id;
            }

        }
    });
}

function getCollexFromSurveyId(surveys, survey_id) {

    for (let i = 0; i < surveys.length; i++) {
        if (surveys[i].surveyId === survey_id) {
            let collectionExercises = surveys[i].collectionExercises;
            return collectionExercises;
        }
    }
}

$(document).ready(function() {
    initiliseDataTables();
});
