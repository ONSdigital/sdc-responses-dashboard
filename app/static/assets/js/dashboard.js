/*jshint esversion: 6 */
function callAPI(collexID = $("#collex-id").data("collex"), enableTimeout = true) {
    const reportingURL = $("#collex-id").data("reporting-url");
    const reportingRefreshCycle = $("#collex-id").data("reporting-refresh-cycle");
    const collectionInstrumentType = $("#collex-id").data("collection-instrument-type");

    $.ajax({
        dataType: "json",
        url: reportingURL + "reporting-api/v1/response-dashboard/" + collectionInstrumentType + "/collection-exercise/" + collexID
    }).done((result) => {

        $('#error-reporting').hide();
        $('.content').show();

        displayCollectionInstrumentData(collectionInstrumentType, result);

    }).fail((result) => {
        $('#error-reporting').show();
        $('.content').hide();
    }).always(function() {
        if (enableTimeout) {
            setTimeout(callAPI, reportingRefreshCycle);
        }
    });
}

function displayCollectionInstrumentData(collectionInstrumentType, response) {

    const timeUpdated = moment.unix(response.metadata.timeUpdated).calendar(); // eslint-disable-line
    let report = {};

    if (collectionInstrumentType.toLowerCase() == 'eq') {
        report = getReportEQ(response);
    } else {
        report = getReportSEFT(response);
    }

    const progress = (report.uploads.value / report.sampleSize.value * 100).toFixed(2);

    $("#progress-uploaded").text(report.uploads.value);
    $("#time-updated").text(timeUpdated);
    $("#progress-size").text(report.sampleSize.value);
    $("#collex-progress").text(progress + "%").css("width", progress + "%");

    $('#counters').empty();

    for (let figure in report) {
        $('#counters').append($('<div>', {
            'class': 'col-lg-6 col-xs-6'
        }).append($('<div>', {
            'class': 'small-box bg-ons-light-blue'
        }).append([$('<div>', {
            'class': 'inner'
        }).append([$('<h3>', {
            'id': report[figure].id + '-counter'
        }).text(report[figure].value), $('<p>').text(report[figure].title)]), $('<div>', {
            'class': 'icon'
        }).append($('<i>', {
            'class': report[figure].class
        }))])));
        $('#' + report[figure].id + '-counter').effect("bounce", "slow");
    }
}

function getReportSEFT(response) {
    const report = {
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
        "accountsEnrolled": {
            "id": "accounts-enrolled",
            "title": "Accounts Enrolled",
            "value": response.report.accountsEnrolled,
            "class": "fa fa-users"
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
        "accountsCreated": {
            "id": "accounts-created",
            "title": "Accounts Created",
            "value": response.report.accountsCreated,
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

$(document).ready(function() {
    callAPI();
});
