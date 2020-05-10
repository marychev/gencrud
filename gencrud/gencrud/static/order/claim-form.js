class ClaimFormModal extends BaseEventListener {
	constructor(component) {
		super(component);

		this.isValid.bind(this);
		this.open.bind(this);
		this.setForm.bind(this);
	}

	inputTypeofChoices() { return this.form.querySelector('label[for="id_typof_choices"]'); }
	
	isValid() {
		const fields = ['user', 'typeof', 'email', 'phone', 'comment'];

		const inputEmail = this.inputEmail();
		const isValidEmail = this.isValidEmail(inputEmail);

		const isDisable = !(this.formData.length === fields.length && isValidEmail && !this.isSent);
		this.buttonSubmitDisabled(isDisable);

		// todo: need to fix: console.log('ClaimFormModal.isValid:', isDisable);

		return isDisable;
	}

	isValidTypeof(input) {
		const children = input.children;
		const isTarget = children.length > 0 && children[0].name === 'typeof';

		return isTarget && (children[0].getAttribute('type') === 'radio');
	}

	validationTypeof(input) { }

	onClickTypeof(event) {		
		if (this.isValidTypeof(event.target)) {
			const inputTypeof = this.inputTypeofChoices();
			const inputValidation = new InputValidation(inputTypeof);

			inputValidation.hide();
			inputValidation.show('ok', true);

			const radioInput = event.target.children;
			radioInput[0].checked = true;
		}

		this.isValid();
	}

	listenerEvents(event) {
		super.listenerEvents(event);
		this.onClickTypeof(event);
	}
}
