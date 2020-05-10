class InputValidation {
	constructor(input) {
		this.input = input;
	}

	valid() { this.input.classList.add("is-valid"); }
	invalid() { this.input.classList.add("is-invalid"); }

	validHTML(message) {
		this.valid();
		return `<div class="valid-feedback">${message}</div>`;
	}

	invalidHTML(message) {
		this.invalid();
		return `<div class="invalid-feedback">${message}</div>`;
	}

	show(message = '', isValid=false) {
		const html = isValid ? this.validHTML(message) : this.invalidHTML(message);
		
		this.input.classList.add("form-control");
		this.input.insertAdjacentHTML('afterend', html);
	}

	hide() {
		this.input.classList.remove("is-valid");
		this.input.classList.remove("is-invalid");

		const invalidNodeList = this.input.closest('div').querySelectorAll('.invalid-feedback');
		const validNodeList = this.input.closest('div').querySelectorAll('.valid-feedback');

		Array.prototype.forEach.call( invalidNodeList, (node) => {
    		node.parentNode.removeChild(node);
		});

		Array.prototype.forEach.call( validNodeList, (node) => {
    		node.parentNode.removeChild(node);
		});
	}
}
