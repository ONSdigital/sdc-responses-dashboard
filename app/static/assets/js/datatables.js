function initialiseDataTables() {

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
            "defaultContent": "No description provided",
            "title": "Collection Exercise Period",
            "width": "300px"
        },
        {
            "data": "periodStartDateTime",
            "defaultContent": "No start date provided",
            "title": "Start Date",
            "width": "300px"
        },
        {
            "data": "periodEndDateTime",
            "defaultContent": "No end date provided",
            "title": "End Date",
            "width": "300px"
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
    /**
     *  Load the collection exercise data into the data table
     */

    const surveys = JSON.parse($('#collex-id').data('surveys'));

    collexTable.clear().draw();
    collexTable.rows.add(getCollexFromSurveyId(surveys, id)).draw();

    $("#modal-collex").modal("toggle");

    $("#collex-datatable tbody").on("click", "tr", function() {
        let id = collexTable.row(this).id();
        let collexID = $("#collex-id").data("collex");

        if (typeof id !== "undefined") {
            if (typeof collexID == "undefined") {
                window.location.href = '/dashboard/collection-exercise/' + id;
            } else {
                window.location.href = id;
            }

        }
    });
}

function getCollexFromSurveyId(surveys, survey_id) {
    /**
     *  Returns an array of collection exercises for a given survey id
     */

    for (let i = 0; i < surveys.length; i++) {
        if (surveys[i].surveyId === survey_id) {
            let collectionExercises = surveys[i].collectionExercises;

            for (let collex in collectionExercises) {
                if (collectionExercises[collex].userDescription === "" ) {
                    collectionExercises[collex].userDescription = "No description provided"
                }
            }

            return collectionExercises;
        }
    }
}

$(document).ready(function() {
    initialiseDataTables();
});
