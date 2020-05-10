/*
 * import: input/input-components.js
 * import: link/link-components.js
*/


const ClaimModalFormComponent = (userId, userEmail, userPhone) => {
    console.log('ClaimModalFormComponent: ', userId, userEmail, userPhone);

	const that = ClaimModalFormComponent;
	that.dataTarget = 'claim-modal';
	that.title = 'Быстрая заявка';
	that.action = '/order/fast-claim-form/create/';

	return {
		dataTarget: that.dataTarget,
		action: that.action,
		html: `<div id="${that.dataTarget}" tabindex="-1" role="dialog" class="modal fade">
        <div class="modal-dialog">
            <div class="modal-content form-claim-modal">
                <button type="button" data-dismiss="modal" aria-label="Close" class="close"><span aria-hidden="true">×</span></button>
                <h3 class="modal-title text-center">${that.title}</h3>
                <div class="modal-body">
                    
                    <ul class="errorlist small text-error"></ul>

                    <form action="${that.action}">
                        ${InputUserHiddenComponent(userId).html}
                        <div class="form-group"><p>Так мы быстрее отреагируем на ваш запрос!</p></div>
                        <div class="form-group">
                            <label for="id_typof_choices" class="">Выберите тип заявки:</label>
                            <div id="id_typof_choices" class="btn-group btn-group-toggle" data-toggle="buttons">
                                <label for="id_typeof-0" class="btn btn-outline-secondary">
                                    <input type="radio" name="typeof" id="id_typeof-0" autocomplete="off" value="0"> Позвони мне
                                </label>
                                
                                <label for="id_typeof-1" class="btn btn-outline-secondary">
                                    <input type="radio" name="typeof" id="id_typeof-1" autocomplete="off" value="1"> Заявка на проект
                                </label>
                                
                                <label for="id_typeof-2" class="btn btn-outline-secondary">
                                    <input type="radio" name="typeof" id="id_typeof-2" autocomplete="off" value="2"> Другое
                                </label>
                            </div>
                        </div>
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
