window.addEventListener('DOMContentLoaded', e => {
	const form = document.querySelector("[data-form='main-form']");
	console.log(form);
	form.addEventListener('submit', handleFormSubmission);
});

const handleFormSubmission = e => {
	const input_els = Array.from(document.querySelectorAll('input'));
	for (let input of input_els) {
		if (!validateInput(input)) {
			e.preventDefault();
			input.value = '';
		}
	}
	e.target.classList.add('was-validated');
};

const validateInput = input => {
	return input.value.length >= 3;
};
