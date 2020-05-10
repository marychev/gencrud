/*
 * import: input/input-components.js: 
 * 		InputEmail, InputPhoneGroupComponent, TextareaCommentGroupComponent, SubmitButtonComponent,
 * import: input/input-validation.js: InputValidation,
*/

class BaseEventListener extends BaseModalForm {
	constructor(component) {
		super(component);
	}

	static postSuccess(textSuccess, wrapperForm) {
		const titleForm = wrapperForm.title;
		const formControls = wrapperForm.form.querySelectorAll('.form-control');

		wrapperForm.isSent = true;
		wrapperForm.buttonSubmitDisabled(true);

		titleForm.innerHTML = textSuccess;
		titleForm.classList.add('text-success');

	    Array.prototype.forEach.call( formControls, (node) => {
			new InputValidation(node).valid();
		});

	    sleep(2500).then(() => {
			$(`#${wrapperForm.id}`).modal('hide');  
			wrapperForm.remove();
	    });
	}


	static postError(errors, wrapperForm)	{
		for (let name in errors)  {
			switch (name) {
				case 'email':
					const inpEmail = wrapperForm.inputEmail();
					const inputEmailValudation = new InputValidation(inpEmail);
					inputEmailValudation.show(errors[name]);
					break;	
				case 'typeof':
					const inpTypeofChoices = wrapperForm.inputTypeofChoices();
				    const inputTypeofChoicesValudation = new InputValidation(inpTypeofChoices);
	        		inputTypeofChoicesValudation.show(errors[name]);
	        		break;
				default:
					return null;
			}
	    }
	}
	
	inputEmail() { return this.form.querySelector('input[id="id_email"]'); }
	inputPhone(){ return this.form.querySelector('input[id="id_phone"]'); }
	inputComment() { return this.form.querySelector('textarea[id="id_comment"]'); }
	buttonSubmit() { return this.form.querySelector(`button[type="${SubmitButtonComponent.type}"]`); }

	buttonSubmitDisabled(isDisable) { 
		const btnSubmit = this.buttonSubmit();
		btnSubmit.disabled = isDisable;
	}

	isValidEmail(input, showValidation = true) {
		const inputEmail = new InputEmail(input);
		showValidation && inputEmail.validationShow();
		return inputEmail.isValid();
	}

	onBlurEmail(event) {
		const inputEmail = new InputEmail(event.target);
		inputEmail.validationShow();
		this.isValid();
	}
	
	isValidPhone(input) {
		return (
			input.name === InputPhoneGroupComponent.named 
			&& input.tagName.toLowerCase() === 'input'
		);
	}

	onBlurPhone(event) {
		this.isValidPhone(event.target) && this._showValidInput(event.target);
		this.isValid();
	}

	isValidComment(input) {
		return (
			input.name === TextareaCommentGroupComponent.named 
			&& input.tagName.toLowerCase() === TextareaCommentGroupComponent.type
		);
	}

	onBlurComment(event) {
		this.isValidComment(event.target) && this._showValidInput(event.target);
		this.isValid();
	}

	onClickSubmit(event) {
		event.preventDefault();
	
		const tagName = event.target && event.target.tagName.toLowerCase();
		const hasSubmit = (
			SubmitButtonComponent.type === event.target.getAttribute('type') && tagName === 'button');

		if (hasSubmit) {
			const that = this;
			const formData = that.formData;
			
			// delete formData["csrfmiddlewaretoken"]; # no delete!

			$.post(this.component.action, formData).done(function (data) {
				console.log('post ->', data);
				if (data.success) {
					BaseEventListener.postSuccess(data.success, that);
				} else { 
					BaseEventListener.postError(data.errors, that);
				}
			});
		}
	}

	listenerEvents(event) {
		this.onBlurEmail(event);	
		this.onBlurPhone(event);
		this.onBlurComment(event);
		this.onClickSubmit(event);
	}

	clean() {
		this.inputEmail().value = '';
		this.inputPhone().value = '';
		this.inputComment().value = '';

		new InputValidation(this.inputEmail()).hide();
		new InputValidation(this.inputPhone()).hide();
		new InputValidation(this.inputComment()).hide();
	}

	_showValidInput(input) {
		const inputValidation = new InputValidation(input);
		
		inputValidation.hide();
		inputValidation.show('ok', true);
	}	
	
}