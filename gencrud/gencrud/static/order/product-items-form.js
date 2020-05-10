class ProductItemsClaimForm extends ProductClaimForm {
	constructor(component) {
		super(component);

		this.isValid.bind(this);
		this.open.bind(this);
		this.setForm.bind(this);
	}

	isValid() {
		const inputEmail = this.inputEmail();
		const isValidEmail = this.isValidEmail(inputEmail);
		
		const isDisable = !(isValidEmail  && !this.isSent);
		this.buttonSubmitDisabled(isDisable);
		
		return isDisable;
	}

	open(event) {
		this.productId = Number(event.target.dataset.productPk);
		this._needSetForm(event) ? this.setForm(event) : null; 
	}

	setForm(event) {
		this.fetchGetProduct(this.productId);

		const that = this;
		const modalForm = that.form || (
			document.getElementById(that.dataTarget) && document.getElementById(that.dataTarget).getElementsByTagName('form')[0]
		);
		
		let checkoxesHTML = [];

		this._checkedCheckboxesOnPage().forEach(function(node) {
			const productItemId = node.value;
			const productItemTitle = node.parentNode.querySelector(`label[for="${node.id}"]`).innerText;
			const checkbox = CustomCheckboxGroupComponent(productItemId, productItemTitle, true);
			
			checkoxesHTML.push(checkbox.html);
		});

		const profileData = getHiddenProfileData();
		const componentHTML = ProductClaimModalFormComponent(
			profileData.id, 
			profileData.email, 
			profileData.phone,
			this.productId, 
			checkoxesHTML
		).html;

		document.body.insertAdjacentHTML('afterend', componentHTML);
		this.wrapperNode.addEventListener('click', this.listenerEvents.bind(this));
	}

	_needSetForm(event) {
		const checkedOnPage = this._checkedCheckboxesOnPage();
		const checkedOnModal = this._checkedCheckboxesOnModal();
		return checkedOnPage.length !== checkedOnModal.length;
	}

	_checkedCheckboxesOnPage() {
		const named = CustomCheckboxGroupComponent().named;
		console.log('named', named)
		const productItemQS = `input[name="${named}"]`;
		return document.querySelectorAll(`${productItemQS}:checked`);
	}
	
	_checkedCheckboxesOnModal() {
		const namedModal = CustomCheckboxGroupComponent().namedModal;
		const productItemQSModal = `input[name="${namedModal}"]`;
		return document.querySelectorAll(`${productItemQSModal}:checked`);
	}

	_removeCheckboxesOnModal() {
		const namedModal = CustomCheckboxGroupComponent().namedModal;
		const firstInput = document.querySelector(`input[name="${namedModal}"]`);
		const formGroupCheckboxes = firstInput && firstInput.closest('.form-group');

		if (formGroupCheckboxes) {
			formGroupCheckboxes.parentNode.removeChild(formGroupCheckboxes);
		}
	}
}