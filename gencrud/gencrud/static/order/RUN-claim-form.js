const sleep = (milliseconds) => new Promise(resolve => setTimeout(resolve, milliseconds));


class ClaimForm {
	constructor(idForm) {
		this.idForm = idForm;

		this.modalFormWrapper = document.getElementById(this.idForm);
		if (this.modalFormWrapper) {
			this.modalForm = this.modalFormWrapper.getElementsByTagName('form')[0];
			this.action = this.modalForm && this.modalForm.getAttribute('action');

			this.targetUser = this.modalForm && this.modalForm.querySelector('input[id="id_user"]');
			this.targetEmail = this.modalForm && this.modalForm.querySelector('input[id="id_email"]');
			this.targetPhone = this.modalForm && this.modalForm.querySelector('input[id="id_phone"]');
			this.targetComment = this.modalForm && this.modalForm.querySelector('textarea[id="id_comment"]'); 
		} else {
			console.warn(`ID: #${this.idForm}: Wrapper for Form  doesn't found in DOM!`, this);
		}
	}

	get titleForm() { return this._titleForm || 'Быстрая заявка';}
	set titleForm(value) { 
		this._titleForm = value;
		this.modalFormWrapper.querySelector('.modal-title').innerHTML = value; 
	}

	cleanForm() {
		this.targetComment.value = '';

		new InputError(this.targetEmail).hide();
		new InputError(this.targetPhone).hide();
		new InputError(this.targetComment).hide();
	}

	post() {
		const postError = this.postError.bind(this);
		const postSuccess = this.postSuccess.bind(this);

		this.formData = $(this.modalForm).serializeArray();
	    delete this.formData["csrfmiddlewaretoken"];    

	    $.post(this.action, this.formData).done(function (data) {
	        data.success ? postSuccess(data.success) : postError(data.errors);
	    });
	}

	postSuccess(success) {
  		this.titleForm = success;
		this.modalFormWrapper.querySelector('.modal-title').classList.add('text-success');

        const formControls = this.modalFormWrapper.querySelectorAll('.form-control');
        Array.prototype.forEach.call( formControls, (node) => {
			node.classList.add("is-valid");
		});

        sleep(2500).then(() => {
			$(`#${this.modalFormWrapper.id}`).modal('hide');  
			this.cleanForm();              
        })
	}

	postError(errors) {
		for (let name in errors) {
        	if (name === 'email') {
				new InputError(this.targetEmail).show(errors[name]);
        	}
        }
	}

	onClickSubmit(target) {
		const tagName = target.tagName.toLowerCase();
		
		console.log('???', target);

		if ((tagName === 'button' || tagName === 'input')
			// && target.getAttribute('type') === 'submit'
		) {
			console.log('!!!');			
			event.preventDefault();
			// this.post();
			console.log('--- END ---');
		}
	}

	onClickEmail(target) {
		document.body.insertAdjacentHTML('afterend', HTMLModalForm());

		const INPUT_NAME = 'email';
		const tagName = target.tagName.toLowerCase();

		if (target.name === INPUT_NAME && tagName === 'input') {
			new InputError(target).hide();
		}
	}

}


function HTMLModalForm() {
	const layout = `<div id="claim-modal" tabindex="-1" role="dialog" class="modal fade jsFastClaimForm show">
        <div class="modal-dialog">
            <div class="modal-content form-claim-modal">
                <button type="button" data-dismiss="modal" aria-label="Close" class="close"><span aria-hidden="true">×</span></button>
                <h3 class="modal-title text-center">Быстрая заявка</h3>
                <div class="modal-body">
                    <ul class="errorlist small text-error"></ul>
                    <form action="/order/fast-claim-form/create/">
                        <input type="hidden" name="user" value="1" id="id_user">

                        <div class="form-group"><p>Так мы быстрее отреагируем на ваш запрос!</p></div>
                        <div class="form-group">
                            <label for="id_typof_choices">Выберите тип заявки:</label>
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
                        <div class="form-group">
                            <input type="email" name="email" value="marychev.mihail@ya.ru" placeholder="your@email.com" required="" id="id_email" class="form-control">
                        </div>
                        <div class="form-group">
                            <input type="text" name="phone" value="+7 (920) 369 79 23" placeholder="Телефон" id="id_phone" class="form-control">
                            <div class="form-text small">Мы никогда не передадим вашу электронную почту кому-либо еще.</div>
                        </div>
                        <div class="form-group">
                            <textarea name="comment" cols="40" rows="4" placeholder="Ваш коментарий" id="id_comment" class="form-control"></textarea>
                        </div>
                        <p><button type="button" id="IAM" class="btn btn-block btn-primary">Отправить</button></p>
                        <p class="small">
                        	<a href="/users/profile/"><i class="fa fa-user"></i> Аккаунт</a>
                        </p>
                    </form>
                </div>
            </div>
        </div>
    </div>`;
    return layout;
}
