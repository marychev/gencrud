class ProductClaimForm extends ClaimForm {
	constructor(idForm, titleForm, productPk) {
		super(idForm, titleForm);

		this._productPk = productPk;
		this.whoCallQS = `[data-target="#${this.idForm}"]`;
		
		if (this.modalFormWrapper) {
			this.targetProduct = this.modalForm.querySelector('input[id="id_product"]');
		}
	
		this.addEventListeners();
	}

	addEventListeners() {
		const onClick = this.onClick.bind(this);
		const whoCanCall = document.querySelectorAll([this.whoCallQS]);
		
		if (this.modalFormWrapper) {
			this.modalForm.addEventListener('click', onClick);
		
			[...whoCanCall].forEach(function(node) {
				node.addEventListener('click', onClick);
			});

			this.modalForm.addEventListener('click', onClick);
		}
	}

	get productPk () { return this._productPk; }
	set productPk(pk) { this._productPk = Number(pk) };

	init(pk) {
		this.productPk = pk;

		let that = this;
		const url = `/api/products/${pk}/`;

		$.get(url).done(function (data) {
			that.productPk = data.id;
			that.targetProduct.value = pk;
			that.titleForm = data.title;
		});
	}

	cleanForm() {
		super.cleanForm();
		this.productPk = null;
	}

	/* handlers events */
	onClick(event) {
		const target = event && event.target;

		if (target && target.getAttribute('data-product-pk')) {
			this.init(target.dataset.productPk);
		}

		this.onClickEmail(target);
		this.onClickSubmit(target);
	}
}



class ProductItemsClaimForm extends ProductClaimForm {
	constructor(idForm, titleForm, productPk, productItemsPks) {
		super(idForm, titleForm, productPk);

		this._productItemsPks = productItemsPks;
	}

	get productItemsPks () { return this._productItemsPks; }
	set productItemsPks(productItemsPks) { this._productItemsPks = productItemsPks };
	
	onClickSubmit(target) {

		// hidden input that generat to djano
		let hiddenInputProductItems = this.modalForm.querySelector('input[id="id_product_items"]');
		if (hiddenInputProductItems && hiddenInputProductItems.parentNode) {
  			hiddenInputProductItems.parentNode.removeChild(hiddenInputProductItems);
		}
	}

	init() {
		super.init(this.productPk);

		const modalForm = this.modalForm;
		
		// -- @product_items -- 

		// clean old items in HTML
		const firstInput = modalForm.querySelector(`input[name="${PI_INPUT_NAME}"]`);
		const formGroupCheckboxes = firstInput && firstInput.closest('.form-group');
		if (formGroupCheckboxes) {
			formGroupCheckboxes.parentNode.removeChild(formGroupCheckboxes);
		}
		
		// init new items in HTML
		this.productItemsPks.forEach(function(pk) {
			const productItem = new ProductItem(pk);
			productItem.init(modalForm);
		});
	}

	onClick(event) {
		const productItemQS = `input[name="${P_INPUT_NAME}"]`;
		const claimProductItemQS = `input[name="${PI_INPUT_NAME}"]`;

		const target = event && event.target;
		// search on page (not modal form)
		const hasProductItems = target.parentNode && Boolean(target.parentNode.querySelector(productItemQS));
		// search on modal form (not page)
		const claimProductItems = this.modalForm.querySelectorAll(`${claimProductItemQS}:checked`);

		let selectedProductItemsIds = [];
		if (hasProductItems) {
			const allCkecked = target.parentNode.querySelectorAll(`${productItemQS}:checked`);

			allCkecked.forEach(function(node) {
				selectedProductItemsIds.push(node.value);
			});
			
			this.productPk = target.dataset.productPk; 
			this.productItemsPks = Array.from(new Set(selectedProductItemsIds));

			this.init();
		}

		if (claimProductItems) {
			claimProductItems.forEach(function(node) {
				selectedProductItemsIds.push(node.value);
			});
		}

		this.onClickSubmit(target);
	}
}

// init
// new ProductClaimForm('product-claim-form-modal');
// new ProductItemsClaimForm('product-claim-form-modal');


