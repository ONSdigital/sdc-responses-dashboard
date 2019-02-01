function setDataTableHeaderWidth() {
	// sets the width of the data table headers to 100%
	$(".dataTables_scrollHeadInner table").css("width", "100%");
}


function setCollexTableHeight() {
    // Dynamically set scroller rowHeight
	let checkCollexTableExist = setInterval(function () {
		let height = $("#collex-datatable tbody").height();
		if (height) {
			// sets the height of next div which follows the collex-datatable element
			$("#collex-datatable + div").height(height + 1);
			// sets the width of the headers to 100%
			setDataTableHeaderWidth();
			clearInterval(checkCollexTableExist);
		}
	}, 100);
}

function setDataTableDimension() {

    setCollexTableHeight();
    setDataTableHeaderWidth();

}

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
		scrollY: "35vh",
		scrollCollapse: true,
		scroller: {
			loadingIndicator: false
		}
	});
	/* eslint-enable */

	setDataTableHeaderWidth();

	$("#survey-search").keyup(function () {
		surveyTable.search($(this).val()).draw();
	});

	let dateRender = (data, type, row, meta) => {
		if (type === "sort" || type === "type") {
			return data;
		} else {
			return moment(data).format("DD-MM-YYYY"); // eslint-disable-line no-undef
		}
	};

	/* eslint-disable */
	const collexTable = $("#collex-datatable").DataTable({
		paging: true,
		lengthChange: false,
		searching: true,
		ordering: true,
		info: true,
		autoWidth: false,
		autoHeight: false,
		scrollY: "35vh",
		scrollCollapse: true,
		scroller: {
			loadingIndicator: false,
			rowHeight: 40
		},
		data: [],
		order: [
			[1, 'desc'],
			[2, 'desc']
		],
		columns: [{
				"data": "userDescription",
				"defaultContent": "No description provided",
				"title": "Collection Exercise Period",
				"width": "50%"
			},
			{
				"data": "scheduledExecutionDateTime",
				"defaultContent": "No go live provided",
				"title": "Go Live Date",
				"width": "25%",
				"render": dateRender
			},
			{
				"data": "scheduledReturnDateTime",
				"defaultContent": "No return by date provided",
				"title": "Return By Date",
				"width": "25%",
				"render": dateRender
			}
		],
		rowId: 'collectionExerciseId'
	});
	/* eslint-enable */

	$("#collex-search").keyup(function () {
		collexTable.search($(this).val()).draw();
	});

	$("#survey-datatable tbody").on("click", "tr", function () {
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
	// Dynamically set scroller rowHeight
	let checkCollexTableExist = setInterval(function () {
		let height = $("#collex-datatable tbody").height();
		if (height) {
			// sets the height of next div which follows the collex-datatable element
			$("#collex-datatable + div").height(height + 1);
			// sets the width of the headers to 100%
			setDataTableHeaderWidth();
			clearInterval(checkCollexTableExist);
		}
	}, 100);

	$("#collex-datatable tbody").on("click", "tr", function () {
		let id = collexTable.row(this).id();
		let collexID = $("#collex-id").data("collex");

		if (typeof id !== "undefined") {
			if (typeof collexID == "undefined") {
				window.location.href = `/dashboard/collection-exercise/${id}`;
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
				if (collectionExercises[collex].userDescription === "") {
					collectionExercises[collex].userDescription = "No description provided"; // eslint-disable-line
				}
			}

			return collectionExercises;
		}
	}
}

$(document).ready(() => {
	initialiseDataTables();
});
