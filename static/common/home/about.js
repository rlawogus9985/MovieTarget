const targets = document.querySelectorAll('[data-observer]')

const options = {
  rootMargin: '0px',
  threshold: 1.0
}

const addClass = (el) => {
	if (!el.classList.contains('is-visible')) {
		el.classList.add('is-visible')
	}
}

const removeClass = (el) => {
	if (el.classList.contains('is-visible')) {
		el.classList.remove('is-visible')
	}
}

const doThings = (entries, observer) => {
	entries.forEach(entry => {
		if (entry.isIntersecting) {
			addClass(entry.target)
		} else {
			removeClass(entry.target)
		}
  })
}

const observer = new IntersectionObserver(doThings, options)

const observer2 = new IntersectionObserver(doThings, { ...options, threshold: 0.4 })

targets.forEach(target => {
	observer.observe(target)
})

images.forEach(target => {
	observer2.observe(target)
})

