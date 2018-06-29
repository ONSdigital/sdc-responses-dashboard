/*jshint esversion: 6 */
function callAPI(collexID = $("#collex-id").data("collex"), enableTimeout = true) {

	const reportingURL = $("#collex-id").data("reporting-url");
	const reportingRefreshCycle = $("#collex-id").data("reporting-refresh-cycle");

	$.ajax({
		url: reportingURL + "reporting-api/v1/response-dashboard/collection_exercise/" + collexID
	}).done((result) => {
		const downloads = result.report.downloads;
		const uploads = result.report.uploads;
		const accountsEnrolled = result.report.accountsEnrolled;
		const sampleSize = result.report.sampleSize;
		const timeUpdated = moment.unix(result.metadata.timeUpdated).calendar(); // eslint-disable-line
		const progress = (uploads / sampleSize * 100).toFixed(2);

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
	});
}

function loadDataTable() {

	/* eslint-disable */
	let dTable = $("#surveys").DataTable({ 
		"paging": true,
		"lengthChange": false,
		"searching": true,
		"ordering": true,
		"info": true,
		"autoWidth": false,
		"autoHeight": false,
		"scrollY": 300,
		"scroller": {
			loadingIndicator: false
		}
	});
	/* eslint-enable */

	$("#survey-search").keyup(function() {
		dTable.search($(this).val()).draw();
	});

	$("#surveys tbody").on("click", "tr", function() {
		const surveyLongName = $(this).data("survey-long-name");
		const surveyShortName = dTable.row(this).data()[0];
		const collectionExercise = dTable.row(this).data()[2];
		const id = dTable.row(this).id();

		$("#collex-id").data("collex", id);
		$("#survey-short-name").text(surveyShortName + " | " + collectionExercise);
		$("#survey-long-name").text(surveyLongName);
		$("#modal-default").modal("toggle");

		callAPI(id, false);
	});
}

$(document).ready(function() {
	callAPI();
	loadDataTable();
});
