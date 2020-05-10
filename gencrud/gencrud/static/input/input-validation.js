class AbstractInputValidation {
	valid() { throw new Error('Not inplementation!'); }
	invalid() { throw new Error('Not inplementation!'); }
	validHTML() { throw new Error('Not inplementation!'); }
	invalidHTML() { throw new Error('Not inplementation!'); }
	show() { throw new Error('Not inplementation!'); }
	hide() { throw new Error('Not inplementation!'); }
}

class InputValidation extends AbstractInputValidation {
	constructor(input) {
		super();
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


class AbstractInputComponent {
	hasComponent() { throw new Error('Not inplementation!'); }
	isValid() { throw new Error('Not inplementation!'); }
	validationShow() { throw new Error('Not inplementation!'); }
}


class BaseInput extends AbstractInputComponent {
	constructor(input) {
		super();
		this.input = input;
	}

	hasComponent() { return this.input.name === this.component.named && this.input.tagName.toLowerCase() === 'input'; }
	isValid() { return this.hasComponent(); }
	validationShow() {
		const inputValidation = new InputValidation(this.input);
		inputValidation.hide();
		inputValidation.show('ok', true);
	}
}


class InputEmail extends BaseInput {
	constructor(input) {
		super(input);
		this.component = InputEmailGroupComponent;
	}

	isValid() {
		const isEmpty = !Boolean(this.input.value);
		const isValidValue = isValidEmail(this.input.value);
		const isValid = (this.hasComponent() && !isEmpty && isValidValue);
		return isValid;
	}

	validationShow() {
  		if (this.hasComponent()) {
			const inputValidation = new InputValidation(this.input)
			inputValidation.hide();

			const isEmpty = !Boolean(this.input.value);
			const isValidValue = isValidEmail(this.input.value);

  			switch(true) {
  				case isEmpty:
  					inputValidation.show('Поле обязательно для заполнения', false);
  					break;
  				case !isValidValue:
  					inputValidation.show('Поле не является EMAIL адресом!', false);
  					break;
  				default:
  					inputValidation.show('ok', true);
  			}
  		}
	}
}


class InputPhone extends BaseInput {
	constructor(input) { 
		super(input);
		this.component = InputEmailGroupComponent;
	}
}


function isValidEmail (string) {
 	return string && Boolean(string.includes('@'));
}