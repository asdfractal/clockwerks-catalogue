// prettier-ignore
const heroIdList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129]
// prettier-enable
const heroFilterTitle = $(".hero-filter-title")
const heroFilterButton = $(".js-filter-button")
const loadingSpinner = $("#loadingOverlay")

/**
 * Sends a query to server to filter heroes by attribute.
 * @async
 * @param {string} query the attribute to filter by
 * @returns {object} JSON data from the response
 */
const queryApi = async (query) => {
	const queryUrl = `/api/heroes/?attr=${query}`
	loadingSpinner.show()
	try {
		const res = await fetch(queryUrl)
		return await res.json()
	} catch {
		$("#errorMessage").text(
			"There was an error contacting the server. Please try again later.",
		)
		return false
	}
}

/**
 * Processes the data from the response and creates and array from the values. Then applies filter to relevant elements.
 * @async
 * @param {string} query the attribute to filter by
 */
const processData = async (query) => {
	const data = await queryApi(query)
	if (data === false) {
		loadingSpinner.hide()
		heroFilterButton.removeClass("hero-filter-active")
		return
	}
	const dataValues = []
	for (const id of Object.values(data)) {
		dataValues.push(id)
	}
	filterHeroes(dataValues)
	loadingSpinner.hide()
}

/**
 * Hides all heroes and then shows matching heroes.
 * @param {array} heroes array of hero IDs to filter
 */
const filterHeroes = (heroes) => {
	$(".hero-thumbnail").hide()
	heroes.forEach((id) => {
		$(`#${id}`).parent().parent().show()
	})
	heroFilterTitle.text(`${_this.id}`).addClass("mb-3")
}

/**
 * Clears hero filter to show full list.
 */
const clearFilter = () => {
	$(".hero-thumbnail").show()
	_this.classList.remove("hero-filter-active")
	heroFilterTitle.text("").removeClass("mb-3")
}

/**
 * Adds click event to filter elements, creates a query parameter and updates DOM.
 */
document.querySelectorAll(".js-filter-button").forEach((element) => {
	element.addEventListener("click", function () {
		_this = this
		if (this.classList.contains("hero-filter-active")) {
			clearFilter()
		} else {
			heroFilterButton.removeClass("hero-filter-active")
			query = this.id
			this.classList.add("hero-filter-active")
			processData(query)
		}
	})
})

/**
 * Adds click event to each individual item on favourite list to toggle the note input for that hero.
 * @param {array} heroIds complete list of hero IDs
 */
const heroNoteToggler = (heroIds) => {
	heroIds.forEach((id) => {
		$(`#${id}-toggler`).click(() => {
			$(`#${id}`).toggle()
		})
	})
}

$(".toast").toast("show")

$(document).ready(function () {
	heroNoteToggler(heroIdList)

	$(document).click(function () {
		$(".navbar-collapse").collapse("hide")
	})
})
