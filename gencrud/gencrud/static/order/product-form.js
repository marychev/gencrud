class ProductClaimForm extends BaseEventListener {
	constructor(component, productId) {
		super(component);

		this.productId = productId;

		this.isValid.bind(this);
		this.open.bind(this);
		this.setForm.bind(this);
	}

	inputProduct() { return this.form.querySelector('input[id="id_product"]'); }
	
	open(event) {
		const prevProductId = this.form && Number(this.inputProduct().value);
		const currentProductId = Number(event.target.dataset.productPk);
		
		this.productId = currentProductId;
		(currentProductId !== prevProductId) ? this.setForm(event) : null; 
	}

	setForm(event) {
		this.fetchGetProduct(this.productId);
		console.log('ProductForm');

		const profileData = getHiddenProfileData();
		const componentHTML = ProductClaimModalFormComponent(
			profileData.id, 
			profileData.email, 
			profileData.phone,
			this.productId
		).html;
		document.body.insertAdjacentHTML('afterend', componentHTML);	
		this.wrapperNode.addEventListener('click', this.listenerEvents.bind(this));
	}

	isValid() {
		const fields = ['user', 'product', 'email', 'phone', 'comment'];

		const inputEmail = this.inputEmail();
		const isValidEmail = this.isValidEmail(inputEmail);
		
		const isDisable = !(this.formData.length === fields.length && isValidEmail && !this.isSent);
		this.buttonSubmitDisabled(isDisable);

		return isDisable;
	}

	fetchGetProduct(productId) {
		const url = `/api/products/${productId}/`;

		const that = this;
		$.get(url).done(function (data) {
			that.productId = data.id;
			that.title.innerText = data.title;
		});
	}
}