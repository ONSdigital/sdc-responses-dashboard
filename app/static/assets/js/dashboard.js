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

$(document).ready(function() {
    callAPI();
});
