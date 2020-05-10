const InputProductHiddenComponent = (productId) => {
    const that = InputProductHiddenComponent;
    that.id = 'id_product';
    that.named = 'product';

    return {
        value: productId,
        html: `<input type="hidden" name="${that.named}" id="${that.id}" value="${productId}">`
    }
};


const CustomCheckboxGroupComponent = (productVariantId, productTitle, isModal) => { 
    const that = CustomCheckboxGroupComponent;
    that.id = `product_item_${productVariantId}`;
    that.named = 'product_item';
    that.namedModal = `modal_${that.named}`;
    that.idModal = `modal_${that.named}_${productVariantId}`;
    that.type = 'checkbox';

    const id = isModal ? that.idModal : that.id;
    const named = isModal ? that.namedModal : that.named;

    return {
        id: id,
        named: named,
        namedModal: that.namedModal,
        html: `<div class="custom-control custom-checkbox">
            <input class="custom-control-input" type="${that.type}" id="${id}" name="${named}" value="${productVariantId}" checked="" />
            <label class="custom-control-label" for="${id}">${productTitle}</label>        
        </div>`,
    }
};


const ProductClaimModalFormComponent = (userId, userEmail, userPhone, productId, checkboxListHTML) => {
	const that = ProductClaimModalFormComponent;
	that.dataTarget = 'product-claim-form-modal';
	that.title = 'Заявка на проект';
	that.action = '/order/product-claim-form/create/';

	return {
		dataTarget: that.dataTarget,
		action: that.action,
		html: `<div id="${that.dataTarget}" role="dialog" class="modal fade" aria-modal="true">
        <div class="modal-dialog">
            <div class="modal-content form-claim-modal">
                <button type="button" data-dismiss="modal" aria-label="Close" class="close"><span aria-hidden="true">×</span></button>
                <h3 class="modal-title text-center">${that.title}</h3>
                <div class="modal-body">
                    <ul class="errorlist small text-error"></ul>
                    <form action="${that.action}">
                        <div class="form-group">
                            ${checkboxListHTML ? checkboxListHTML.join('') : ''}
                        </div>
                        ${InputUserHiddenComponent(userId).html}
                        ${InputProductHiddenComponent(productId).html}
                        ${InputEmailGroupComponent(userEmail).html}
                        ${InputPhoneGroupComponent(userPhone).html}
                        ${TextareaCommentGroupComponent().html}
                        ${SubmitButtonComponent().html}
                        ${ProfileLinkComponent().html}
                    </form>
                </div>
            </div>
        </div>
    </div>`
    }
};