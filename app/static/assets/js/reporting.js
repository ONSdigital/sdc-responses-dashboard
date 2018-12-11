/*jshint esversion: 6 */
function getReport(response) {
    const report = {
        "accountsPending": {
            "id": "accounts-pending",
            "title": "Accounts Pending",
            "value": response.report.accountsPending,
            "class": "fa fa-user-plus",
            "tooltip": {
                "placement": "bottom",
                "title": "For an <strong>eQ</strong>; This is a total number of cases where a questionnaire has been successfully submitted and receipted. <p />For a <strong>SEFT</strong>; This is the total number of cases where a collection instrument has been successfully uploaded."
            }
        },
        "accountsEnrolled": {
            "id": "accounts-enrolled",
            "title": "Accounts Enrolled",
            "value": response.report.accountsEnrolled,
            "class": "fa fa-users",
            "tooltip": {
                "placement": "bottom",
                "title": "For an <strong>eQ</strong>; This is a total number of cases where a questionnaire has been successfully submitted and receipted. <p />For a <strong>SEFT</strong>; This is the total number of cases where a collection instrument has been successfully uploaded."
            }
        },
        "notStarted": {
            "id": "not-started",
            "title": "Not Started",
            "value": response.report.notStarted,
            "class": "fa fa-times",
            "tooltip": {
                "placement": "bottom",
                "title": "For an <strong>eQ</strong>; This is a total number of cases where a questionnaire has been successfully submitted and receipted. <p />For a <strong>SEFT</strong>; This is the total number of cases where a collection instrument has been successfully uploaded."
            }
        },
        "inProgress": {
            "id": "in-progress",
            "title": "In Progress",
            "value": response.report.inProgress,
            "class": "fa fa-spinner",
            "tooltip": {
                "placement": "bottom",
                "title": "For an <strong>eQ</strong>; This is a total number of cases where a questionnaire has been successfully submitted and receipted. <p />For a <strong>SEFT</strong>; This is the total number of cases where a collection instrument has been successfully uploaded."
            }
        },
        "completed": {
            "id": "completed",
            "title": "Completed",
            "value": response.report.completed,
            "class": "fa fa-check",
            "tooltip": {
                "placement": "bottom",
                "title": "For an <strong>eQ</strong>; This is a total number of cases where a questionnaire has been successfully submitted and receipted. <p />For a <strong>SEFT</strong>; This is the total number of cases where a collection instrument has been successfully uploaded."
            }
        },
        "sampleSize": {
            "id": "sample-size",
            "title": "Sample Size",
            "value": response.report.sampleSize,
            "class": "fa fa-sitemap fa-color-white",
            "tooltip": {
                "placement": "bottom",
                "title": "For an <strong>eQ</strong>; This is a total number of cases where a questionnaire has been successfully submitted and receipted. <p />For a <strong>SEFT</strong>; This is the total number of cases where a collection instrument has been successfully uploaded."
            }
        }
    };

    return report;
}

function displayCollectionExerciseData(response) {

    const timeUpdated = moment.unix(response.metadata.timeUpdated).calendar(); // eslint-disable-line
    let report = getReport(response);

    $("#counters").empty();
    /* eslint-disable */
    for (const figure in report) {
        if (report.hasOwnProperty(figure)) {

            let layoutClass = Object.keys(report).length % 2 && figure === "sampleSize" ? "col-lg-12 col-xs-12" : "col-lg-6 col-sm-6 col-xs-12";

            $("#counters").append($("<div>", {
                "class": layoutClass
            }).append($("<div>", {
                "class": "small-box bg-ons-light-blue",
                "id": `${report[figure].id}-box`
            }).append([$("<div>", {
                "class": "inner"
            }).append([$("<h3>", {
                "id": `${report[figure].id}-counter`
            }).text(report[figure].value), $("<p>").text(report[figure].title)]), $("<div>", {
                "class": "icon"
            }).append($("<i>", {
                "class": report[figure].class
            }))])));

            // Adds a minimal bounce animation to each counter
            $(`#${report[figure].id}-counter`).effect("bounce", "slow");

            // Adds a tooltip to each counter
            $(`#${report[figure].id}-box`).tooltip({
                "title": report[figure].tooltip.title,
                "placement": report[figure].tooltip.placement,
                "html": true
            });
        }
    }

    /* eslint-enable */

    const progress = ((report.completed.value / report.sampleSize.value * 100) || 0).toFixed()

    $("#sample-size-box").removeClass("bg-ons-light-blue").addClass("bg-ons-blue");
    $("#progress-uploaded").text(report.completed.value);
    $("#time-updated").text(timeUpdated);
    $("#progress-size").text(report.sampleSize.value);

    if (progress > 1) {
        $("#collex-progress").text(`${progress}%`).css("width", `${progress}%`);
    }

}

function callAPI() {
    const collexID = $("#collex-id").data("collex");
    const surveyID = $("#collex-id").data("survey");
    const reportingRefreshCycleInSeconds = $("#collex-id").data("reporting-refresh-cycle");

    $.ajax({
        dataType: "json",
        url: `/dashboard/reporting/survey/${surveyID}/collection-exercise/${collexID}`
    }).done((result) => {

        $(".content-header").show();
        $(".content").show();
        $("#error-reporting").hide();
        $("#loading").hide();
        $("#time-updated-label").show();

        displayCollectionExerciseData(result);
    }).fail((result) => {
        $("#loading").hide();
        $(".content-header").hide();
        $(".content").hide();
        $("#error-reporting").show();
    }).always(() => {
        if (reportingRefreshCycleInSeconds > 1) {
            setTimeout(callAPI, reportingRefreshCycleInSeconds * 1000);
        }
    });
}

$(document).ready(() => {
    callAPI(); // eslint-disable-line
});
