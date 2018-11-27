/*jshint esversion: 6 */
function getReportSEFT(response) {
    const report = {
        "accountsPending": {
            "id": "accounts-pending",
            "title": "Accounts Pending",
            "value": response.report.accountsPending,
            "class": "fa fa-user-plus"
        },
        "accountsEnrolled": {
            "id": "accounts-enrolled",
            "title": "Accounts Enrolled",
            "value": response.report.accountsEnrolled,
            "class": "fa fa-users"
        },
        "downloads": {
            "id": "downloads",
            "title": "Downloads",
            "value": response.report.downloads,
            "class": "fa fa-download"
        },
        "uploads": {
            "id": "uploads",
            "title": "Uploads",
            "value": response.report.uploads,
            "class": "fa fa-upload"
        },
        "sampleSize": {
            "id": "sample-size",
            "title": "Sample Size",
            "value": response.report.sampleSize,
            "class": "fa fa-sitemap fa-color-white"
        }
    };

    return report;
}

function getReportEQ(response) {
    const report = {
        "accountsPending": {
            "id": "accounts-pending",
            "title": "Accounts Pending",
            "value": response.report.accountsPending,
            "class": "fa fa-user-plus"
        },
        "accountsEnrolled": {
            "id": "accounts-enrolled",
            "title": "Accounts Enrolled",
            "value": response.report.accountsEnrolled,
            "class": "fa fa-users"
        },
        "notStarted": {
            "id": "not-started",
            "title": "Not Started",
            "value": response.report.notStarted,
            "class": "fa fa-times"
        },
        "inProgress": {
            "id": "in-progress",
            "title": "In Progress",
            "value": response.report.inProgress,
            "class": "fa fa-spinner"
        },
        "uploads": {
            "id": "completed",
            "title": "Completed",
            "value": response.report.completed,
            "class": "fa fa-check"
        },
        "sampleSize": {
            "id": "sample-size",
            "title": "Sample Size",
            "value": response.report.sampleSize,
            "class": "fa fa-sitemap fa-color-white"
        }
    };

    return report;
}

function displayCollectionInstrumentData(collectionInstrumentType, response) {

    const timeUpdated = moment.unix(response.metadata.timeUpdated).calendar(); // eslint-disable-line
    let report = {};

    if (collectionInstrumentType.toLowerCase() === "eq") {
        report = getReportEQ(response);
    } else {
        report = getReportSEFT(response);
    }
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
            $(`#${report[figure].id}-counter`).effect("bounce", "slow");
        }
    }
    /* eslint-enable */

    const progress = (report.uploads.value / report.sampleSize.value * 100).toFixed(2);

    $("#sample-size-box").removeClass("bg-ons-light-blue").addClass("bg-ons-blue");
    $("#progress-uploaded").text(report.uploads.value);
    $("#time-updated").text(timeUpdated);
    $("#progress-size").text(report.sampleSize.value);
    $("#collex-progress").text(`${progress}%`).css("width", `${progress}%`);
}

function callAPI() {
    const collexID = $("#collex-id").data("collex");
    const surveyID = $("#collex-id").data("survey");
    const reportingRefreshCycleInSeconds = $("#collex-id").data("reporting-refresh-cycle");
    const collectionInstrumentType = $("#collex-id").data("collection-instrument-type");

    $.ajax({
        dataType: "json",
        url: `/dashboard/reporting/${collectionInstrumentType}/survey/${surveyID}/collection-exercise/${collexID}`
    }).done((result) => {

        $(".content-header").show();
        $(".content").show();
        $("#error-reporting").hide();
        $("#loading").hide();
        $("#time-updated-label").show();

        displayCollectionInstrumentData(collectionInstrumentType, result);
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
